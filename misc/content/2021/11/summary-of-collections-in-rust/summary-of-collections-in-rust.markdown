Status: published
Date: 2021-11-20 22:36:35
Modified: 2021-11-20 22:36:35
Author: Benjamin Du
Slug: summary-of-collections-in-rust
Title: Summary of Collections in Rust
Category: Computer Science
Tags: Computer Science, programming

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


The module 
[std::collections](https://doc.rust-lang.org/std/collections/index.html)
has a good summary on popular collection data structures in Rust 
and when to use them.

- Sequences: Vec, VecDeque (double-ended queue), LinkedList (doubly-linked list)
- Maps: HashMap, BTreeMap (sorted map)
- Sets: HashSet, BTreeSet (sorted set)
- Misc: BinaryHeap (priority queue)

## Third-party Collections 

- [Crate - indexmap](https://crates.io/crates/indexmap)
    A pure-Rust hash table which preserves (in a limited sense) insertion order.

- [TinySet](https://crates.io/crates/tinyset)
    provides a few collections that are optimized to scale in size well for small numbers of elements, 
    while still scaling well in time (and size) for numbers of elements.

- [fnv](https://crates.io/crates/fnv)
    is an implementation of the Fowler–Noll–Vo hash function.

- [hashbrown](https://crates.io/crates/hashbrown)
    is a Rust port of Google's high-performance SwissTable hash map, 
    adapted to make it a drop-in replacement for Rust's standard HashMap and HashSet types.

## References 

