# 模块级重测明细

最终重测报告。收集数不等于真正执行测试体数量，skip/xfail 单列。

| 模块文件 | 功能分类 | 状态 | 收集 | 通过 | 失败 | 跳过 | xfail | xpass | 崩溃 | 超时 | 未完成 | 收集日志 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| test_alignment.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 12 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_alignment/output.log |
| test_analysis.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 30 | 6 | 0 | 19 | 5 | 0 | 0 | 0 | 0 | collection/test_analysis/output.log |
| test_aot_inductor.py | AOT 编译、打包与部署 | 已执行全部已收集用例 | 1028 | 29 | 284 | 553 | 0 | 0 | 162 | 0 | 0 | collection/test_aot_inductor/output.log |
| test_aot_inductor_arrayref.py | AOT 编译、打包与部署 | 已执行全部已收集用例 | 340 | 14 | 3 | 205 | 0 | 0 | 118 | 0 | 0 | collection/test_aot_inductor_arrayref/output.log |
| test_aot_inductor_custom_ops.py | AOT 编译、打包与部署 | 已执行全部已收集用例 | 41 | 4 | 19 | 0 | 0 | 0 | 18 | 0 | 0 | collection/test_aot_inductor_custom_ops/output.log |
| test_aot_inductor_package.py | AOT 编译、打包与部署 | 收集失败 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_aot_inductor_package/output.log |
| test_aot_inductor_utils.py | AOT 编译、打包与部署 | 零用例/入口条件 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_aot_inductor_utils/output.log |
| test_aoti_cache_dir.py | AOT 编译、打包与部署 | 已执行全部已收集用例 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_aoti_cache_dir/output.log |
| test_aoti_cross_compile_windows.py | AOT 编译、打包与部署 | 已执行全部已收集用例 | 14 | 8 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | collection/test_aoti_cross_compile_windows/output.log |
| test_aoti_torchbind_constants.py | AOT 编译、打包与部署 | 已执行全部已收集用例 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_aoti_torchbind_constants/output.log |
| test_async_compile.py | 编译流程、子进程与 Autograd | 已执行全部已收集用例 | 42 | 6 | 0 | 36 | 0 | 0 | 0 | 0 | 0 | collection/test_async_compile/output.log |
| test_augmented_graph_helper.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 20 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_augmented_graph_helper/output.log |
| test_auto_chunker.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 14 | 0 | 6 | 8 | 0 | 0 | 0 | 0 | 0 | collection/test_auto_chunker/output.log |
| test_auto_functionalize.py | 编译流程、子进程与 Autograd | 已执行全部已收集用例 | 44 | 43 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | collection/test_auto_functionalize/output.log |
| test_autoheuristic.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 12 | 2 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | collection/test_autoheuristic/output.log |
| test_b2b_gemm.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 9 | 0 | 6 | 3 | 0 | 0 | 0 | 0 | 0 | collection/test_b2b_gemm/output.log |
| test_benchmark_fusion.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 6 | 4 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_benchmark_fusion/output.log |
| test_benchmarking.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 27 | 13 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | collection/test_benchmarking/output.log |
| test_best_config.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_best_config/output.log |
| test_binary_folding.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_binary_folding/output.log |
| test_block_analysis.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 10 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_block_analysis/output.log |
| test_block_ptr_store_dtype.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_block_ptr_store_dtype/output.log |
| test_cache.py | 缓存与序列化 | 已执行全部已收集用例 | 728 | 728 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_cache/output.log |
| test_cache_dir_utils.py | 缓存与序列化 | 已执行全部已收集用例 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_cache_dir_utils/output.log |
| test_caching.py | 缓存与序列化 | 已执行全部已收集用例 | 212 | 212 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_caching/output.log |
| test_ck_backend.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 41 | 0 | 0 | 41 | 0 | 0 | 0 | 0 | 0 | collection/test_ck_backend/output.log |
| test_codecache.py | 缓存与序列化 | 已执行全部已收集用例 | 317 | 167 | 7 | 143 | 0 | 0 | 0 | 0 | 0 | collection/test_codecache/output.log |
| test_codegen_triton.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 16 | 13 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | collection/test_codegen_triton/output.log |
| test_collective_autotuning.py | 分布式与通信 | 已执行全部已收集用例 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_collective_autotuning/output.log |
| test_combo_kernels.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 125 | 3 | 0 | 122 | 0 | 0 | 0 | 0 | 0 | collection/test_combo_kernels/output.log |
| test_comm_analysis.py | 分布式与通信 | 已执行全部已收集用例 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_comm_analysis/output.log |
| test_compile.py | 编译流程、子进程与 Autograd | 已执行全部已收集用例 | 13 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_compile/output.log |
| test_compile_subprocess.py | 编译流程、子进程与 Autograd | 已执行全部已收集用例 | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | collection/test_compile_subprocess/output.log |
| test_compile_worker.py | 编译流程、子进程与 Autograd | 已执行全部已收集用例 | 23 | 14 | 2 | 7 | 0 | 0 | 0 | 0 | 0 | collection/test_compile_worker/output.log |
| test_compiled_autograd.py | 编译流程、子进程与 Autograd | 收集失败 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_compiled_autograd/output.log |
| test_compiled_fx_graph_serialization.py | 编译流程、子进程与 Autograd | 已执行全部已收集用例 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_compiled_fx_graph_serialization/output.log |
| test_compiled_optimizers.py | 编译流程、子进程与 Autograd | 已执行全部已收集用例 | 314 | 6 | 124 | 184 | 0 | 0 | 0 | 0 | 0 | collection/test_compiled_optimizers/output.log |
| test_config.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 16 | 13 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_config/output.log |
| test_control_deps.py | 编译流程、子进程与 Autograd | 已执行全部已收集用例 | 6 | 1 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_control_deps/output.log |
| test_control_flow.py | 编译流程、子进程与 Autograd | 已执行全部已收集用例 | 747 | 54 | 55 | 638 | 0 | 0 | 0 | 0 | 0 | collection/test_control_flow/output.log |
| test_cooperative_reductions.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 167 | 0 | 163 | 4 | 0 | 0 | 0 | 0 | 0 | collection/test_cooperative_reductions/output.log |
| test_coordinate_descent_tuner.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 14 | 10 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_coordinate_descent_tuner/output.log |
| test_cpp_wrapper_custom_ops.py | CPU 与 C++ Wrapper | 已执行全部已收集用例 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_cpp_wrapper_custom_ops/output.log |
| test_cpp_wrapper_hipify.py | CPU 与 C++ Wrapper | 已执行全部已收集用例 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_cpp_wrapper_hipify/output.log |
| test_cpu_cpp_wrapper.py | CPU 与 C++ Wrapper | 零用例/入口条件 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_cpu_cpp_wrapper/output.log |
| test_cpu_repro.py | CPU 与 C++ Wrapper | 已执行全部已收集用例 | 789 | 779 | 5 | 4 | 0 | 0 | 0 | 1 | 0 | collection/test_cpu_repro/output.log |
| test_cpu_select_algorithm.py | CPU 与 C++ Wrapper | 已执行全部已收集用例 | 1895 | 226 | 1356 | 313 | 0 | 0 | 0 | 0 | 0 | collection/test_cpu_select_algorithm/output.log |
| test_cuda_repro.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 113 | 7 | 102 | 4 | 0 | 0 | 0 | 0 | 0 | collection/test_cuda_repro/output.log |
| test_cudacodecache.py | 缓存与序列化 | 已执行全部已收集用例 | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | collection/test_cudacodecache/output.log |
| test_cudagraph_trees.py | Graph、Stream 与设备执行 | 零用例/入口条件 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_cudagraph_trees/output.log |
| test_cudagraph_trees_expandable_segments.py | Graph、Stream 与设备执行 | 收集失败 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_cudagraph_trees_expandable_segments/output.log |
| test_custom_lowering.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 6 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_custom_lowering/output.log |
| test_custom_op_autotune.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 23 | 2 | 14 | 7 | 0 | 0 | 0 | 0 | 0 | collection/test_custom_op_autotune/output.log |
| test_custom_op_out_lowering.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_custom_op_out_lowering/output.log |
| test_custom_partitioner_fn.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_custom_partitioner_fn/output.log |
| test_custom_post_grad_passes.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_custom_post_grad_passes/output.log |
| test_cutedsl_grouped_mm.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 24 | 0 | 0 | 24 | 0 | 0 | 0 | 0 | 0 | collection/test_cutedsl_grouped_mm/output.log |
| test_cutedsl_template.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 0 | 0 | collection/test_cutedsl_template/output.log |
| test_cutlass_backend.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 194 | 5 | 183 | 6 | 0 | 0 | 0 | 0 | 0 | collection/test_cutlass_backend/output.log |
| test_cutlass_evt.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 8 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | collection/test_cutlass_evt/output.log |
| test_cutlass_fallback.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 12 | 8 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | collection/test_cutlass_fallback/output.log |
| test_debug_graph_dump.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 6 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_debug_graph_dump/output.log |
| test_debug_trace.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 4 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | collection/test_debug_trace/output.log |
| test_decompose_mem_bound_mm.py | 矩阵乘、算法选择与自动调优 | 收集失败 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_decompose_mem_bound_mm/output.log |
| test_dependencies.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_dependencies/output.log |
| test_deterministic.py | 算子、精度与随机性 | 已执行全部已收集用例 | 34 | 2 | 30 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_deterministic/output.log |
| test_device_assert.py | Graph、Stream 与设备执行 | 已执行全部已收集用例 | 8 | 3 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_device_assert/output.log |
| test_distributed_patterns.py | 分布式与通信 | 已执行全部已收集用例 | 20 | 17 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_distributed_patterns/output.log |
| test_dropout_align_random_eager.py | 算子、精度与随机性 | 已执行全部已收集用例 | 13 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | collection/test_dropout_align_random_eager/output.log |
| test_efficient_conv_bn_eval.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_efficient_conv_bn_eval/output.log |
| test_embedding.py | 算子、精度与随机性 | 已执行全部已收集用例 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_embedding/output.log |
| test_exc_lowering_stack_trace.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_exc_lowering_stack_trace/output.log |
| test_extension_backend.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 3 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_extension_backend/output.log |
| test_external_callables.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_external_callables/output.log |
| test_flex_attention.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 560 | 0 | 0 | 560 | 0 | 0 | 0 | 0 | 0 | collection/test_flex_attention/output.log |
| test_flex_aux_vectorization.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 17 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_flex_aux_vectorization/output.log |
| test_flex_decoding.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 570 | 0 | 1 | 569 | 0 | 0 | 0 | 0 | 0 | collection/test_flex_decoding/output.log |
| test_flex_flash.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 251 | 7 | 0 | 244 | 0 | 0 | 0 | 0 | 0 | collection/test_flex_flash/output.log |
| test_flex_gemm_runtime.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 7 | 1 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | collection/test_flex_gemm_runtime/output.log |
| test_foreach.py | 算子、精度与随机性 | 已执行全部已收集用例 | 615 | 20 | 0 | 595 | 0 | 0 | 0 | 0 | 0 | collection/test_foreach/output.log |
| test_fp8.py | 算子、精度与随机性 | 已执行全部已收集用例 | 320 | 2 | 81 | 237 | 0 | 0 | 0 | 0 | 0 | collection/test_fp8/output.log |
| test_fused_attention.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 57 | 56 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | collection/test_fused_attention/output.log |
| test_fusion_regions.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 7 | 4 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_fusion_regions/output.log |
| test_fuzzer.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 11 | 9 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_fuzzer/output.log |
| test_fx_fusion.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_fx_fusion/output.log |
| test_fxir_backend.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 77 | 15 | 62 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_fxir_backend/output.log |
| test_gpu_cpp_wrapper.py | CPU 与 C++ Wrapper | 已执行全部已收集用例 | 18 | 0 | 2 | 16 | 0 | 0 | 0 | 0 | 0 | collection/test_gpu_cpp_wrapper/output.log |
| test_gpu_select_algorithm.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 58 | 0 | 58 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_gpu_select_algorithm/output.log |
| test_graph_transform_observer.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_graph_transform_observer/output.log |
| test_grid_sampler_codegen.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | collection/test_grid_sampler_codegen/output.log |
| test_group_batch_fusion.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 15 | 2 | 2 | 11 | 0 | 0 | 0 | 0 | 0 | collection/test_group_batch_fusion/output.log |
| test_halide.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 4 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | collection/test_halide/output.log |
| test_helion_kernels.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_helion_kernels/output.log |
| test_indexing.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 56 | 53 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | collection/test_indexing/output.log |
| test_inductor_annotations.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_inductor_annotations/output.log |
| test_inductor_freezing.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 24 | 21 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_inductor_freezing/output.log |
| test_inductor_scheduler.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 24 | 11 | 3 | 4 | 6 | 0 | 0 | 0 | 0 | collection/test_inductor_scheduler/output.log |
| test_inductor_utils.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 4 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_inductor_utils/output.log |
| test_inplace_padding.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 9 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_inplace_padding/output.log |
| test_inplacing_pass.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 26 | 14 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_inplacing_pass/output.log |
| test_interval_mask_packing.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_interval_mask_packing/output.log |
| test_kernel_benchmark.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 20 | 0 | 17 | 3 | 0 | 0 | 0 | 0 | 0 | collection/test_kernel_benchmark/output.log |
| test_kernel_optimization.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_kernel_optimization/output.log |
| test_layout_optim.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 11 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_layout_optim/output.log |
| test_lookup_table.py | 算子、精度与随机性 | 已执行全部已收集用例 | 37 | 0 | 0 | 37 | 0 | 0 | 0 | 0 | 0 | collection/test_lookup_table/output.log |
| test_loop_ordering.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 90 | 14 | 76 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_loop_ordering/output.log |
| test_low_contention_collectives.py | 分布式与通信 | 已执行全部已收集用例 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_low_contention_collectives/output.log |
| test_max_autotune.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 577 | 51 | 274 | 252 | 0 | 0 | 0 | 0 | 0 | collection/test_max_autotune/output.log |
| test_max_autotune_blackwell.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 127 | 3 | 124 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_max_autotune_blackwell/output.log |
| test_mem_estimation.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_mem_estimation/output.log |
| test_memory.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 9 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_memory/output.log |
| test_memory_planning.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 4 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | collection/test_memory_planning/output.log |
| test_metrics.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 6 | 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | collection/test_metrics/output.log |
| test_minifier.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 14 | 5 | 6 | 0 | 0 | 0 | 3 | 0 | 0 | collection/test_minifier/output.log |
| test_minifier_isolate.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_minifier_isolate/output.log |
| test_minifier_utils.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_minifier_utils/output.log |
| test_mix_order_reduction.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 498 | 2 | 192 | 304 | 0 | 0 | 0 | 0 | 0 | collection/test_mix_order_reduction/output.log |
| test_mkldnn_pattern_matcher.py | CPU 与 C++ Wrapper | 已执行全部已收集用例 | 31 | 21 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_mkldnn_pattern_matcher/output.log |
| test_mmdecomp.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 31 | 4 | 0 | 27 | 0 | 0 | 0 | 0 | 0 | collection/test_mmdecomp/output.log |
| test_move_constructors_to_gpu.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 8 | 2 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | collection/test_move_constructors_to_gpu/output.log |
| test_mps_basic.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 57 | 0 | 0 | 57 | 0 | 0 | 0 | 0 | 0 | collection/test_mps_basic/output.log |
| test_multi_kernel.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 19 | 0 | 17 | 2 | 0 | 0 | 0 | 0 | 0 | collection/test_multi_kernel/output.log |
| test_native_matmul.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 14 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_native_matmul/output.log |
| test_needs_exact_strides.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 5 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_needs_exact_strides/output.log |
| test_nested_reduction.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 180 | 0 | 160 | 20 | 0 | 0 | 0 | 0 | 0 | collection/test_nested_reduction/output.log |
| test_nv_universal_gemm.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 72 | 3 | 0 | 69 | 0 | 0 | 0 | 0 | 0 | collection/test_nv_universal_gemm/output.log |
| test_online_softmax.py | 注意力、Softmax 与归约 | 已执行全部已收集用例 | 35 | 1 | 34 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_online_softmax/output.log |
| test_op_completeness.py | 算子、精度与随机性 | 已执行全部已收集用例 | 5 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | collection/test_op_completeness/output.log |
| test_op_dtype_prop.py | 算子、精度与随机性 | 已执行全部已收集用例 | 623 | 1 | 580 | 42 | 0 | 0 | 0 | 0 | 0 | collection/test_op_dtype_prop/output.log |
| test_optimize_indexing.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 15 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_optimize_indexing/output.log |
| test_ordered_set.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 401 | 386 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | collection/test_ordered_set/output.log |
| test_origami.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 9 | 2 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | collection/test_origami/output.log |
| test_pad_as_cat.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_pad_as_cat/output.log |
| test_pad_mm.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 19 | 0 | 0 | 19 | 0 | 0 | 0 | 0 | 0 | collection/test_pad_mm/output.log |
| test_pad_mm_utils.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_pad_mm_utils/output.log |
| test_padding.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 57 | 3 | 44 | 10 | 0 | 0 | 0 | 0 | 0 | collection/test_padding/output.log |
| test_pallas.py | CUDA 专属与其他后端 | 零用例/入口条件 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_pallas/output.log |
| test_pattern_matcher.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 98 | 40 | 42 | 16 | 0 | 0 | 0 | 0 | 0 | collection/test_pattern_matcher/output.log |
| test_perf.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 68 | 1 | 53 | 14 | 0 | 0 | 0 | 0 | 0 | collection/test_perf/output.log |
| test_profiler.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 8 | 1 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | collection/test_profiler/output.log |
| test_provenance_tracing.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 17 | 6 | 2 | 7 | 0 | 0 | 2 | 0 | 0 | collection/test_provenance_tracing/output.log |
| test_quantization.py | 算子、精度与随机性 | 已执行全部已收集用例 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_quantization/output.log |
| test_remote_cache.py | 缓存与序列化 | 已执行全部已收集用例 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_remote_cache/output.log |
| test_scatter_optimization.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 9 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_scatter_optimization/output.log |
| test_segmented_tree.py | 诊断、性能与基础设施 | 收集失败 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_segmented_tree/output.log |
| test_select_algorithm.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 40 | 5 | 2 | 33 | 0 | 0 | 0 | 0 | 0 | collection/test_select_algorithm/output.log |
| test_selective_lowering.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_selective_lowering/output.log |
| test_simd_range_trees.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_simd_range_trees/output.log |
| test_smoke.py | Inductor 综合、动态形状与 OpInfo | 已执行全部已收集用例 | 3 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_smoke/output.log |
| test_snode_runtime.py | 调度、布局、索引与内存 | 已执行全部已收集用例 | 27 | 2 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_snode_runtime/output.log |
| test_split_cat_fx_aten_passes.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 5 | 1 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | collection/test_split_cat_fx_aten_passes/output.log |
| test_split_cat_fx_passes.py | 图变换、融合与 Lowering | 已执行全部已收集用例 | 11 | 10 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_split_cat_fx_passes/output.log |
| test_static_triton_launcher.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 28 | 3 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | collection/test_static_triton_launcher/output.log |
| test_subgraph_choice.py | 矩阵乘、算法选择与自动调优 | 已执行全部已收集用例 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_subgraph_choice/output.log |
| test_symm_mem_registry.py | 分布式与通信 | 已执行全部已收集用例 | 19 | 17 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_symm_mem_registry/output.log |
| test_template_heuristics_registry.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_template_heuristics_registry/output.log |
| test_torchbind.py | 算子、精度与随机性 | 已执行全部已收集用例 | 16 | 10 | 0 | 1 | 0 | 0 | 5 | 0 | 0 | collection/test_torchbind/output.log |
| test_torchinductor.py | Inductor 综合、动态形状与 OpInfo | 已执行全部已收集用例 | 1304 | 116 | 1074 | 108 | 0 | 0 | 6 | 0 | 0 | collection/test_torchinductor/output.log |
| test_torchinductor_codegen_config_overrides.py | Inductor 综合、动态形状与 OpInfo | 已执行全部已收集用例 | 6 | 2 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | collection/test_torchinductor_codegen_config_overrides/output.log |
| test_torchinductor_codegen_dynamic_shapes.py | Inductor 综合、动态形状与 OpInfo | 已执行全部已收集用例 | 1240 | 717 | 9 | 508 | 0 | 0 | 6 | 0 | 0 | collection/test_torchinductor_codegen_dynamic_shapes/output.log |
| test_torchinductor_dynamic_shapes.py | Inductor 综合、动态形状与 OpInfo | 已执行全部已收集用例 | 1311 | 881 | 12 | 412 | 0 | 0 | 6 | 0 | 0 | collection/test_torchinductor_dynamic_shapes/output.log |
| test_torchinductor_opinfo.py | Inductor 综合、动态形状与 OpInfo | 已执行全部已收集用例 | 3737 | 0 | 0 | 3737 | 0 | 0 | 0 | 0 | 0 | collection/test_torchinductor_opinfo/output.log |
| test_torchinductor_opinfo_properties.py | Inductor 综合、动态形状与 OpInfo | 已执行全部已收集用例 | 1134 | 268 | 840 | 0 | 26 | 0 | 0 | 0 | 0 | collection/test_torchinductor_opinfo_properties/output.log |
| test_torchinductor_strided_blocks.py | Inductor 综合、动态形状与 OpInfo | 已执行全部已收集用例 | 323 | 0 | 0 | 323 | 0 | 0 | 0 | 0 | 0 | collection/test_torchinductor_strided_blocks/output.log |
| test_triton_cpu_backend.py | CUDA 专属与其他后端 | 零用例/入口条件 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_triton_cpu_backend/output.log |
| test_triton_extension_backend.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 3 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | followup/collection/test_triton_extension_backend/output.log |
| test_triton_helpers.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 16 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_triton_helpers/output.log |
| test_triton_heuristics.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 53 | 26 | 8 | 19 | 0 | 0 | 0 | 0 | 0 | collection/test_triton_heuristics/output.log |
| test_triton_kernels.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 394 | 5 | 293 | 96 | 0 | 0 | 0 | 0 | 0 | collection/test_triton_kernels/output.log |
| test_triton_launcher_integration.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 6 | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_triton_launcher_integration/output.log |
| test_triton_syntax.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_triton_syntax/output.log |
| test_triton_wrapper.py | Triton 代码生成、模板与启动 | 已执行全部已收集用例 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_triton_wrapper/output.log |
| test_unbacked_symints.py | Inductor 综合、动态形状与 OpInfo | 已执行全部已收集用例 | 55 | 10 | 3 | 42 | 0 | 0 | 0 | 0 | 0 | collection/test_unbacked_symints/output.log |
| test_user_streams.py | Graph、Stream 与设备执行 | 已执行全部已收集用例 | 71 | 13 | 0 | 1 | 57 | 0 | 0 | 0 | 0 | collection/test_user_streams/output.log |
| test_utils.py | 诊断、性能与基础设施 | 已执行全部已收集用例 | 22 | 17 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | collection/test_utils/output.log |
| test_xpu_basic.py | CUDA 专属与其他后端 | 已执行全部已收集用例 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | collection/test_xpu_basic/output.log |
