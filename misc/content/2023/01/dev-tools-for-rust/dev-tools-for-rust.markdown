Status: published
Date: 2023-01-13 16:02:14
Modified: 2023-01-19 20:21:24
Author: Benjamin Du
Slug: dev-tools-for-rust
Title: Dev Tools for Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, dev, development, develop, tool, cargo

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://crates.io/crates/cargo-careful
Execute Rust code carefully, with extra checking along the way

### [cargo-semver-checks](https://crates.io/crates/cargo-semver-checks)
[cargo-semver-checks](https://crates.io/crates/cargo-semver-checks)
scans your Rust crate for semver violations.

### [cargo-udeps](https://github.com/est31/cargo-udeps)
[cargo-udeps](https://github.com/est31/cargo-udeps)
finds unused dependencies in Cargo.toml.

### [marker](https://github.com/rust-marker/marker)
[marker](https://github.com/rust-marker/marker)
is a stable linting interface for Rust. Let's make custom lints a reality.

https://crates.io/crates/vergen
Generate build, git, rustc, cargo, and sysinfo related cargo:rustc-env instructions via build.rs 
for use in your code via the env! macro or option_env! macro.

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

### [app-template](https://github.com/knurling-rs/app-template)
[app-template](https://github.com/knurling-rs/app-template)
quickly sets up a `probe-run` + `defmt` + `flip-link` embedded project
.


