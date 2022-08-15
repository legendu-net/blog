Status: published
Date: 2021-04-22 21:11:46
Author: Benjamin Du
Slug: tips-on-rustc
Title: Tips on rustc
Category: Computer Science
Tags: Computer Science, programming, Rust, rustc, optimization, cargo
Modified: 2022-08-14 20:55:35

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Optimization 

[Cheap tricks for high-performance Rust](https://deterministic.space/high-performance-rust.html)

[Optimizations: the speed size tradeoff](https://docs.rust-embedded.org/book/unsorted/speed-vs-size.html)

[A performance retrospective using Rust (part 3)](https://agourlay.github.io/rust-performance-retrospective-part3/)

[The Magic of zerocopy](https://swatinem.de/blog/magic-zerocopy/)

1. By default, 
    the Rust compiler `rustc` does no speed/size optimizations (`-C opt-level=0`).

2. `rustc` supports three levels of optimization for speed (`-C opt-level=1`, `-C opt-level=2` and `-C opt-level=3`)
    and 2 levels of optimization for size (`-C opt-level=s` and `-C opt-level=z`).

3. `rustc -O` is equivalent to `rustc -C opt-level=2`
    and `cargo build --release` uses the release profile which defaults to `-C opt-level=3`.

## References

- [Optimizations: the speed size tradeoff](https://docs.rust-embedded.org/book/unsorted/speed-vs-size.html)

- [Cheap tricks for high-performance Rust](https://deterministic.space/high-performance-rust.html)

- [Inline In Rust](https://matklad.github.io/2021/07/09/inline-in-rust.html)

