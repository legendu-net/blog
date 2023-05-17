Status: published
Date: 2023-01-13 16:20:03
Modified: 2023-05-15 22:31:28
Author: Benjamin Du
Slug: foreign-language-integration-in-rust
Title: Foreign Language Integration in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, foreign, language, integration, ffi, cc, gcc, make, cmake, ABI

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**




## [cc](https://crates.io/crates/cc)
[cc](https://crates.io/crates/cc)
is a build-time dependency for Cargo build scripts 
to assist in invoking the native C compiler 
to compile native C code into a static archive to be linked into Rust code.

## [cmake](https://crates.io/crates/cmake)
[cmake](https://crates.io/crates/cmake)
is a build dependency for running `cmake` to build a native library.

## [libc](https://crates.io/crates/libc)
[libc](https://crates.io/crates/libc)
Raw FFI bindings to platform libraries like libc.
[libc](https://crates.io/crates/libc)
provides all of the definitions necessary 
to easily interoperate with C code (or "C-like" code) 
on each of the platforms that Rust supports. 
This includes type definitions (e.g. c_int), constants (e.g. EINVAL) as well as function headers (e.g. malloc).

## [C2Rust](https://github.com/immunant/c2rust)
[C2Rust](https://github.com/immunant/c2rust)
helps you migrate C99-compliant code to Rust. 
The translator (or transpiler), c2rust transpile, 
produces unsafe Rust code that closely mirrors the input C code. 
The primary goal of the translator is to preserve functionality; 
test suites should continue to pass after translation.

## [typeshare](https://github.com/1Password/typeshare)
[Typeshare](https://github.com/1Password/typeshare)
is the ultimate tool for synchronizing your type definitions 
between Rust and other languages for seamless FFI.

## [rust-bindgen](https://github.com/rust-lang/rust-bindgen)
[rust-bindgen](https://github.com/rust-lang/rust-bindgen)
automatically generates Rust FFI bindings to C (and some C++) libraries.

## [ritual](https://github.com/rust-qt/ritual)
[Ritual](https://github.com/rust-qt/ritual)
allows to use C++ libraries from Rust. 
It analyzes the C++ API of a library and generates a fully-featured crate 
that provides convenient (but still unsafe) access to this API.

## [rust-cpp](https://github.com/mystor/rust-cpp)
[rust-cpp](https://github.com/mystor/rust-cpp)
is a build tool & macro which enables you to write C++ code inline in your rust code.

## [crubit](https://github.com/google/crubit)
[crubit](https://github.com/google/crubit)
is a C++/Rust bidirectional interop tool.

## [autocxx](https://github.com/google/autocxx)
[autocxx](https://github.com/google/autocxx)
is a tool for calling C++ from Rust in a heavily automated, but safe, fashion.

## [inline-python](https://github.com/fusion-engineering/inline-python)
[inline-python](https://github.com/fusion-engineering/inline-python)
inlines Python code directly in your Rust code.

## [rust-cpython](https://github.com/dgrunwald/rust-cpython)

## [libloading](https://crates.io/crates/libloading)
[libloading](https://crates.io/crates/libloading)
provides bindings around the platform's dynamic library 
loading primitives with greatly improved memory safety.

## References 

- [Foreign Function Interface](https://doc.rust-lang.org/nomicon/ffi.html)

- [How to call a C++ dynamic library from Rust?](https://stackoverflow.com/questions/52923460/how-to-call-a-c-dynamic-library-from-rust)

- [Calling Rust from Python](https://www.legendu.net/misc/blog/calling-rust-from-python) 

- [Calling Rust from Java](https://www.legendu.net/misc/blog/calling-rust-from-java)

- [Rustdef Makes It Dead Simple to Call Rust in Python Notebook](https://www.legendu.net/misc/blog/rustdef-makes-it-dead-simple-to-call-rust-in-python-notebook)   

