import onnxruntime

ONNX_DEVICE = onnxruntime.get_device()

# 输出 cpu or gpu
print(ONNX_DEVICE)
print(onnxruntime.__version__)

print(onnxruntime.get_available_providers())
