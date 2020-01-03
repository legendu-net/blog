Status: published
Date: 2020-01-02 17:30:13
Author: Benjamin Du
Slug: tips-on-pytorch
Title: Tips on Pytorch
Category: Programming
Tags: programming, Python, PyTorch, GPU, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## PyTorch on GPU

You can use the command `torch.cuda.is_available()`
to check whether GPU is available for PyTorch.
Details of GPUs can be obtained using the following code.


    :::bash
    In [1]: import torch

    In [2]: torch.cuda.current_device()
    Out[2]: 0

    In [3]: torch.cuda.device(0)
    Out[3]: <torch.cuda.device at 0x7efce0b03be0>

    In [4]: torch.cuda.device_count()
    Out[4]: 1

    In [5]: torch.cuda.get_device_name(0)
    Out[5]: 'GeForce GTX 950M'

    In [6]: torch.cuda.is_available()
    Out[6]: True

## References

https://stackoverflow.com/questions/48152674/how-to-check-if-pytorch-is-using-the-gpu
