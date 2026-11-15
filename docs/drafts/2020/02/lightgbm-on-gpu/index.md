---
title: LightGBM on GPU
created: '2020-02-04T20:49:35-08:00'
date: '2026-11-15T12:20:36-08:00'
authors:
  - bendu
label: lightgbm-on-gpu
license: CC-BY-4.0
tags:
  - AI
  - data science
  - machine learning
  - GPU
  - LightGBM
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://pypi.org/project/lightgbm/#build-gpu-version

https://github.com/microsoft/LightGBM/blob/master/docs/Installation-Guide.rst#build-gpu-version

https://www.kaggle.com/vinhnguyen/gpu-acceleration-for-lightgbm

[Microsoft's Example Dockerfile for GPU version of LightGBM](https://github.com/microsoft/LightGBM/blob/master/docker/gpu/dockerfile.gpu)

[LightGBM GPU Tutorial](https://lightgbm.readthedocs.io/en/latest/GPU-Tutorial.html)

[How I set Windows GPU Environment for tensorflow, lightgbm, xgboost, catboost, etc…](https://harangdev.github.io/tips/1/)

install the below libraries (non GPU) before you install/compile LightGBM

:::bash
apt-get install cmake libboost-dev
pip3 install joblib numpy scipy scikit-learn

## GPU vs CPU Performance

It seems to that GPU have 3 ~ 10 times speed up generally speaking.

https://github.com/Microsoft/LightGBM/blob/master/docs/GPU-Performance.rst
