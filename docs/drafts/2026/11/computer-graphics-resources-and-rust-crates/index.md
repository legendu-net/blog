---
title: Computer Graphics Resources and Rust Crates
created: '2026-11-25T06:55:47.080664-08:00'
date: '2026-11-25T06:55:47-08:00'
authors:
  - bendu
label: computer-graphics-resources-and-rust-crates
license: CC-BY-4.0
tags:
  - programming
  - computer graphics
  - ray tracing
  - Rust
  - 2D graphics
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

This post collects high-signal learning resources for computer graphics—covering physically based ray tracing and 2D vector rasterization—alongside key crates in the Rust graphics ecosystem (see also [](#useful-rust-crates)).

## Books & Tutorials

### Ray Tracing in One Weekend — The Book Series

[Ray Tracing in One Weekend](https://raytracing.github.io/) (written by Peter Shirley, Trevor David Black, and Steve Hollasch, released under CC0) is the standard hands-on introduction to writing a physically based path tracer from scratch. The series consists of three progressive books:

1. **Ray Tracing in One Weekend**: Builds a brute-force path tracer from scratch, covering rays, camera geometry, anti-aliasing, and diffuse, metal, and dielectric (glass) materials.
1. **Ray Tracing: The Next Week**: Adds motion blur, Bounding Volume Hierarchies (BVH) for acceleration, texture mapping, Perlin noise, quads, volumes/fog, and emissive light sources.
1. **Ray Tracing: The Rest of Your Life**: Covers Monte Carlo integration, probability density functions (PDFs), importance sampling, and rendering the Cornell Box accurately.

### `ray-tracing-rs`

[aarestad/ray-tracing-rs](https://github.com/aarestad/ray-tracing-rs) is a Rust implementation following the *Ray Tracing in One Weekend* tutorial series, serving as a practical reference for translating the C++ book code into idiomatic Rust.

## 2D & 3D Graphics Crates in Rust

### `tiny-skia`

[tiny-skia](https://crates.io/crates/tiny-skia) is a small, pure-Rust, CPU-only 2D vector graphics library ported from a subset of Google's Skia engine.

- **Strengths**: High-quality anti-aliased path rendering, strokes, gradients, and blend modes without C++ FFI, OpenGL/Vulkan, or GPU driver dependencies. Supports `no_std` (with `alloc`).
- **API style**: Exposes a low-level API (explicit transforms, clipping masks, and shaders) rather than a stateful high-level canvas, making it ideal as a rendering backend.
- **Ecosystem adoption**: Powers major Rust rendering tools such as `resvg` (SVG rendering) and `typst-render` (Typst typesetting).

### Complementary Rust Graphics Crates

For broader 2D/3D graphics work in Rust, `tiny-skia` pairs well with or is complemented by:

```{list-table} Rust Graphics Crates Overview
---
header-rows: 1
name: rust-graphics-crates-table
widths: 18 22 60
---
* - Crate
  - Domain
  - Best Use Case
* - [tiny-skia](https://crates.io/crates/tiny-skia)
  - CPU 2D vector graphics
  - Headless rendering, SVG/PDF rasterization, and portable 2D drawing without GPU dependencies.
* - [vello](https://crates.io/crates/vello)
  - GPU 2D vector graphics
  - High-throughput, compute-shader-accelerated 2D vector rendering on top of `wgpu`.
* - [wgpu](https://crates.io/crates/wgpu)
  - GPU 3D / compute
  - Cross-platform WebGPU-style 3D rendering and general GPU compute pipelines (Vulkan, Metal, DX12, WebGPU).
* - [image](https://crates.io/crates/image)
  - Raster image I/O
  - Encoding/decoding PNG, JPEG, WebP, etc., and basic pixel buffer manipulation.
```

## References

- [Ray Tracing in One Weekend — The Book Series](https://raytracing.github.io/)
- [aarestad/ray-tracing-rs on GitHub](https://github.com/aarestad/ray-tracing-rs)
- [tiny-skia on crates.io](https://crates.io/crates/tiny-skia)
