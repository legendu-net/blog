Status: published
Date: 2021-10-26 22:38:20
Modified: 2023-06-04 23:52:18
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

## Benchmark Numbers for Rust

[Infographics: Operation Costs in CPU Clock Cycles](http://ithare.com/infographics-operation-costs-in-cpu-clock-cycles/)

[Introduction to C and Computer Organization](https://sites.google.com/site/arch1utep/home/course_outline/msp430-instruction-timing)

random access of an element of array,

my impression is that it's about 6-7 CPU cycles (including bound check).
get_unchecked (without bound check) takes about 4 CPU cycles (verify this)

[How much does an array access cost?](https://pqnelson.github.io/2021/08/23/array-access-cost.html)

multiplication of an non-const integer with a const integer: 4.5 cpu cycles 

multiplication of 2 non-const usize: 6 cpu cycles

usize::count_trailing_zeros: 9.5 CPU cycles
usize::count_ones: 21 CPU cycles

f64::max: about 12?
f64::max is not fast due to the fact that it needs to handle NaNs.
A simple implementation of max using `>`
is much faster if your data won't have NaNs.


Vec::clear / ArrayVec::clear: 2



## References

- [Conditional compilation for benchmarks](https://users.rust-lang.org/t/conditional-compilation-for-benchmarks/47227)

- [How to benchmark a private function on all versions of the compiler](https://users.rust-lang.org/t/how-to-benchmark-a-private-function-on-all-versions-of-the-compiler/11210)

- [Why my Rust benchmarks were wrong, or how to correctly use std::hint::black_box?](https://gendignoux.com/blog/2022/01/31/rust-benchmarks.html)

- [criterion](https://crates.io/crates/criterion)

- [Benchmark testing your Rust code](https://www.youtube.com/watch?v=eIB3Pd5LBkc)

- [cargo-benchcmp](https://github.com/BurntSushi/cargo-benchcmp)

- [Useful tip for benchmarking/testing optional Cargo features](https://users.rust-lang.org/t/useful-tip-for-benchmarking-testing-optional-cargo-features/60365)

- https://github.com/madsmtm/objc2/blob/master/objc2/benches/autorelease.rs

