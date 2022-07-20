Status: published
Date: 2021-12-24 09:50:50
Modified: 2022-07-18 16:53:54
Author: Benjamin Du
Slug: rust-async-multithreading-parallel
Title: Async, Multithreading and Parallel Computing in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, multi-threading, thread, rayon, parallel

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [rayon](https://crates.io/crates/rayon)
Running code in parallel.

## [crossbeam-channel](https://crates.io/crates/crossbeam-channel)
[crossbeam-channel](https://crates.io/crates/crossbeam-channel)
provides multi-producer multi-consumer channels for message passing. 
It is an alternative to std::sync::mpsc with more features and better performance.

## tokio
Tokio is a library for async IO operations.



## [threadpool](https://crates.io/crates/threadpool)
[threadpool](https://crates.io/crates/threadpool)
provides a thread pool for running a number of jobs on a fixed set of worker threads.


## [scheduled-thread-pool](https://crates.io/crates/scheduled-thread-pool)
[scheduled-thread-pool](https://crates.io/crates/scheduled-thread-pool)
provides a thread pool which can schedule execution at a specific delay and repeat it periodically.

