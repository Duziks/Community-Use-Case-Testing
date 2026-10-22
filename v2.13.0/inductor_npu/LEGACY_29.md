# 29 个旧兼容节点的自动隔离

沿用流水线原有的 `python -m pytest ...` 命令，无需专用脚本或额外参数。
例如在本目录运行单个节点：

```bash
python -m pytest test_compile.py::TestStandaloneInductor::test_aot_cpp_march_config -v
```

`conftest.py` 自动识别 `legacy_29_nodes.json` 中的 29 个完整 node ID，包括具体参数实例。
只有这些节点会在全新 Python 子进程中执行，并在导入测试之前设置 `has_triton=False`。
其他节点继续使用 pytest 原有执行流程，父进程不修改门控。
11 个测试文件头部保留 `patch_has_triton()`，不再全局强制 False。

子进程的 setup/call/teardown 报告回传给原 pytest，保留 PASS、FAIL、SKIP、XFAIL 及错误详情，
继续由原 pytest 汇总退出码和 `--junitxml` 报告。崩溃或缺失报告会记为失败。
每个节点独立缓存，运行结束后清理；POSIX 下取消入口时同时终止子进程及其编译进程组。

节点选择（如 `-k`、完整 node ID）仍由父 pytest 完成；子进程只执行选中的一个节点。
保留正常的 conftest 自动加载，不使用 `--noconftest`。
这只验证旧兼容模式，不代表这些节点在完整 NPU Inductor 模式下通过。
