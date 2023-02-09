Status: published
Date: 2023-01-13 15:40:23
Modified: 2023-02-08 11:40:58
Author: Benjamin Du
Slug: useful-rust-crates-for-filesystem
Title: Useful Rust Crates for Filesystem
Category: Computer Science
Tags: Computer Science, programming, Rust, crate, useful, filesystem, fs

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [std::fs](https://doc.rust-lang.org/std/fs/)

## [glob](https://crates.io/crates/glob)
[glob](https://crates.io/crates/glob)
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

- [Compress and Decompress Files in Rust](https://www.legendu.net/misc/blog/compress-and-decompress-files-in-rust)

- [Hands on the Glob Crate in Rust](https://www.legendu.net/misc/blog/hands-on-the-glob-crate-in-rust)
