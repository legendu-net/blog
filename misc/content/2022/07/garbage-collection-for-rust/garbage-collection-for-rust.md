Status: published
Date: 2022-07-11 16:57:55
Modified: 2023-08-29 14:22:08
Author: Benjamin Du
Slug: garbage-collection-memory-management-for-rust
Title: Garbage Collection for Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, concurrent, data structure, epoch, GC, garbage collection

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## [crossbeam-epoch](https://crates.io/crates/crossbeam-epoch)
The 

[crossbeam-epoch](https://crates.io/crates/crossbeam-epoch)
crate 
provides epoch-based garbage collection for building concurrent data structures.

## [bumpalo](https://crates.io/crates/bumpalo)
[bumpalo](https://crates.io/crates/bumpalo)
is a fast bump allocation arena for Rust.
Bump allocation is a fast, but limited approach to allocation. We have a chunk of memory, and we maintain a pointer within that memory. Whenever we allocate an object, we do a quick check that we have enough capacity left in our chunk to allocate the object and then update the pointer by the object's size. That's it!

## [sharded-slab](https://crates.io/crates/sharded-slab)
[sharded-slab](https://crates.io/crates/sharded-slab)
is a lock-free concurrent slab.
Slabs provide pre-allocated storage for many instances of a single data type. When a large number of values of a single type are required, this can be more efficient than allocating each item individually. Since the allocated items are the same size, memory fragmentation is reduced, and creating and removing new items can be very cheap.

## [slab](https://crates.io/crates/slab)
[slab](https://crates.io/crates/slab)
provides pre-allocated storage for a uniform data type.

## [rust-gc](https://github.com/Manishearth/rust-gc)
[rust-gc](https://github.com/Manishearth/rust-gc)
is a simple tracing (mark and sweep) garbage collector for Rust
.


## References 

- [Rust Crates - Memory Management Related](https://crates.io/categories/memory-management?sort=downloads)

- [[KAIST CS492C, 2020 Fall] Safe Memory Reclamation (crossbeam-epoch)](https://www.youtube.com/watch?v=rL9Z8eQEgek)

- [ECE 459 Lecture 16: Crossbeam](https://www.youtube.com/watch?v=6BYKw0Y758Q)

- [Solve concurrency issue with crossbeam. Rust Lang](https://www.youtube.com/watch?v=FJl0mQ_gNE4)

- [crossbeam / rust](https://www.youtube.com/watch?v=uVIdqs_OHAs)

- [ECE 459 Lecture 16: Rayon](https://www.youtube.com/watch?v=L0dEE2IqbD8)

- [I built a garbage collector for a language that doesn't need one](https://claytonwramsey.github.io/2023/08/14/dumpster.html)


