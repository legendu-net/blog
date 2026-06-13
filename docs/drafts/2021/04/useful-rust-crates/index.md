---
title: Useful Rust Crates
created: '2021-04-09T23:34:03-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: useful-rust-crates
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - crate
  - useful
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://lib.rs/

https://blessed.rs/crates

https://crates.io/crates?sort=downloads

[Rust日常开发三方库精选](https://course.rs/practice/third-party-libs.html)

## [Summary of Collections in Rust](summary-of-collections-in-rust)

## [Dev Tools for Rust](dev-tools-for-rust)

## [Error Handling in Rust](error-handling-in-rust)

## [Useful Rust Crates for Testing](useful-rust-crates-for-testing)

## [Profile Rust Applications](profile-rust-applications)

## [Implement a Singleton in Rust](implement-a-singleton-in-rust)

## [Generating Random Numbers in Rust](generating-random-numbers-in-rust)

## [Useful Rust Crates for Bit Manipulations](useful-rust-crates-for-bit-manipulations)

## [Serialization and Deserialization in Rust](serialization-and-deserialization-in-rust)

## [Design Pattern and Productivity for Rust](design-pattern-and-productivity-for-rust)

## [Useful Algorithms Implemented in Rust](useful-algorithms-implemented-in-rust)

## [Progress Bar in Rust](progress-bar-in-rust)

## [Rust for Backend Development](rust-for-backend-development)

## [Rust for Frontend Development](rust-for-frontend-development)

## [Parsing Command-line Arguments in Rust](parsing-command-line-arguments-in-rust)

## [Useful Rust Crates for Developing Command Line Apps](useful-rust-crates-for-developing-command-line-apps)

## [Great Command Line Tools Developed in Rust](great-command-line-tools-developed-in-rust)

## [Rust Crates for RPC](rust-crates-for-rpc)

## [Useful Rust Crates for Filesystem](useful-rust-crates-for-filesystem)

## [Compress and Decompress Files in Rust](compress-and-decompress-files-in-rust)

## [Rust for Game Development](rust-for-game-development)

## [Foreign Language Integration in Rust](foreign-language-integration-in-rust)

## [Rust for IoT](rust-for-iot)

## Search Engines

### [tantivy](https://crates.io/crates/tantivy)

[tantivy](https://crates.io/crates/tantivy)
is a full-text search engine library written in Rust.

[Building a distributed search engine with tantivy](https://fosdem.org/2023/schedule/event/rust_building_a_distributed_search_engine_with_tantivy/)

## Memory Management

[stacker](https://crates.io/crates/stacker)
A stack growth library useful
when implementing deeply recursive algorithms
that may accidentally blow the stack.

[serde_stacker](https://crates.io/crates/serde_stacker)
Serde adapter that avoids stack overflow by dynamically growing the stack

### [shared_memory](https://github.com/elast0ny/shared_memory)

[shared_memory](https://github.com/elast0ny/shared_memory)
A crate that allows you to share memory between processes.
This crate provides lightweight wrappers around shared memory APIs in an OS agnostic way.
It is intended to be used with it's sister crate raw_sync
which provide simple primitves to synchronize access to the shared memory (Mutex, RwLock, Events, etc).

### [rust-scudo](https://github.com/google/rust-scudo)

[rust-scudo](https://github.com/google/rust-scudo)
contains the Rust bindings for the Scudo hardened allocator.

## Macros

[Develop Macros in Rust](develop-macros-in-rust)

## Plug-in System

### [extism](https://github.com/extism/extism)

[extism](https://github.com/extism/extism)
is an universal plug-in System
which allows you to extend anything with WebAssembly.

## References

- [Rust Crates](https://crates.io/)

- [12 Killer Rust Libraries You Should Know](https://jondot.medium.com/12-killer-rust-libraries-you-should-know-c60bab07624f)

- [Awesome Rust](https://github.com/rust-unofficial/awesome-rust)
