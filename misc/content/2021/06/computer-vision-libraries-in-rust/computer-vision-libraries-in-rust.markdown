Status: published
Date: 2021-06-25 16:02:10
Modified: 2021-09-20 00:00:35
Author: Benjamin Du
Slug: computer-vision-libraries-in-rust
Title: Computer Vision Libraries in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, CV, computer vision, image, video
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [resize](https://github.com/PistonDevelopers/resize)
[resize](https://github.com/PistonDevelopers/resize)
Image resampling library in pure Rust.
- Fast, with support for many pixel formats
- No encoders/decoders, meant to be used with some external library
- Tuned for resizing to the same dimensions multiple times: uses preallocated buffers and matrixes

## [image](https://github.com/image-rs/image)
[image](https://github.com/image-rs/image)
is a Rust library for encoding and decoding images.

## [gstreamer](https://crates.io/crates/gstreamer)
[gstreamer](https://crates.io/crates/gstreamer)
provides safe bindings for Rust.

## [opencv-rust](https://github.com/twistedfall/opencv-rust)
[opencv-rust](https://github.com/twistedfall/opencv-rust)
Experimental Rust bindings for OpenCV 3 and 4.

v4l
https://github.com/raymanfx/libv4l-rs

nalgebra
https://github.com/dimforge/nalgebra

img_hash
https://crates.io/crates/img_hash

imageproc
https://crates.io/crates/imageproc
An image processing library, based on the image library.

https://crates.io/crates/eye
Eye is a cross platform camera capture and control library written in native Rust. 
It features multiple platform backends, 
such as v4l2 for Linux.

https://github.com/rust-cv
