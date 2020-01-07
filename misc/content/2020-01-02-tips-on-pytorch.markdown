Status: published
Date: 2020-01-07 10:29:59
Author: Benjamin Du
Slug: tips-on-pytorch
Title: Tips on PyTorch
Category: Programming
Tags: programming, Python, PyTorch, GPU, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## PyTorch Tutorials

https://pytorch.org/tutorials/beginner/pytorch_with_examples.html

torch.Sequential is an easy and quick way to construct simple neural netowrks.
For more complicated neural network architextures, 
you'd better implement your own class extending torch.nn.Module.

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

2. shall we every use `inplace=True` when manipulating Layers in PyTorch?

## PyTorch Ecosystem

torchvision: Popular deep learning models for computer vision.

torchtext: Data loaders and abstractions for text and NLP.

torchaudio: Data manipulation and transformation for audio signal processing, powered by PyTorch.

[PyTorch Hub](https://pytorch.org/hub/) has pretrained deep learning models 
that anyone can download.


## References

https://stackoverflow.com/questions/48152674/how-to-check-if-pytorch-is-using-the-gpu

https://medium.com/ai%C2%B3-theory-practice-business/use-gpu-in-your-pytorch-code-676a67faed09

https://groups.google.com/forum/#!topic/torch7/CkB57025yRY
