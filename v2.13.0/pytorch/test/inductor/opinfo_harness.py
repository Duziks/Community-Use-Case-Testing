import torch
import torch_npu
from torch_npu.contrib import transfer_to_npu
from torch_npu.utils import _dynamo
_dynamo.use_jit_script = True
torch.cuda.get_device_capability = lambda :(10, 0)
import torch_npu.testing
import torch_npu._inductor

import os
import subprocess

from torch.testing._internal.common_methods_invocations import op_db


if __name__ == "__main__":
    i = 0
    while i < len(op_db):
        start = i
        end = i + 20
        os.environ["PYTORCH_TEST_RANGE_START"] = f"{start}"
        os.environ["PYTORCH_TEST_RANGE_END"] = f"{end}"
        popen = subprocess.Popen(
            ["pytest", "test/inductor/test_torchinductor_opinfo.py"],
            stdout=subprocess.PIPE,
        )
        for line in popen.stdout:
            print(line.decode(), end="")
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(
                return_code, ["pytest", "test/inductor/test_torchinductor_opinfo.py"]
            )
        i = end + 1
