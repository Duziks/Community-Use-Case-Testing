"""Run the 29 legacy cases in a fresh process, or run their normal complement."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "legacy_29_nodes.json"


def read_nodes():
    nodes = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if len(nodes) != 29 or len(set(nodes)) != 29:
        raise ValueError("The legacy manifest must contain exactly 29 unique node IDs")
    for node in nodes:
        filename, separator, test = node.partition("::")
        if not separator or not test or Path(filename).name != filename:
            raise ValueError(f"Invalid legacy node ID: {node}")
    return nodes


def item_id(item):
    try:
        filename = item.path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return None
    suffix = item.nodeid.partition("::")[2]
    return f"{filename}::{suffix}"


def gate_state():
    result = {}
    for name in ("torch_npu.utils._dynamo", "torch.utils._triton"):
        module = sys.modules.get(name)
        result[name] = None if module is None else bool(module.has_triton())
    return result


def worker(mode, targets, nodes, output, collect_only):
    metadata = {"mode": mode, "pid": os.getpid(), "python": sys.executable,
                "requested": targets, "collected": [], "deselected": [], "reports": []}
    if mode == "legacy":
        # Only this fresh child imports and changes the compiler availability gate.
        import torch
        import torch_npu
        from torch_npu.utils import _dynamo

        _dynamo.use_jit_script = True
        import torch_npu.contrib.transfer_to_npu  # noqa: F401

        if "torch_npu._inductor" in sys.modules:
            raise RuntimeError("NPU Inductor was already imported; legacy mode requires a fresh process")
        _dynamo.has_triton = lambda *args, **kwargs: False
        _dynamo.patch_has_triton()
        metadata["imports"] = {
            module.__name__: {"version": module.__version__, "file": module.__file__}
            for module in (torch, torch_npu)
        }
        metadata["gate_before_collection"] = gate_state()

    import pytest

    class Scope:
        def pytest_configure(self, config):
            if getattr(config.option, "numprocesses", None) not in (None, 0):
                raise pytest.UsageError("This scoped entry runs serially; do not pass pytest-xdist -n")

        @pytest.hookimpl(trylast=True)
        def pytest_collection_modifyitems(self, config, items):
            if mode == "normal":
                removed = [item for item in items if item_id(item) in nodes]
                items[:] = [item for item in items if item_id(item) not in nodes]
                metadata["deselected"] = [item_id(item) for item in removed]
                if removed:
                    config.hook.pytest_deselected(items=removed)
            else:
                actual = [item_id(item) for item in items]
                if len(actual) != len(targets) or set(actual) != set(targets):
                    raise pytest.UsageError("Legacy collection must match the requested exact node IDs")

        def pytest_collection_finish(self, session):
            metadata["collected"] = [item_id(item) or item.nodeid for item in session.items]
            metadata["gate_after_collection"] = gate_state()
            (output / "collection.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
            if mode == "legacy":
                actual = metadata["collected"]
                if len(actual) != len(targets) or set(actual) != set(targets):
                    raise pytest.UsageError("Legacy collection changed after scope validation")

        def pytest_runtest_logreport(self, report):
            event = {"nodeid": report.nodeid, "when": report.when,
                     "outcome": report.outcome, "wasxfail": getattr(report, "wasxfail", None)}
            metadata["reports"].append(event)
            with (output / "events.jsonl").open("a", encoding="utf-8") as stream:
                stream.write(json.dumps(event) + "\n")

    arguments = [*targets, "--rootdir", str(ROOT), "-o", f"cache_dir={output / 'pytest'}"]
    if mode == "legacy":
        arguments += ["-vv", "--tb=short", "-o", "addopts=", "--noconftest"]
    if collect_only:
        arguments.append("--collect-only")
    print(f"MODE={mode}; PID={os.getpid()}; OUTPUT={output}", flush=True)
    if mode == "legacy":
        print("Legacy compatibility only; this does not validate the NPU Inductor backend", flush=True)
    try:
        code = int(pytest.main(arguments, plugins=[Scope()]))
        metadata["exit_code"] = code
        return code
    finally:
        metadata["gate_after_pytest"] = gate_state()
        metadata["test_module_files"] = {
            name: str(Path(module.__file__).resolve())
            for name, module in list(sys.modules.items())
            if getattr(module, "__file__", None)
            and Path(module.__file__).resolve().is_relative_to(ROOT.parent)
        }
        (output / "run.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normal", action="store_true", help="Run normal pytest targets, excluding the 29 legacy nodes")
    parser.add_argument("--collect-only", action="store_true")
    parser.add_argument("--list", action="store_true", help="Print the exact legacy node IDs without importing torch")
    parser.add_argument("--output-dir", type=Path, help="New evidence/cache directory; must not already exist")
    parser.add_argument("--_worker", choices=("normal", "legacy"), help=argparse.SUPPRESS)
    parser.add_argument("targets", nargs=argparse.REMAINDER, help="Use -- before exact legacy IDs or normal pytest arguments")
    args = parser.parse_args()
    nodes = read_nodes()
    if args.list:
        print("\n".join(nodes))
        return 0
    targets = args.targets[1:] if args.targets[:1] == ["--"] else args.targets
    mode = args._worker or ("normal" if args.normal else "legacy")
    if mode == "legacy":
        targets = targets or nodes
        if len(set(targets)) != len(targets) or any(node not in nodes for node in targets):
            parser.error("Legacy mode accepts only unique, exact node IDs from --list; file/class selectors are rejected")
    elif not targets:
        parser.error("Normal mode requires explicit pytest targets after --")

    if args._worker:
        if args.output_dir is None or not args.output_dir.is_dir():
            parser.error("Worker requires an existing output directory")
        os.chdir(ROOT)
        return worker(mode, targets, nodes, args.output_dir, args.collect_only)

    if args.output_dir is None:
        output = Path(tempfile.mkdtemp(prefix=f"inductor-{mode}-"))
    else:
        output = args.output_dir.resolve()
        output.mkdir(parents=True, exist_ok=False)
    env = os.environ.copy()
    env.update(TORCHINDUCTOR_CACHE_DIR=str(output / "inductor"),
               TRITON_CACHE_DIR=str(output / "triton"), XDG_CACHE_HOME=str(output / "xdg"))
    if mode == "legacy":
        env.update(PYTEST_ADDOPTS="", PYTEST_DISABLE_PLUGIN_AUTOLOAD="1")
    command = [sys.executable, str(Path(__file__).resolve()), "--_worker", mode,
               "--output-dir", str(output)]
    if args.collect_only:
        command.append("--collect-only")
    command += ["--", *targets]
    print(f"Starting a fresh {mode} process; evidence: {output}", flush=True)
    code = subprocess.run(command, cwd=ROOT, env=env).returncode
    (output / "exit-code.txt").write_text(str(code) + "\n", encoding="utf-8")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
