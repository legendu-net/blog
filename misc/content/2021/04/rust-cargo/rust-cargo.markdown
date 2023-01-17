Status: published
Date: 2021-04-28 16:21:14
Author: Benjamin Du
Slug: tips-on-cargo
Title: Tips on Cargo
Category: Computer Science
Tags: Computer Science, programming, Rust, cargo, format, fmt, rustfmt
Modified: 2023-01-16 18:50:10

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Create a Project

    cargo init
    cargo new project_name
    cargo new --lib project_name

## Install a Rust Crate (Package) 

Install a Rust crate from GitHub (the default branch).

    :::bash
    cargo install --git https://github com/RustPython/RustPython
    
Specify the option `--version` to install a specific version of a package.

    :::bash
    cargo install --version 0.8.1 evcxr_jupyter

## Update Dependencies

Please refer to
[cargo-update](https://doc.rust-lang.org/cargo/commands/cargo-update.html)
for the official tutorial. 

## Build a Project 

Build the debug version of the project.

    :::bash
    cargo build 

Build the release version of the project.

    :::bash
    cargo build --release

https://doc.rust-lang.org/cargo/commands/cargo-build.html

## Run The Current Package

    cargo run
    cargo run --release

For more details,
please refer to
[cargo-run](https://doc.rust-lang.org/cargo/commands/cargo-run.html) 
.

## Run Unit Tests

Please refer to
[Unit Test in Rust](https://www.legendu.net/misc/blog/unit-test-in-rust)
for more discussions.

## Running Test

[Controlling How Tests Are Run](https://doc.rust-lang.org/book/ch11-02-running-tests.html)

cargo test -- --test-threads=1

cargo test -- --show-output

cargo test -- --ignored

cargo test -- --ignored --show-output

cargo test --release 

cargo test --release -- --ignored

## Suppress Warnings Using RUSTFLAGS

Before cargo officially supports an option to disable warnings,
you can use the environment variable `RUSTFLAGS` to disable warnings during compiling.

    :::bash
    RUSTFLAGS=-Awarnings cargo build
    RUSTFLAGS=-Awarnings cargo build --release
    RUSTFLAGS=-Awarnings cargo test
    RUSTFLAGS=-Awarnings cargo test --release

A better way is to use the command `cargo rustc` 
(instead of `cargo build`)
which allows users to pass compiler flags to it. 

    :::bash
    cargo rustc --lib -- -Awarnings

## Cargo Extensions / Addons 

Please refer to
[Dev Tools for Rust](https://www.legendu.net/misc/blog/dev-tools-for-rust)
for detailed discussions.

## References 

- [Top 10 Rust Cargo Commands](https://dev.to/davidadewoyin/top-rust-cargo-commands-2b70)

- [How can I only show warnings if there are no errors?](https://stackoverflow.com/questions/53355265/how-can-i-only-show-warnings-if-there-are-no-errors)

- [Can tests be built in release mode using Cargo?](https://stackoverflow.com/questions/29818084/can-tests-be-built-in-release-mode-using-cargo)

- [What's the difference between Cargo's build and rustc commands?](https://doc.rust-lang.org/cargo/commands/cargo-build.html)
