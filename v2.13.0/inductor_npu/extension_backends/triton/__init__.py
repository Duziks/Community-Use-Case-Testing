import torch
import torch_npu
from torch_npu.contrib import transfer_to_npu
from torch_npu.utils import _dynamo
_dynamo.use_jit_script = True
torch.cuda.get_device_capability = lambda :(10, 0)
import torch_npu.testing
import torch_npu._inductor

