Status: published
Date: 2021-04-28 16:21:14
Author: Benjamin Du
Slug: tips-on-cargo
Title: Tips on Cargo
Category: Computer Science
Tags: Computer Science, programming, Rust, cargo, format, fmt, rustfmt
Modified: 2023-01-11 12:16:36

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

### [rustfmt](https://github.com/rust-lang/rustfmt) - Format Code
[rustfmt](https://github.com/rust-lang/rustfmt)
is Rust's code (official) formatting tool.
If `rustfmt` has been installed (using `rustup component add rustfmt`),
you can run the following command to format code in a Rust project.

    cargo fmt 

Notice that `cargo fmt` might have issues with Rust code 
that are nested in many layers
and there's no good configuration to make it work.
It is suggested that you do not nest Rust code too deeply. 
This not only make things easier for `cargo fmt`
but also makes your Rust code cleaner and more readable.

### [rust-clippy](https://github.com/rust-lang/rust-clippy)
[rust-clippy](https://github.com/rust-lang/rust-clippy)
is a bunch of lints to catch common mistakes and improve your Rust code.

### [cargo-nextest](https://github.com/nextest-rs/nextest)

[cargo-nextest](https://github.com/nextest-rs/nextest)
is a next-generation test runner for Rust.

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

### [cargo-generate](https://github.com/cargo-generate/cargo-generate)
[cargo-generate](https://github.com/cargo-generate/cargo-generate)
is a developer tool to help you get up and running quickly with a new Rust project 
by leveraging a pre-existing git repository as a template.


### [cargo-shuttle](https://github.com/shuttle-hq/shuttle)
[Shuttle] (https://www.shuttle.rs/)
is a Rust-native cloud development platform that lets you deploy your Rust apps for free.


### [cargo-careful](https://github.com/RalfJung/cargo-careful)
[cargo-careful](https://github.com/RalfJung/cargo-careful)
is a tool to run your Rust code extra carefully 
-- opting into a bunch of nightly-only extra checks that help detect Undefined Behavior, 
and using a standard library with debug assertions.

### [cargo-pgo](https://github.com/Kobzol/cargo-pgo)

Cargo subcommand for optimizing binaries with PGO and BOLT.

### [cargo-hack](https://github.com/taiki-e/cargo-hack)
Cargo subcommand to provide various options useful for testing and continuous integration.

### [cargo-watch](https://github.com/watchexec/cargo-watch)
Cargo Watch watches over your project's source for changes, 
and runs Cargo commands when they occur.

### [dylint](https://github.com/trailofbits/dylint)
Dylint is a Rust linting tool, similar to Clippy. 
But whereas Clippy runs a predetermined, static set of lints, 
Dylint runs lints from user-specified, dynamic libraries. 
Thus, Dylint allows developers to maintain their own personal lint collections.

## References 

- [Top 10 Rust Cargo Commands](https://dev.to/davidadewoyin/top-rust-cargo-commands-2b70)

- [How can I only show warnings if there are no errors?](https://stackoverflow.com/questions/53355265/how-can-i-only-show-warnings-if-there-are-no-errors)

- [Can tests be built in release mode using Cargo?](https://stackoverflow.com/questions/29818084/can-tests-be-built-in-release-mode-using-cargo)

- [What's the difference between Cargo's build and rustc commands?](https://doc.rust-lang.org/cargo/commands/cargo-build.html)
