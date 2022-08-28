Status: published
Date: 2021-11-20 22:36:35
Modified: 2022-08-26 10:46:42
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

![rust-collection-summary](https://user-images.githubusercontent.com/824507/151688238-88410b52-723d-4d31-bcb1-0a6c8580fb95.png)

## Third-party Collections and Related Tools

heapless / [arrayvec](https://crates.io/crates/arrayvec): stores on the stack only. Limited capacity, capacity set at creation.

smallvec: stores some elements on the stack, falls back to the heap if the stack capacity is exceeded.

tinyvec: provides both, implemented in 100% safe code. For example, smallvec had 5 memory safety bugs to date; they are guaranteed to never happen with tinyvec. The drawback is that the stack storage is zero-initialized on creation, which incurs some cost; for small capacities it's usually negligible, but adds up if you want to store thousands of elements.

Contiguous Data in Rust
https://github.com/paulkernfeld/contiguous-data-in-rust

ndarray
https://crates.io/crates/ndarray

An n-dimensional array for general elements and for numerics. Lightweight array views and slicing; views support chunking and splitting.


- [heapless](https://crates.io/crates/heapless)
    provides `static` friendly data structures that don't require dynamic memory allocation.

- [dashmap](https://crates.io/crates/dashmap)
    is a blazing fast concurrent HashMap for Rust.

- [arrayvec](https://crates.io/crates/arrayvec)
    [arrayvec](https://crates.io/crates/arrayvec)
    provides a vector with fixed capacity, 
    backed by an array (which is stored on the stack).
    Notice that you cannot collect an iterator into an Array.
    However,
    you can collect an iterator into an ArrayVec.
    For more discussions,
    please refer to
    [How do I collect into an array?](https://stackoverflow.com/questions/26757355/how-do-i-collect-into-an-array)
    .

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

### Make It Easy to Construct Arrays

Please refer to 
[Array in Rust](https://www.legendu.net/misc/blog/rust-collection-array/)
for detailed discussions.

## References 

- [Iterator in Rust](http://www.legendu.net/misc/blog/rust-collection-iterator/)

- [String in Rust](http://www.legendu.net/misc/blog/rust-str/)

- [Array in Rust](http://www.legendu.net/misc/blog/rust-collection-array/)

- [Range in Rust](http://www.legendu.net/misc/blog/rust-collection-range/)

- [Tuple in Rust](http://www.legendu.net/misc/blog/rust-collection-tuple/)

- [HashMap in Rust](http://www.legendu.net/misc/blog/rust-hashmap/)

- [Vector in Rust](http://www.legendu.net/misc/blog/rust-vector/)

- [Set in Rust](http://www.legendu.net/misc/blog/set-in-rust/)

- [Data Frame Implementations in Rust](http://www.legendu.net/misc/blog/data-frame-implementations-in-rust/)
