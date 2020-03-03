Status: published
Date: 2020-03-03 11:18:32
Author: Benjamin Du
Slug: common-issues-in-pytorch
Title: Common Issues in PyTorch
Category: AI
Tags: AI, data science, machine learning, deep learning, PyTorch, issue, device

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Input type (torch.FloatTensor) and weight type (torch.cuda.FloatTensor) should be the same

This means that the input data and the model are on different devices (CPU and CUDA). 
Moving them to the same device resolves the issue.

https://discuss.pytorch.org/t/input-type-torch-floattensor-and-weight-type-torch-cuda-floattensor-should-be-the-same/48633

