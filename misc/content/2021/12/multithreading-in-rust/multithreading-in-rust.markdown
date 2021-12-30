Status: published
Date: 2021-12-24 09:50:50
Modified: 2021-12-25 13:18:04
Author: Benjamin Du
Slug: multithreading-in-rust
Title: Multithreading in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, multi-threading, thread, rayon, parallel

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [rayon](https://crates.io/crates/rayon)

## [crossbeam-channel](https://crates.io/crates/crossbeam-channel)
[crossbeam-channel](https://crates.io/crates/crossbeam-channel)
provides multi-producer multi-consumer channels for message passing. It is an alternative to std::sync::mpsc with more features and better performance.
