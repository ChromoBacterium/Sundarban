# Disclaimer
OnnxCV is no longer in development due to personal work. Feel free to fork this repository anytime.

# ONNXCV
Alpha release

# Welcome to ONNXCV
Welcome to OnnxCV! OnnxCV (**O**pen **N**eural **N**etwork E**X**change Runtime for **C**omputer **V**ision) is an inference engine for realtime computer vision, built upon [ONNX Runtime](https://github.com/Microsoft/onnxruntime) and OpenCV.

To learn more about ONNX, go to their Github repo [here](https://github.com/onnx/onnx) or their website [here](https://onnx.ai/).
To learn more about OpenCV, go to their repo [here](https://github.com/opencv/opencv) or their website [here](https://opencv.org/).

# Quickstart
Install ONNXCV by invoking the following command in a terminal or command prompt:
`pip install onnxcv`

Create a new directory and download the [ResNet](https://s3.amazonaws.com/onnx-model-zoo/resnet/resnet18v1/resnet18v1.onnx) model.
Copy and paste the following script in your code:

```python
from  onnxcv import ImageClassifier
clf = ImageClassifier('resnet18v1.onnx')
clf.run()
```
`clf.run()` initiates the device camera to show a visual output. The camera data will then be converted into the model compatible array to allow the model to make predictions. The predictions are arrays that are shown in the terminal.

# To Do:
  - Finish documentation (ETA: 1 day)
