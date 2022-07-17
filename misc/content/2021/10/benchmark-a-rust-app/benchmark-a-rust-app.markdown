Status: published
Date: 2021-10-26 22:38:20
Modified: 2022-07-17 00:38:23
Author: Benjamin Du
Slug: benchmark-a-rust-app
Title: Benchmark a Rust App
Category: Computer Science
Tags: Computer Science, programming, Rust, bench, benchmark, cargo, cargo-bench, criterion

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. The built-in benchmarking is still unstable and will likely be deprecated.

2. [criterion](https://crates.io/crates/criterion)
    is currently the best Rust crate for benchmarking.

## Criterion

1. can only benchmark public functions/methods

2. Criterion.rs supports the same filtering behavior that the standard-library testing and benchmarking tools support, 
    so you should be able to just run `cargo bench NAME` 
    and it will only run benchmarks with "NAME" in the benchmark name or function name.

## Iai
[Iai](https://crates.io/crates/iai)
is an experimental benchmarking harness 
that uses Cachegrind to perform extremely precise single-shot measurements of Rust code.

## References

- [criterion](https://crates.io/crates/criterion)

- [Benchmark testing your Rust code](https://www.youtube.com/watch?v=eIB3Pd5LBkc)

- [cargo-benchcmp](https://github.com/BurntSushi/cargo-benchcmp)
