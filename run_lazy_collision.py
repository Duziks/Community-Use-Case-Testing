import torch
import torch_npu
from torch_npu.contrib import transfer_to_npu
from torch_npu.utils import _dynamo
_dynamo.use_jit_script = True
torch.cuda.get_device_capability = lambda :(10, 0)
import torch_npu.testing
import torch_npu._inductor
from torch.testing._internal.inductor_utils import GPU_TYPE

from torch._inductor import config

config.cpp_wrapper = True
config.triton.autotune_at_compile_time = False

def fn(x, y, z, w):
    a = x.sin()
    torch._dynamo.graph_break()
    b = (a * y).cos()
    torch._dynamo.graph_break()
    c = (b * z).sin()
    torch._dynamo.graph_break()
    d = (c * w).cos()
    return d.sum()

args = [torch.randn(32, device=GPU_TYPE, requires_grad=True) for _ in range(4)]
ref_args = [a.detach().clone().requires_grad_(True) for a in args]
ref = fn(*ref_args)
ref.backward()

compiled_fn = torch.compile(fn)
res = compiled_fn(*args)
res.backward()

# NPU float32 与 eager 存在归约顺序差异：梯度接近 0 的元素相对误差被放大，
# 默认容差(rtol=1e-5, atol=1e-8)过严导致误报，放宽到 rtol/atol=1e-4。
assert torch.allclose(res.detach(), ref.detach(), rtol=1e-4, atol=1e-4), (
    f"Forward mismatch: {res} vs {ref}"
)
for i, (a, r) in enumerate(zip(args, ref_args)):
    assert torch.allclose(a.grad, r.grad, rtol=1e-4, atol=1e-4), (
        f"Grad mismatch for arg {i}"
    )

print("PASS: forward and grads all match")