import torch
import torch.utils.cpp_extension

print(torch.__version__)
print(torch.version.cuda)

print(torch.backends.cudnn.version())

print(torch.cuda.is_available())

# cuda 目录
print(torch.utils.cpp_extension.CUDA_HOME)