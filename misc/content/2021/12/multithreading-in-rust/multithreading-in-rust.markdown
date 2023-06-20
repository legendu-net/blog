Status: published
Date: 2021-12-24 09:50:50
Modified: 2023-06-19 18:48:18
Author: Benjamin Du
Slug: rust-concurrency-async-multithreading-parallel
Title: Async, Concurrency, Multithreading and Parallel Computing in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, multi-threading, thread, rayon, parallel

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Basic Struct Types for Rust Concurrency

UnsafeCell: the only foundamental struct which allows interior mutability.
    Other struct (e.g., Cell, RefCell, Rc, Arc, etc.) with interior mutability relies on UnsafeCell.
Rc: reference counting, single thread
Arc: Atomic reference counting, multi-thread
Cell: single thread
    get and set methods for midifying
    does not modify in-place
RefCell: 
    can borrow content with borrow and borrow_mut
    single thread; reference rule checked at runtime; panics if it cannot get the borrow
Atomics: concurrent version of Cell
RwLock: concurrent version of RefCell
    blocks/sleep intead of calling panic if it cannot get the borrow
Mutex: conrrent version of RefCell; simpler than RwLock; only allow exclusive borrows

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

## [deadpool](https://crates.io/crates/deadpool)
[Deadpool](https://crates.io/crates/deadpool)
is a dead simple async pool for connections and objects of any type.

## [mobc](https://crates.io/crates/mobc)
[mobc](https://crates.io/crates/mobc)
is a generic connection pool with async/await support.

## References

- [Basics of Rust Concurrency (Atomics and Locks Chapter 1)](https://www.youtube.com/watch?v=99Qzpv325yI)
