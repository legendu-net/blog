Status: published
Date: 2021-04-09 23:34:03
Author: Benjamin Du
Slug: useful-rust-crates
Title: Useful Rust Crates
Category: Computer Science
Tags: Computer Science, programming, Rust, crate, useful
Modified: 2023-01-17 15:45:16
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://crates.io/crates?sort=downloads

## [Summary of Collections in Rust](https://www.legendu.net/misc/blog/summary-of-collections-in-rust) 

## [Dev Tools for Rust](https://www.legendu.net/misc/blog/dev-tools-for-rust)

## [Error Handling in Rust](https://www.legendu.net/misc/blog/error-handling-in-rust)

## [Useful Rust Crates for Testing](https://www.legendu.net/misc/blog/useful-rust-crates-for-testing)

## [Profile Rust Applications](https://www.legendu.net/misc/blog/profile-rust-applications)

## [Implement a Singleton in Rust](https://www.legendu.net/misc/blog/implement-a-singleton-in-rust) 

## [Generating Random Numbers in Rust](https://www.legendu.net/misc/blog/rust-rng) 

## [Useful Rust Crates for Bit Manipulations](https://www.legendu.net/misc/blog/useful-rust-crates-for-bit-manipulations) 

## [Serialization and Deserialization in Rust](https://www.legendu.net/misc/blog/serialization-and-deserialization-in-rust)

## [Design Pattern and Productivity for Rust](https://www.legendu.net/misc/blog/design-pattern-and-productivity-for-rust)

## [Useful Algorithms Implemented in Rust](https://www.legendu.net/misc/blog/useful-algorithms-implemented-in-rust) 

## [Progress Bar in Rust](https://www.legendu.net/misc/blog/progress-bar-in-rust)

## [Rust for Backend Development](https://www.legendu.net/misc/blog/rust-for-backend-development) 

## [Rust for Frontend Development](https://www.legendu.net/misc/blog/rust-for-frontend-development) 

## [Great Command Line Tools Developed in Rust](https://www.legendu.net/misc/blog/great-command-line-tools-developed-in-rust)

## [Rust Crates for RPC](https://www.legendu.net/misc/blog/rust-crates-for-rpc) 

## [Rust for Distributed Applications](https://www.legendu.net/misc/blog/rust-for-distributed-applications)

## [Useful Rust Crates for Filesystem](https://www.legendu.net/misc/blog/useful-rust-crates-for-filesystem) 

## [Compress and Decompress Files in Rust](https://www.legendu.net/misc/blog/compress-and-decompress-files-in-rust)

## [Rust for Game Development](https://www.legendu.net/misc/blog/rust-for-game-development)

## [Foreign Language Integration in Rust](https://www.legendu.net/misc/blog/foreign-language-integration-in-rust)

## [Rust for IoT](https://www.legendu.net/misc/blog/rust-for-iot)

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

### [proc-macro2](https://crates.io/crates/proc-macro2)
[proc-macro2](https://crates.io/crates/proc-macro2)
is a substitute implementation of the compiler's `proc_macro` API 
to decouple token-based libraries from the procedural macro use case.

## References

- [Rust Crates](https://crates.io/)

- [12 Killer Rust Libraries You Should Know](https://jondot.medium.com/12-killer-rust-libraries-you-should-know-c60bab07624f)

- [Awesome Rust](https://github.com/rust-unofficial/awesome-rust)

