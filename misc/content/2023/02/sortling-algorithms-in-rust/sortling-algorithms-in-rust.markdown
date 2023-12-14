Status: published
Date: 2023-02-23 11:45:10
Modified: 2023-12-13 14:16:35
Author: Benjamin Du
Slug: sorting-algorithms-in-rust
Title: Sorting Algorithms in Rust
Category: Computer Science
Tags: Computer Science, programming, algorithm, algo, sort, Rust, GlideSort

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

- [slice::sort](https://doc.rust-lang.org/std/primitive.slice.html#method.sort)
- [slice::sort_by](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_by)
- [slice::sort_by_key](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_by_key)
- [slice::sort_unstable](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable)
- [slice::sort_unstable_by](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable_by)
- [slice::sort_unstable_by_key](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable_by_key)

## [GlideSort](https://crates.io/crates/glidesort)
[GlideSort](https://crates.io/crates/glidesort)
is a novel stable sorting algorithm 
that combines the best-case behavior of Timsort-style merge sorts for pre-sorted data 
with the best-case behavior of pattern-defeating quicksort 
for data with many duplicates. 
It is a comparison-based sort supporting arbitrary comparison operators, 
and while exceptional on data with patterns it is also very fast for random data.

## References

sort-research-rs
https://github.com/Voultapher/sort-research-rs/blob/main/writeup/sort_safety/text.md
