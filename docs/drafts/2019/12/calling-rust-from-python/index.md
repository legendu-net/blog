---
title: Calling Rust from Python
created: '2019-12-28T11:37:35-08:00'
date: '2026-11-15T12:20:36-08:00'
authors:
  - bendu
label: calling-rust-from-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - Rust
  - PyO3
  - maturin
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tools

[pyo3](https://github.com/PyO3/pyo3)

Rust bindings for Python, including tools for creating native Python extension modules.
Running and interacting with Python code from a Rust binary is also supported.

[maturin](https://github.com/PyO3/maturin)

Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries
as python packages.

## A Single Library for Rust and Python

[A single library crate for Rust and Python](https://github.com/PyO3/pyo3/discussions/2271)

[Wrap Rust Library for Python (without changing Rust library)](https://users.rust-lang.org/t/wrap-rust-library-for-python-without-changing-rust-library/69285)

## Calling Python from Rust

- [Calling Rust from Python using PyO3](https://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-python-using-pyo3/)

- [inline-python](https://github.com/fusion-engineering/inline-python)

## References

- [Calling Rust code from Python](https://www.youtube.com/watch?v=DpUlfWP_gtg)
