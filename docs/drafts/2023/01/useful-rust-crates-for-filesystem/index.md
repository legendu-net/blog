---
title: Useful Rust Crates for Filesystem
created: '2023-01-13T15:40:23-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: useful-rust-crates-for-filesystem
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - crate
  - useful
  - filesystem
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [std::fs](https://doc.rust-lang.org/std/fs/)

## [camino](https://crates.io/crates/camino)

[Camino](https://crates.io/crates/camino)
is an extension of the std::path module that adds new Utf8PathBuf and Utf8Path types.

## [glob](hands-on-the-glob-crate-in-rust)

[glob](hands-on-the-glob-crate-in-rust)
supports matching file paths against Unix shell style patterns.

## [jwalk](https://crates.io/crates/jwalk)

[jwalk](https://crates.io/crates/jwalk)
performs filesystem walk in parallel with streamed and sorted results.

## [trash-rs](https://github.com/Byron/trash-rs)

[trash-rs](https://github.com/Byron/trash-rs)
is a Rust library for moving files to the Recycle Bin

## [open](https://crates.io/crates/open)

[open](https://crates.io/crates/open)
opens a path or URL using the program configured on the system.

## [notify](https://crates.io/crates/notify)

[notify](https://crates.io/crates/notify)
is a cross-platform filesystem notification library
.

## [walkdir](https://crates.io/crates/walkdir)

[walkdir](https://crates.io/crates/walkdir)
is a cross platform Rust library for efficiently walking a directory recursively.
Comes with support for following symbolic links,
controlling the number of open file descriptors and efficient mechanisms for pruning the entries in the directory tree.

## References

- [Compress and Decompress Files in Rust](compress-and-decompress-files-in-rust)

- [Hands on the Glob Crate in Rust](hands-on-the-glob-crate-in-rust)
