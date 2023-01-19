Status: published
Date: 2023-01-13 16:51:04
Modified: 2023-01-13 16:51:04
Author: Benjamin Du
Slug: rust-crates-for-parallel-concurrency-and-async
Title: Rust Crates for Parallel Concurrency and Async
Category: Computer Science
Tags: Computer Science, programming, Rust, crate, parallel, concurrency, async, distributed

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## [futures](https://crates.io/crates/futures)
[futures](https://crates.io/crates/futures)
is an implementation of futures and streams featuring zero allocations, 
composability, and iterator-like interfaces.
It is a library providing the foundations for asynchronous programming in Rust. 
It includes key trait definitions like Stream, 
as well as utilities like `join!`, `select!`, 
and various futures combinator methods which enable expressive asynchronous control flow.

## [tokio](https://crates.io/crates/tokio)
[tokio](https://crates.io/crates/tokio)
is an event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications.

## [rayon](https://crates.io/crates/rayon)
[rayon](https://crates.io/crates/rayon)
is a data-parallelism library for Rust. 
It is extremely lightweight and makes it easy to convert a sequential computation into a parallel one. 
It also guarantees data-race freedom.

https://crates.io/crates/bus
A lock-free, bounded, single-producer, multi-consumer, broadcast channel.


## Distributed

https://crates.io/crates/zmq
High-level bindings to the zeromq library


[ockam](https://github.com/ockam-network/ockam)

https://crates.io/crates/riker
Easily build fast, highly concurrent and resilient applications. An Actor Framework for Rust.
