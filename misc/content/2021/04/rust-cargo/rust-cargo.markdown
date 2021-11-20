Status: published
Date: 2021-04-28 16:21:14
Author: Benjamin Du
Slug: tips-on-cargo
Title: Tips on Cargo
Category: Computer Science
Tags: Computer Science, programming, Rust, cargo, format, fmt, rustfmt
Modified: 2021-06-16 18:07:04

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Create a Project

    cargo init
    cargo new project_name

## Install a Rust Crate (Package) 

Install a Rust crate from GitHub (the default branch).

    :::bash
    cargo install --git https://github com/RustPython/RustPython
    
Specify the option `--version` to install a specific version of a package.

    :::bash
    cargo install --version 0.8.1 evcxr_jupyter

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

    cargo test
    cargo test name_of_test_fun
    cargo test test_mod::inner_mod::name_of_test_fun

    cargo test --release 

If building the project with optimization is not too slow, 
it is suggested that your turn on optimization for the test profile 
in your `Cargo.toml` file.

    [profile.test]
    opt-level = 3

https://doc.rust-lang.org/cargo/commands/cargo-test.html

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

## Extensions to Cargo

### Format Code

If `rustfmt` has been installed (using `rustup component add rustfmt`),
you can run the following command to format code in a Rust project.

    cargo fmt 

### [cargo-edit](https://github.com/killercup/cargo-edit)

[cargo-edit](https://github.com/killercup/cargo-edit)
is a utility for managing cargo dependencies from the command line.
It is a temporary solution before the issue
[Add cargo-add (from cargo-edit) to cargo proper](https://github.com/rust-lang/cargo/issues/5586)
is resolved.

    :::bash
    cargo install cargo-edit

### [cargo-crev](https://github.com/crev-dev/cargo-crev)
[cargo-crev](https://github.com/crev-dev/cargo-crev)
is a cryptographically verifiable code review system for the cargo (Rust) package manager.
It is an implementation of Crev as a command line tool integrated with cargo,
which helps Rust users evaluate the quality and trustworthiness of their package dependencies.

### [cargo-audit](https://github.com/RustSec/cargo-audit)
[cargo-audit](https://github.com/RustSec/cargo-audit)
is a Cargo subcommand
which audits Cargo.lock files for crates with security vulnerabilities.
It also supports CICD tools such as GitHub Actions 
(via [audit-check](https://github.com/actions-rs/audit-check))
and Travis CI.



## References 

[How can I only show warnings if there are no errors?](https://stackoverflow.com/questions/53355265/how-can-i-only-show-warnings-if-there-are-no-errors)

[Can tests be built in release mode using Cargo?](https://stackoverflow.com/questions/29818084/can-tests-be-built-in-release-mode-using-cargo)

[What's the difference between Cargo's build and rustc commands?](https://doc.rust-lang.org/cargo/commands/cargo-build.html)
