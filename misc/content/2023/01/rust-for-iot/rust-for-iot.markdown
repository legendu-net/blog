Status: published
Date: 2023-01-13 10:42:03
Modified: 2023-01-24 20:14:28
Author: Benjamin Du
Slug: rust-for-iot
Title: Rust for IoT
Category: Computer Science
Tags: Computer Science, programming, Rust, IoT, RTOS, OS, embeded, embed, hardware

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [tock-os](https://github.com/tock/tock)
[tock-os](https://github.com/tock/tock)
Tock is an embedded operating system designed for running multiple concurrent, 
mutually distrustful applications on Cortex-M and RISC-V based embedded platforms. 
Tock's design centers around protection, both from potentially malicious applications and from device drivers.

## [embassy](https://github.com/embassy-rs/embassy)
[embassy](https://github.com/embassy-rs/embassy)
is a modern embedded framework, using Rust and async.

## [cortex-m-rtic](https://github.com/rtic-rs/cortex-m-rtic)
[cortex-m-rtic](https://github.com/rtic-rs/cortex-m-rtic)
Real-Time Interrupt-driven Concurrency (RTIC) framework for ARM Cortex-M microcontrollers.

## [hubris](https://github.com/oxidecomputer/hubris)
[hubris](https://github.com/oxidecomputer/hubris)
is a lightweight, memory-protected, message-passing kernel for deeply embedded systems.

## [FreeRTOS](https://github.com/lobaro/FreeRTOS-rust)
[FreeRTOS](https://github.com/lobaro/FreeRTOS-rust)
is a Rust create to use FreeRTOS in rust projects. 
The freertos-cargo-build crate can be used to build and link FreeRTOS from source inside build.rs.

## [Drone OS](https://www.drone-os.com/)
[Drone OS](https://www.drone-os.com/)
is an Embedded Operating System for writing real-time applications in Rust.

## [R3-OS](https://crates.io/crates/r3)
[R3-OS](https://crates.io/crates/r3)
is an experimental static component-oriented RTOS for deeply embedded systems.

## [Bern RTOS](https://bern-rtos.org/)
[Bern RTOS](https://bern-rtos.org/)
is a real-time operating system for microcontrollers written in Rust
.

## [Using Rust in RIOT](https://doc.riot-os.org/using-rust.html)

[RIOT](https://github.com/RIOT-OS/RIOT)
is a real-time multi-threading operating system (developed in C)
that supports a range of devices 
that are typically found in the Internet of Things (IoT): 8-bit, 16-bit and 32-bit microcontrollers.

On supported CPUs, 
Rust can be used to develop RIOT applications. 
Support is indicated in the has_rust_target feature, 
and tested for in applications using the Makefile line FEATURES_REQUIRED += rust_target.

## Embedded

[Rust Embedded Org @ GitHub](https://github.com/orgs/rust-embedded/repositories)

[PlatformIO](https://platformio.org/)
is a professional collaborative platform for embedded development
.

### [probe-rs](https://github.com/probe-rs/probe-rs)
[probe-rs](https://github.com/probe-rs/probe-rs)
is a debugging toolset and library 
for debugging embedded ARM and RISC-V targets on a separate host
.

### [probe-run](https://github.com/knurling-rs/probe-run)
[probe-run](https://github.com/knurling-rs/probe-run)
is a custom Cargo runner 
that transparently runs Rust firmware on an embedded device.
probe-run is powered by probe-rs 
and thus supports all the devices and probes supported by probe-rs.


[Learning Rust For Embedded Systems](https://www.embeddedrelated.com/showarticle/1432.php)

https://pfesenmeier.github.io/wsl2-and-embedded-development/

https://mabez.dev/blog/posts/esp-rust-18-10-2021/

[Safe & Portable Data Structure Design](https://www.youtube.com/watch?v=1UtklNrB8XA&t=1619s)

[not-yet-awesome-embedded-rust](https://github.com/rust-embedded/not-yet-awesome-embedded-rust)
is a collection of items that are not yet awesome in Embedded Rust
.



## References

- [6 Things I Wish I Knew Starting with Embedded Rust](https://apollolabsblog.hashnode.dev/6-things-i-wish-i-knew-starting-with-embedded-rust)

- [Embedded Rust & Embassy: UART Serial Communication](https://apollolabsblog.hashnode.dev/embedded-rust-embassy-uart-serial-communication)

- [Rust for Robots](https://www.legendu.net/misc/blog/rust-for-robots)
