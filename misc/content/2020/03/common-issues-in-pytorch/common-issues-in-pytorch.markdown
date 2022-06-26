Status: published
Date: 2020-03-03 11:41:04
Author: Benjamin Du
Slug: common-issues-in-pytorch
Title: Common Issues in PyTorch
Category: AI
Tags: AI, data science, machine learning, deep learning, PyTorch, issue, device
Modified: 2021-09-16 20:58:50

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## [GPU Related Issues and Solutions](http://www.legendu.net/misc/blog/GPU-related-issues-and-solutions)

## Input type (torch.FloatTensor) and weight type (torch.cuda.FloatTensor) should be the same

This means that the input data and the model are on different devices (CPU and CUDA). 
Moving them to the same device resolves the issue.
Please refer to 
[Move a Tensor to a Specific Device in PyTorch](http://www.legendu.net/misc/blog/common-issues-in-pytorch/)
on how to move a Tensor to a specific device.

https://discuss.pytorch.org/t/input-type-torch-floattensor-and-weight-type-torch-cuda-floattensor-should-be-the-same/48633

## [Error: Expected more than 1 value per channel when training](https://discuss.pytorch.org/t/error-expected-more-than-1-value-per-channel-when-training/26274)
