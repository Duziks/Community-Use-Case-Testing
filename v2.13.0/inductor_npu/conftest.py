"""Run only the listed compatibility cases in a fresh legacy process."""

import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile

import pytest


ROOT = Path(__file__).resolve().parent
LEGACY_NODES = frozenset(json.loads((ROOT / "legacy_29_nodes.json").read_text(encoding="utf-8")))
CHILD_NODE = "TORCH_NPU_LEGACY_NODE"
CHILD_REPORT = "TORCH_NPU_LEGACY_REPORT"
BOOTSTRAP = """
import sys
import torch
import torch_npu
from torch_npu.utils import _dynamo
_dynamo.use_jit_script = True
import torch_npu.contrib.transfer_to_npu
if 'torch_npu._inductor' in sys.modules:
    raise RuntimeError('Legacy gate must precede the NPU Inductor import')
_dynamo.has_triton = lambda *args, **kwargs: False
_dynamo.patch_has_triton()
import pytest
raise SystemExit(pytest.main(sys.argv[1:]))
"""


def _node_id(item):
    try:
        path = item.path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return None
    return path + "::" + item.nodeid.partition("::")[2]


def pytest_collection_finish(session):
    target = os.environ.get(CHILD_NODE)
    if target is not None:
        if target not in LEGACY_NODES or [_node_id(item) for item in session.items] != [target]:
            raise pytest.UsageError("Legacy child must collect exactly its requested whitelist node")
        from torch_npu.utils import _dynamo
        from torch.utils import _triton

        if _dynamo.has_triton() or _triton.has_triton():
            raise pytest.UsageError("Legacy child lost its has_triton=False gate")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    if os.environ.get(CHILD_NODE) is not None:
        report = outcome.get_result()
        report.user_properties.append(("legacy_child_pid", os.getpid()))
        data = item.config.hook.pytest_report_to_serializable(config=item.config, report=report)
        with open(os.environ[CHILD_REPORT], "a", encoding="utf-8") as stream:
            stream.write(json.dumps(data) + "\n")


def _stop_child(process):
    # Kill the session as well: compiler descendants can outlive their parent.
    if os.name == "posix":
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            return
    elif process.poll() is None:
        process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        if os.name != "posix":
            process.kill()
    finally:
        if os.name == "posix":
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        process.wait()


def _run_child(command, env):
    process = subprocess.Popen(
        command, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, encoding="utf-8", errors="replace", start_new_session=os.name == "posix",
    )
    previous = signal.getsignal(signal.SIGTERM)

    def terminate(signum, frame):
        _stop_child(process)
        signal.signal(signum, previous)
        if callable(previous):
            previous(signum, frame)
        else:
            signal.signal(signum, signal.SIG_DFL)
            os.kill(os.getpid(), signum)

    signal.signal(signal.SIGTERM, terminate)
    try:
        output, _ = process.communicate()
        return process.returncode, output
    finally:
        signal.signal(signal.SIGTERM, previous)
        _stop_child(process)


def _child_reports(item, target):
    with tempfile.TemporaryDirectory(prefix="npu-legacy-") as directory:
        output = Path(directory)
        report_path = output / "reports.jsonl"
        env = os.environ.copy()
        env.update({
            CHILD_NODE: target, CHILD_REPORT: str(report_path), "PYTEST_ADDOPTS": "",
            "TORCHINDUCTOR_CACHE_DIR": str(output / "inductor"),
            "TRITON_CACHE_DIR": str(output / "triton"), "XDG_CACHE_HOME": str(output / "xdg"),
        })
        filename, _, suffix = target.partition("::")
        command = [
            sys.executable, "-c", BOOTSTRAP, str(ROOT / filename) + "::" + suffix,
            "--rootdir", str(item.config.rootpath), "-o", "addopts=",
            "-o", "cache_dir=" + str(output / "pytest"),
            "-o", "xfail_strict=" + str(item.config.getini("xfail_strict")),
            "--tb=" + item.config.option.tbstyle,
        ]
        if item.config.option.runxfail:
            command.append("--runxfail")
        code, log = _run_child(command, env)
        reports = []
        if report_path.exists():
            try:
                reports = [item.config.hook.pytest_report_from_serializable(
                    config=item.config, data=json.loads(line)
                ) for line in report_path.read_text(encoding="utf-8").splitlines()]
            except (ValueError, TypeError, KeyError):
                reports = []
        phases = [report.when for report in reports if report is not None]
        complete = phases == ["setup", "call", "teardown"] or (
            phases == ["setup", "teardown"] and not reports[0].passed
        )
        if not complete or code not in (0, 1) or (code == 1 and not any(r.failed for r in reports)):
            return [pytest.TestReport(
                nodeid=item.nodeid, location=item.location, keywords={}, outcome="failed",
                longrepr=f"Legacy child did not finish normally (exit {code}).\n{log}", when="call",
            )]
        for report in reports:
            report.nodeid = item.nodeid
            report.location = item.location
        return reports


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    target = _node_id(item)
    if os.environ.get(CHILD_NODE) is not None or target not in LEGACY_NODES:
        return None
    item.ihook.pytest_runtest_logstart(nodeid=item.nodeid, location=item.location)
    try:
        for report in _child_reports(item, target):
            item.ihook.pytest_runtest_logreport(report=report)
    finally:
        item.session._setupstate.teardown_exact(nextitem)
        item.ihook.pytest_runtest_logfinish(nodeid=item.nodeid, location=item.location)
    return True
