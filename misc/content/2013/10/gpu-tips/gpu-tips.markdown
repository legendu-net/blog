Status: published
Author: Ben Chuanlong Du
Date: 2013-10-12 11:19:32
Title: Tips on GPU Computing
Slug: gpu-tips
Category: Computer Science
Tags: tips, GPU, programming, Nvidia
Modified: 2023-07-18 00:56:57

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
 
## List GPU Devices on Linux

You can list GPU devices using the following command on linux.

    :::bash
    lspci -v | grep VGA


## Machine Learning Frameworks Supporting Managing GPU Resources

- [Horovod](https://github.com/horovod/horovod)

- [Apache Ray](https://github.com/ray-project/ray)

- [ZeRO + DeepSpeed](https://github.com/microsoft/DeepSpeed)
    is a deep learning optimization library 
    that makes distributed training on GPU clusters easy, efficient, and effective.

## High-level Scientific Libraries with Built-in GPU Support 

- TensorFlow

- PyTorch 

- XGBoost

- LightGBM

- [scikit-cuda](https://github.com/lebedov/scikit-cuda)

- [cudf](https://github.com/rapidsai/cudf)

- Numba


## Low-level Libraries for General Purpose GPU Computing

1. CUDA and Vulkan (successor to OpenCL) are the 2 most popular frameworks for GPU computing.
    CUDA is commerical and for Nvidia GPUs only 
    while Vulkan is opensource and support more brand of GPUs.
    Generally speaking, 
    CUDA has slight better performance than Vulkan on Nvidia GPUs.
    It is suggested that you go with CUDA if you want to squeeze the most out of performance.

### Rust

- [wgpu](https://github.com/gfx-rs/wgpu)
[wgpu](https://github.com/gfx-rs/wgpu)
is a cross-platform, safe, pure-rust graphics api. 
It runs natively on Vulkan, Metal, D3D12, D3D11, and OpenGLES; 
and on top of WebGPU on wasm.

- [ash](https://github.com/MaikKlein/ash/)
[ash](https://github.com/MaikKlein/ash/)
is a very lightweight wrapper around Vulkan.

- [rust-gpu](https://github.com/EmbarkStudios/rust-gpu)
    [rust-gpu](https://github.com/EmbarkStudios/rust-gpu)
    aims at making Rust a first-class language and ecosystem for GPU shaders.

- [vulkano](https://github.com/vulkano-rs/vulkano)
[Vulkano](https://github.com/vulkano-rs/vulkano)
is a Rust wrapper around the Vulkan graphics API. 
It follows the Rust philosophy, 
which is that as long as you don't use unsafe code you shouldn't be able to trigger any undefined behavior. 
In the case of Vulkan, this means that non-unsafe code should always conform to valid API usage.
[Vulkano](https://github.com/vulkano-rs/vulkano)
is not as mature as
[ash](https://github.com/MaikKlein/ash/)
.

https://github.com/zakarumych/gpu-alloc

https://github.com/zakarumych/gpu-descriptor
Backend agnostic descriptor allocator for Vulkan-like APIs

- [ArrayFire-rust](https://github.com/arrayfire/arrayfire-rust)


## [pathfinder](https://github.com/servo/pathfinder)
[pathfinder](https://github.com/servo/pathfinder)
is a fast, practical, GPU-based rasterizer for fonts and vector graphics 
using OpenGL 3.0+, OpenGL ES 3.0+, WebGL 2, and Metal.

### GPU Computing in Python

Please refer to 
[GPU Computing in Python](http://www.legendu.net/misc/gpu-computing-in-python)
for more details.

https://weeraman.com/put-that-gpu-to-good-use-with-python-e5a437168c01

https://docs.anaconda.com/anaconda/user-guide/tasks/gpu-packages/

https://towardsdatascience.com/python-performance-and-gpus-1be860ffd58d

https://developer.nvidia.com/how-to-cuda-python

https://devblogs.nvidia.com/numba-python-cuda-acceleration/

https://github.com/harrism/numba_examples/blob/master/mandelbrot_numba.ipynb

- [wgpu-py](https://github.com/pygfx/wgpu-py)
[wgpu-py](https://github.com/pygfx/wgpu-py)
is a next generation GPU API for Python.
It is a Python lib wrapping wgpu-native and exposing it with a Pythonic API similar to the WebGPU spec.

- [vulkan-kompute](https://github.com/EthicalML/vulkan-kompute)
General purpose GPU compute framework for cross vendor graphics cards 
(AMD, Qualcomm, NVIDIA & friends). 
Blazing fast, mobile-enabled, asynchronous and optimized for advanced GPU data processing usecases.

https://gabdube.github.io/python/vulkan/2019/01/10/python-and-vulkan-01.html

[Beyond CUDA: GPU Accelerated Python for Machine Learning on Cross-Vendor Graphics Cards Made Simple](https://towardsdatascience.com/beyond-cuda-gpu-accelerated-python-for-machine-learning-in-cross-vendor-graphics-cards-made-simple-6cc828a45cc3)


### C++ 

- [Thrust](https://developer.nvidia.com/thrust)

    Thrust is a parallel algorithms library which resembles the C++ Standard Template Library (STL). 
    Thrust is high-level interface greatly enhances programmer productivity 
    while enabling performance portability between GPUs and multicore CPUs. 
    Interoperability with established technologies (such as CUDA, TBB, and OpenMP) facilitates integration with existing software. 

- [ArrayFire](https://github.com/arrayfire/arrayfire)



### Java

- [aparapi](https://github.com/Syncleus/aparapi)

- [jcuda](https://github.com/jcuda/jcuda)

    Java bindings for CUDA.

## Graphics Rendering

OpenGL
https://github.com/mcfletch/pyopengl

PyOpenGL

GLFW
https://github.com/glfw/glfw
GLFW is an Open Source, multi-platform library for OpenGL, OpenGL ES and Vulkan application development. It provides a simple, platform-independent API for creating windows, contexts and surfaces, reading input, handling events, etc.

[vulkano](https://github.com/vulkano-rs/vulkano)







## External Graphics Card

https://www.pcworld.com/article/2984716/how-to-transform-your-laptop-into-a-gaming-powerhouse-with-an-external-graphics-card.html

https://www.laptopmag.com/articles/best-egpus


## References

- [CUDA Installation Guide for Microsoft Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)

- [Comparative performance analysis ofVulkan and CUDA programming modelimplementations for GPUs](https://core.ac.uk/reader/323473500)

- [Nvidia CUDA Linux Repositories](https://developer.download.nvidia.com/compute/cuda/repos/)

- [A Comparison of Modern Graphics APIs](https://alain.xyz/blog/comparison-of-modern-graphics-apis) 

- https://bheisler.github.io/post/state-of-gpgpu-in-rust/

- https://towardsdatascience.com/python-performance-and-gpus-1be860ffd58d

- https://towardsdatascience.com/speed-up-your-algorithms-part-1-pytorch-56d8a4ae7051

- https://towardsdatascience.com/speed-up-your-algorithms-part-2-numba-293e554c5cc1

- https://towardsdatascience.com/speed-up-your-algorithms-part-3-parallelization-4d95c0888748

- https://towardsdatascience.com/speeding-up-your-algorithms-part-4-dask-7c6ed79994ef

- https://github.com/PuneetGrov3r/MediumPosts/blob/master/SpeedUpYourAlgorithms/1)%20PyTorch.ipynb

- https://github.com/PuneetGrov3r/MediumPosts/blob/master/SpeedUpYourAlgorithms/2)%20Numba.ipynb

- https://github.com/PuneetGrov3r/MediumPosts/blob/master/SpeedUpYourAlgorithms/3)%20Prallelization.ipynb

- https://github.com/PuneetGrov3r/MediumPosts/blob/master/SpeedUpYourAlgorithms/4)%20Dask.ipynb

- https://github.com/harrism/numba_examples/blob/master/mandelbrot_numba.ipynb

