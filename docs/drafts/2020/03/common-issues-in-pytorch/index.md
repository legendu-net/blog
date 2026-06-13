---
title: Common Issues in PyTorch
created: '2020-03-03T11:41:04-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: common-issues-in-pytorch
license: CC-BY-4.0
tags:
  - AI
  - data science
  - machine learning
  - deep learning
  - PyTorch
  - issue
  - device
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [GPU Related Issues and Solutions](gpu-related-issues-and-solutions)

## Input type (torch.FloatTensor) and weight type (torch.cuda.FloatTensor) should be the same

This means that the input data and the model are on different devices (CPU and CUDA).
Moving them to the same device resolves the issue.
Please refer to
[Move a Tensor to a Specific Device in PyTorch](common-issues-in-pytorch)
on how to move a Tensor to a specific device.

https://discuss.pytorch.org/t/input-type-torch-floattensor-and-weight-type-torch-cuda-floattensor-should-be-the-same/48633

## [Error: Expected more than 1 value per channel when training](https://discuss.pytorch.org/t/error-expected-more-than-1-value-per-channel-when-training/26274)
