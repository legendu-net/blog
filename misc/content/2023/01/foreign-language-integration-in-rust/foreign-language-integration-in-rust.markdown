Status: published
Date: 2023-01-13 16:20:03
Modified: 2023-01-13 16:20:03
Author: Benjamin Du
Slug: foreign-language-integration-in-rust
Title: Foreign Language Integration in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, foreign, language, integration, ffi, cc, gcc, make, cmake

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**




https://crates.io/crates/cc
A build-time dependency for Cargo build scripts to assist in invoking the native C compiler to compile native C code into a static archive to be linked into Rust code.

https://crates.io/crates/cmake
A build dependency for running `cmake` to build a native library

[  Calling Rust from Python  ](https://www.legendu.net/misc/blog/calling-rust-from-python) 

[  Calling Rust from Java  ](https://www.legendu.net/misc/blog/calling-rust-from-java)

[  Rustdef Makes It Dead Simple to Call Rust in Python Notebook  ](https://www.legendu.net/misc/blog/rustdef-makes-it-dead-simple-to-call-rust-in-python-notebook)   


## Rust Crates for Foreign Language Interfaces

### [libc](https://crates.io/crates/libc)
[libc](https://crates.io/crates/libc)
Raw FFI bindings to platform libraries like libc.
[libc](https://crates.io/crates/libc)
provides all of the definitions necessary 
to easily interoperate with C code (or "C-like" code) 
on each of the platforms that Rust supports. 
This includes type definitions (e.g. c_int), constants (e.g. EINVAL) as well as function headers (e.g. malloc).

### [rust-bindgen](https://github.com/rust-lang/rust-bindgen)
[rust-bindgen](https://github.com/rust-lang/rust-bindgen)
automatically generates Rust FFI bindings to C (and some C++) libraries.

### [ritual](https://github.com/rust-qt/ritual)
[Ritual](https://github.com/rust-qt/ritual)
allows to use C++ libraries from Rust. 
It analyzes the C++ API of a library and generates a fully-featured crate 
that provides convenient (but still unsafe) access to this API.

### [rust-cpp](https://github.com/mystor/rust-cpp)
[rust-cpp](https://github.com/mystor/rust-cpp)
is a build tool & macro which enables you to write C++ code inline in your rust code.

### [inline-python](https://github.com/fusion-engineering/inline-python)
[inline-python](https://github.com/fusion-engineering/inline-python)
inlines Python code directly in your Rust code.

### [rust-cpython](https://github.com/dgrunwald/rust-cpython)

## References 

- [Foreign Function Interface](https://doc.rust-lang.org/nomicon/ffi.html)
- [How to call a C++ dynamic library from Rust?](https://stackoverflow.com/questions/52923460/how-to-call-a-c-dynamic-library-from-rust)