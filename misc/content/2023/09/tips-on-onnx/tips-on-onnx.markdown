Status: published
Date: 2023-09-07 15:11:23
Modified: 2023-09-13 23:01:01
Author: Benjamin Du
Slug: tips-on-onnx
Title: Tips on ONNX
Category: Computer Science
Tags: Computer Science, programming, ONNX, tract, AI, deep learning, machine learning

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [ONNX Runtime](https://github.com/microsoft/onnxruntime)
[ONNX Runtime](https://github.com/microsoft/onnxruntime)
is a cross-platform inference and training machine-learning accelerator.
ONNX Runtime inference can enable faster customer experiences and lower costs, supporting models from deep learning frameworks such as PyTorch and TensorFlow/Keras as well as classical machine learning libraries such as scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime is compatible with different hardware, drivers, and operating systems, and provides optimal performance by leveraging hardware accelerators where applicable alongside graph optimizations and transforms.

## [tract](https://github.com/sonos/tract)
[tract](https://github.com/sonos/tract)
is a Neural Network inference toolkit. It can read ONNX or NNEF, optimize them and run them.

