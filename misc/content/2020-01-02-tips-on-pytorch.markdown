Status: published
Date: 2020-01-06 00:55:36
Author: Benjamin Du
Slug: tips-on-pytorch
Title: Tips on PyTorch
Category: Programming
Tags: programming, Python, PyTorch, GPU, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.

## PyTorch Tutorials

https://pytorch.org/tutorials/beginner/pytorch_with_examples.html
**

## PyTorch on GPU

https://pytorch.org/docs/master/notes/cuda.html

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

You can force synchronous computation by setting environment variable CUDA_LAUNCH_BLOCKING=1. 
This can be handy when an error occurs on the GPU. 
(With asynchronous execution, such an error isn’t reported until after the operation is actually executed, 
so the stack trace does not show where it was requested.)

## Make Sure that PyTorch is Using GPU

https://discuss.pytorch.org/t/solved-make-sure-that-pytorch-using-gpu-to-compute/4870

## Configuration

cudnn.benchmark = true -- uses the inbuilt cudnn auto-tuner to find the fastest convolution algorithms.
                       -- If this is set to false, uses some in-built heuristics that might not always be fastest.

Regarding cudnn.fastest, 
I think it’s because by default it also tries not to use very much memory, 
but when you enable fastest, 
it doesn’t care.

See https://github.com/soumith/cudnn.torch/blob/master/SpatialConvolution.lua#L167-L174

regarding cudnn.benchmark, 
if you have variable length sequences given as inputs, 
benchmark will try to auto-tune for every new input shape, 
and that will result in a huge slowdown.

https://pytorch.org/docs/master/notes/cuda.html#device-agnostic-code
This is the suggested way to control tensors on CPU/GPU. 

## Use PyTorch Models in Production

https://medium.com/datadriveninvestor/deploy-your-pytorch-model-to-production-f69460192217

https://pytorch.org/tutorials/advanced/super_resolution_with_caffe2.html

## Questions

> There are significant caveats to using CUDA models with multiprocessing; 
> unless care is taken to meet the data handling requirements exactly, 
> it is likely that your program will have incorrect or undefined behavior.

Apache Ray is essentially multiprocessing, right? 
How does Apache Ray work with PyTorch?


## References

https://stackoverflow.com/questions/48152674/how-to-check-if-pytorch-is-using-the-gpu

https://medium.com/ai%C2%B3-theory-practice-business/use-gpu-in-your-pytorch-code-676a67faed09

https://groups.google.com/forum/#!topic/torch7/CkB57025yRY
