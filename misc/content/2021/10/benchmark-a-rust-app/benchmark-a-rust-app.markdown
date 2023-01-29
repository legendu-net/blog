Status: published
Date: 2021-10-26 22:38:20
Modified: 2022-08-14 13:37:21
Author: Benjamin Du
Slug: benchmark-a-rust-app
Title: Benchmark a Rust App
Category: Computer Science
Tags: Computer Science, programming, Rust, bench, benchmark, cargo, cargo-bench, criterion

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Traps 

1. The built-in benchmarking is still unstable and will likely be deprecated.

2. [criterion](https://crates.io/crates/criterion)
    is currently the best Rust crate for benchmarking.

## [Criterion](https://crates.io/crates/criterion)

1. With Rust stable, 
    Criterion can only benchmark public functions/methods
    .

2. Criterion supports the same filtering behavior that the standard-library testing and benchmarking tools support, 
    so you should be able to just run `cargo bench NAME` 
    and it will only run benchmarks with "NAME" in the benchmark name or function name.

3. Even if Criterion is currently the best available benchmarking tool available in Rust,
    it still have a few issues.
    - It can only benchmark public functions/methods with Rust stable
    - If you benchmark WALL/CPU times, 
        the benchmark results of the same function (without code change)
        might vary significantly with 2 benchmarks running at very close times.
        It is suggested that you benchmark Linux perf events instead,
        which gives you stable benchmark results.

4. There are lots of Criterion extensions enhancing features of Criterion.
    - cargo-criterion
    - [criterion-perf-events](https://crates.io/crates/criterion-perf-events)
        This is a measurement plugin for Criterion.rs to measure events of the Linux perf interface.
    - [criterion-cycles-per-byte](https://crates.io/crates/criterion-cycles-per-byte)
        measures (proportional) clock cycles using the x86 or x86_64 `rdtsc` instruction.
        Notice that RDTSC 
        (and thus [criterion-cycles-per-byte](https://crates.io/crates/criterion-cycles-per-byte))
        does not measure accurate CPU cycles.
        Please refer to
        [RDTSC does not measure cycles](https://github.com/wainwrightmark/criterion-cycles-per-byte/issues/1)
        for detailed discussions.
    - [criterion-linux-perf](https://crates.io/crates/criterion-linux-perf)
        A measurement plugin for Criterion.rs that provides measurements using Linux's perf interface

## [Iai](https://crates.io/crates/iai)
1. [Iai](https://crates.io/crates/iai)
    is an experimental benchmarking harness 
    that uses Cachegrind to perform extremely precise single-shot measurements of Rust code.

2. The idea of Iai is very cool,
    but unfotuantely it does not support excluding setup code from benchmark at this time.
    This makes Iai unusable in most cases.
    The PR
    [Use Callgrind instead of Cachegrind #26](https://github.com/bheisler/iai/pull/26)
    might fix this issue later.

## References

- [criterion](https://crates.io/crates/criterion)

- [Benchmark testing your Rust code](https://www.youtube.com/watch?v=eIB3Pd5LBkc)

- [cargo-benchcmp](https://github.com/BurntSushi/cargo-benchcmp)

- [Useful tip for benchmarking/testing optional Cargo features](https://users.rust-lang.org/t/useful-tip-for-benchmarking-testing-optional-cargo-features/60365)

- https://github.com/madsmtm/objc2/blob/master/objc2/benches/autorelease.rs

