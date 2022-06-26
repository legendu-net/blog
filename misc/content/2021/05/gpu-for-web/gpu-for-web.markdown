Status: published
Date: 2021-05-12 09:26:51
Author: Benjamin Du
Slug: gpu-for-web
Title: GPU for Web
Category: Computer Science
Tags: Computer Science, programming, GPU, Web, gpuweb, wgpu
Modified: 2021-06-17 17:04:56
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


https://github.com/gpuweb/gpuweb
This is the repository for the W3C's GPU for the Web Community Group.


## [gfx-rs](https://github.com/gfx-rs/gfx)
[gfx-rs](https://github.com/gfx-rs/gfx)
is a low-level, cross-platform graphics and compute abstraction library in Rust. 
[gfx-rs](https://github.com/gfx-rs/gfx)
is hard to use. 
It's recommended for performance-sensitive libraries and engines. 
wgpu-rs is a safe and simple alternative.

## [wgpu](https://github.com/gfx-rs/wgpu)
[wgpu](https://github.com/gfx-rs/wgpu)
is an implementation of WebGPU API in Rust, 
targeting both native and the Web. 
See the upstream WebGPU specification (work in progress).

## [wgpu-py](https://github.com/pygfx/wgpu-py)
[wgpu-py](https://github.com/pygfx/wgpu-py)
is a next generation GPU API for Python.
It is a Python lib wrapping wgpu-native and exposing it with a Pythonic API similar to the WebGPU spec.

## References 

[Point of WebGPU on native](http://kvark.github.io/web/gpu/native/2020/05/03/point-of-webgpu-native.html)
