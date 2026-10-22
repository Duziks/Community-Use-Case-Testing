# 29 个旧兼容节点的隔离入口

这 29 项由 `legacy_29_nodes.json` 的完整 node ID 限定，包括具体参数实例。
测试文件头部保留 `_dynamo.patch_has_triton()`，将公共检测入口接到 NPU 的实际检测函数；
不再把 `_dynamo.has_triton` 强制改为 False。普通 `pytest` 保持正常后端行为；
需要保留旧兼容验证时，使用下面的独立入口。

在当前目录及匹配的 Python/CANN 环境中，设置当时空闲的物理卡：

```bash
export ASCEND_RT_VISIBLE_DEVICES=<空闲物理卡号>
python run_legacy_29.py --output-dir /你的证据目录/legacy29
python run_legacy_29.py --normal --output-dir /你的证据目录/normal -- test_compile.py test_torchinductor.py -v
```

正常组的文件列表应换为流水线原有测试范围；入口会精确排除清单中的 29 项，
不会排除它们所在的整个文件、类或参数化方法。两条命令使用不同的新进程，
各自有独立的 Inductor/Triton/XDG 缓存。指定的输出目录必须事先不存在。
不要忽略任一命令的退出码。

旧兼容组在子进程导入测试前将 NPU 与公共 `has_triton` 置为 False，进程退出即结束。
这个组的 PASS 仅表示旧兼容模式通过，不代表完整 NPU Inductor 编译能力通过。
正常组不会设置此门控；导入测试 helper 也不会再因此切换到旧模式。

仅运行清单中的部分节点、检查收集结果：

```bash
python run_legacy_29.py --list
python run_legacy_29.py -- 'test_compile.py::TestStandaloneInductor::test_aot_cpp_march_config'
python run_legacy_29.py --collect-only
python run_legacy_29.py --normal --collect-only -- test_compile.py
```

旧兼容入口拒绝清单外节点、文件级/类级选择、重复节点及扩大收集范围的 pytest 参数。
正常入口允许在 `--` 后传递 pytest 选择与输出参数；本入口串行执行，拒绝 xdist `-n`。
使用普通 `python -m pytest` 时，
29 项仍会走正常模式，不会自动获得兼容门控；完整流水线应使用上述两组入口。

每组保存 `run.json`（模式、进程、收集节点、排除节点、逐阶段结果、门控状态）
和 `exit-code.txt`。正常组若没有导入 torch，门控字段为 null；这不等于 False。
不得通过同一 pytest 进程内的 fixture 或临时 monkeypatch 来混跑两种模式，
因为后端注册及 Python 模块缓存不会随一个布尔值恢复而撤销。
