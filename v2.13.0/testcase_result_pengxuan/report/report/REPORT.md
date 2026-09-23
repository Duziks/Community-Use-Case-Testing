# A5-37 / torch-213 两项阻断修复后重测

**状态：最终重测报告**  
主批次状态快照：2026-09-22 23:09:17 +08:00。

输入完整性：已检查=True；相对本次修复后记录发生变化的路径=[]。若列表非空，不能把结果视为同一代码版本的完整验证。

## 1. 已完成的修复

1. **缓存接口契约**：在 `torch_npu/contrib/transfer_to_npu.py` 的 `_get_npu_type()` 上添加 `@functools.cache`，保持返回 `"npu"` 的原有语义，同时提供真正的缓存与 `cache_clear` 接口；没有吞掉异常或使用 no-op。同步修改了本地 `pytorch_ascend` 源码和 A5-37 的 torch-213 实际加载文件。
2. **future import 顺序**：将 `test_cache.py`、`test_caching.py`、`test_user_streams.py` 的 NPU 适配前缀移到 future import 之后，保留原测试正文和模块 docstring。
3. 全量收集又暴露同类问题：顶层 `test_triton_extension_backend.py` 引用的 `extension_backends/triton/device_interface.py` 也有错误前缀。本轮一并按相同方法修复该**依赖文件**，但没有递归执行子目录测试；该顶层模块重收集得到 3 条用例，单独串行补跑。

修改和原文件备份见 `fixes.patch`、`fixes.json`、`dependency_fix.patch`、`dependency_fix.json`、`backups/`；本地可提交补丁见 `local_source.patch`。

### 针对性验证

- 2 个新增回归测试通过：迁移函数缓存接口/命中/清空行为；全新进程中先 transfer 再导入 Inductor。
- 顶层 182 个 Python 文件语法检查全部通过；依赖文件另作语法检查并成功重收集。
- 回归测试在真实 A5-37 / torch-213 中执行，不用本机 CPU 模拟 NPU。未修改上游 `pytorch`。
- 版本字符串不因本次源码修补变化；这是 **原有 torch-npu 安装 + 本次补丁**，不是升级到一个新的 wheel。

## 2. 覆盖与当前结果

| 指标 | 数量 |
|---|---:|
| 顶层测试模块 | 176 |
| 成功收集出用例的模块 | 166 |
| 新的收集阻断模块 | 5 |
| 零用例/入口条件模块 | 5 |
| 已收集用例 | 23425 |
| 已记录终结结果 | 23425 |
| 待完成 | 0 |
| passed | 5465 |
| failed | 6636 |
| skipped | 10900 |
| xfail | 97 |
| xpass | 0 |
| 进程崩溃 | 326 |
| 超时 | 1 |

**“修复导入阻断”不等于“所有用例通过”。** 本轮首次进入大量原来未执行的测试体，新暴露的错误单独统计；不把新失败归到已经修复的旧根因。

上轮 pytest 为 176 个模块全部在公共初始化阶段阻断、0 条测试体执行；上轮额外原生入口的 122 条结果与本轮全量 pytest 的覆盖面不同，不能直接比较通过率。

## 3. 按测试模块分类

| 分类 | 模块 | 收集阻断 | 收集用例 | 通过 | 失败 | 跳过 | xfail | 崩溃 | 超时 | 待完成 |
|---|---|---|---|---|---|---|---|---|---|---|
| AOT 编译、打包与部署 | 8 | 1 | 1427 | 56 | 309 | 764 | 0 | 298 | 0 | 0 |
| 编译流程、子进程与 Autograd | 10 | 1 | 1194 | 140 | 187 | 867 | 0 | 0 | 0 | 0 |
| 缓存与序列化 | 6 | 0 | 1270 | 1117 | 7 | 146 | 0 | 0 | 0 | 0 |
| Triton 代码生成、模板与启动 | 14 | 0 | 676 | 67 | 341 | 268 | 0 | 0 | 0 | 0 |
| 矩阵乘、算法选择与自动调优 | 15 | 1 | 928 | 78 | 504 | 346 | 0 | 0 | 0 | 0 |
| 注意力、Softmax 与归约 | 11 | 0 | 2354 | 96 | 550 | 1708 | 0 | 0 | 0 | 0 |
| 图变换、融合与 Lowering | 23 | 0 | 276 | 150 | 82 | 44 | 0 | 0 | 0 | 0 |
| 调度、布局、索引与内存 | 18 | 0 | 377 | 128 | 198 | 40 | 11 | 0 | 0 | 0 |
| 分布式与通信 | 5 | 0 | 45 | 35 | 8 | 2 | 0 | 0 | 0 | 0 |
| Graph、Stream 与设备执行 | 4 | 1 | 79 | 16 | 3 | 3 | 57 | 0 | 0 | 0 |
| CPU 与 C++ Wrapper | 7 | 0 | 2737 | 1030 | 1373 | 333 | 0 | 0 | 1 | 0 |
| CUDA 专属与其他后端 | 18 | 0 | 644 | 41 | 354 | 249 | 0 | 0 | 0 | 0 |
| 算子、精度与随机性 | 10 | 0 | 1669 | 42 | 694 | 928 | 0 | 5 | 0 | 0 |
| Inductor 综合、动态形状与 OpInfo | 9 | 0 | 9113 | 1995 | 1941 | 5133 | 26 | 18 | 0 | 0 |
| 诊断、性能与基础设施 | 18 | 1 | 636 | 474 | 85 | 69 | 3 | 5 | 0 | 0 |

详见 `modules.md`、`modules.json`；逐条结果见 `cases.md`、`cases_index.json`。

## 4. 错误分类

| 错误类别 | 用例数 | 代表用例 |
|---|---|---|
| R00 单例/阶段超时（非普通断言失败） | 1 | test_cpu_repro.py::CPUReproTests::test_vec_compare_op_cpu_only |
| R00 进程崩溃（单列，不把后续用例判失败） | 326 | test_torchbind.py::TestTorchbind::test_aoti_torchbind_name_collision |
| R01 NPU codegen/scheduler 注册或设备支持缺口 | 3643 | test_alignment.py::NPUTests::test_alignment_without_custom_op_npu |
| R02 CacheBase.get_system 缓存接口缺口（非本次 get_gpu_type 修复） | 1 | test_codecache.py::TestCacheKeyStrategy::test_cache_base_get_system_uses_system_strategy |
| R03 自动调优没有可用算法候选 | 423 | test_max_autotune_blackwell.py::TestMaxAutotuneBlackwell::test_blackwell_max_autotune_addmm_persistent_tma_a_transposed_False_b_transposed_False_dynamic_False_tma_store_False_epilogue_subtile_1 |
| R04 CUDA 专属接口/后端残留 | 1722 | test_torchinductor_opinfo_properties.py::TestOpInfoPropertiesPRIVATEUSE1::test_batch_invariance_abs_backend_aot_eager_decomp_partition_npu_bfloat16 |
| R05 Triton 多驱动同时激活 | 42 | test_triton_kernels.py::CustomOpTests::test_wrap_triton_disabled_in_triton_op |
| R06 NPU Runtime/算子执行错误 | 90 | test_alignment.py::NPUTests::test_Q4_K_dequantization_npu |
| R07 NPU convolution Meta 一维参数解包 | 1 | test_utils.py::TestUtilsPRIVATEUSE1::test_flops_fx_npu |
| R08 profiler/benchmark 接口或行为不兼容 | 4 | test_minifier_isolate.py::MinifierIsolateTests::test_after_aot_gpu_runtime_error |
| R09 依赖或测试资源缺失 | 4 | test_torchinductor.py::GPUTests::test_lite_triton_kernel_wrapper_functional_npu |
| R10 条件初始化/符号未定义（适配风险） | 384 | test_triton_kernels.py::KernelTests::test_constexpr_dynamic_shapes_wrapped_False_autotune_False |
| R11 Dynamo/图捕获不支持 | 111 | test_compiled_optimizers.py::CompiledOptimizerTests::test_adadelta_cpu |
| R13 API/属性/注册表不匹配 | 45 | test_comm_analysis.py::TestNcclEstimateDeviceResolution::test_fake_backend_falls_back_to_analytical |
| R14 数值/张量结果断言 | 25 | test_online_softmax.py::TestOnlineSoftmax::test_prepare_softmax_after_partitioning |
| R15 测试预期/结构/计数断言 | 68 | test_comm_analysis.py::TestNcclEstimateDeviceResolution::test_multi_backend_pg_resolves_to_nccl |
| R16 其他 RuntimeError（不能直接等同设备故障） | 42 | test_compiled_optimizers.py::CompiledOptimizerParityTestsPRIVATEUSE1::test_correctness_SparseAdam_use_closure_False_npu_float32 |
| R99 其他错误（查看原始堆栈） | 31 | test_torchinductor.py::GPUTests::test_clone_dropout_npu |

分类根据真实错误信息与堆栈进行第一层归类，不等于每一类已经完成底层根因修复：

- `Device npu not supported` / 无 scheduling constructor：标记设备注册或支持缺口；需进一步区分迁移适配、初始化时序和具体后端能力。
- **`CacheBase.get_system.cache_clear()` 的同名 AttributeError 与本次修复的 `get_gpu_type` 不是同一个函数**，不能仅搜索 `cache_clear` 就断言本次修复无效。
- CUDA 专属接口（如 `_cuda_synchronize`、CUDA allocator、cuBLASLt）、ROCm 属性假设、Triton 多驱动激活：优先标记为 NPU 迁移/后端选择兼容问题，而非数值算子缺陷。
- NPU `aclnn*` / ACL 错误按真实 Runtime 分类，发生后换进程并检查设备健康。
- AOT 加载阶段出现的 SIGABRT 等进程崩溃：保留 Python fatal stack 和退出码；没有足够证据时不猜测 C++ 底层原因，也不误计后续未执行用例失败。
- assertion、数值差异、Dynamo Unsupported、缺少候选算法等单列；不能把所有 RuntimeError 都当成设备上下文损坏。
- 明确的适配错误是已修复的 future import 顺序；其他兼容分类的具体修复归属需结合用例与后端进一步判断，不为了降低失败数而修改断言或强行跳过。

## 5. 剩余收集阻断

| 模块 | 实际错误 | 日志 |
|---|---|---|
| test_aot_inductor_package.py | E   ModuleNotFoundError: No module named 'parameterized' | collection/test_aot_inductor_package/output.log |
| test_compiled_autograd.py | E   FileNotFoundError: [Errno 2] No such file or directory: '/home/p00927906/workspace/triton_dev/Community-Use-Case-Testing-v2.10.0/v2.13.0/test_autograd.py' | collection/test_compiled_autograd/output.log |
| test_cudagraph_trees_expandable_segments.py | E   ModuleNotFoundError: No module named 'tools' | collection/test_cudagraph_trees_expandable_segments/output.log |
| test_decompose_mem_bound_mm.py | E   AttributeError: 'NoneType' object has no attribute 'split' | collection/test_decompose_mem_bound_mm/output.log |
| test_segmented_tree.py | E   ModuleNotFoundError: No module named 'hypothesis' | collection/test_segmented_tree/output.log |

这些是原始公共初始化问题消除后才暴露的依赖、上游测试资源或设备属性问题。本轮没有擅自安装新依赖、复制缺失的上游测试树或修改其他不相关用例。

## 6. 隔离、健康检查与统计规则

- 使用当时空闲的设备 **0、1、4、5、6、7**，避开忙碌的 2、3；每个工作进程仅可见单卡，**不代表多卡覆盖**。
- 每个执行批次最多 100 条用例，以模块优先的公平队列调度。pytest `-x`：遇到第一条 failure/error 即退出该进程，剩余用例重新排队，在全新 Python 进程继续。
- 每条用例按完整 nodeid 去重。进程崩溃/超时只记录当前未终结用例；其后的用例不批量判失败。
- 遇到 RuntimeError、崩溃或超时，在新进程执行 eager NPU 运算并同步；健康检查连续 3 次失败才隔离该工作设备。当前健康检查记录 **6445** 次，非零退出/超时 **5** 次。原始记录见 `health.json` 与 `followup/health.json`。
- 300 秒无测试事件看门狗；超时独立计数，不算普通功能断言失败。没有重置 NPU 或操作其他人的进程。
- 为本次审计进程及其子进程限制 core dump 大小，保留文本崩溃堆栈；没有修改系统全局 core 配置，也没有删除用户文件。
- 新建按设备区分的本次编译缓存；不清理用户原有缓存。外部 pytest 插件自动加载关闭；仅使用事件记录插件。
- passed 包括 CPU、纯 Python 和 NPU 测试，不能当作 NPU kernel 通过数。skip/xfail/xpass、收集失败、零用例和未完成项分列；不把它们合并成“通过”。
- 修复依赖文件后的 3 条补跑等待主批次退出后才执行，避免同卡并发干扰。

## 7. 环境与证据

实际包版本：`{"torch": "2.13.0+cpu", "torch-npu": "2.13.0.dev20260911", "triton": "3.6.0", "numpy": "1.26.4", "pytest": "8.4.2"}`。Python：`3.11.15`。

远端目录：`/home/p00927906/workspace/inductor_retest_20260922_fixed/`。

- `collection_summary.json`：首次修复后的 176 模块收集；`followup/collection_summary.json` 覆盖依赖修复模块的旧结果。
- `execution_summary.json`、`execution/*/state.json`：可恢复进度与逐次退出码；`followup/` 保存 3 条补跑。
- `execution/*/*.log`、`*.jsonl`：完整输出和阶段事件；`cases.json` 保存包含堆栈的逐条结果。
- `regression.log`、`syntax_check.json`、`fixes*.json/patch`、`dependency_fix*`：修复验证和备份记录。
- `all_execution_ended.json` 出现表示两批执行器都结束；仍需核对本报告“待完成”和进度中的 blocked/runner_error，不能只看控制进程退出码。

本报告在任务运行期间可重复生成；只有标题为“最终重测报告”且待完成为 0 时，才表示所有成功收集的用例都拿到了结果。收集失败的模块仍未获得功能验证。
