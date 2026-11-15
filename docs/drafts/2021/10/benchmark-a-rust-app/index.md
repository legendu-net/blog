---
title: Benchmark a Rust App
created: '2021-10-26T22:38:20-07:00'
date: '2026-11-15T12:20:38-08:00'
authors:
  - bendu
label: benchmark-a-rust-app
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - bench
  - benchmark
  - Cargo
  - cargo-bench
  - criterion
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Traps

1. Rust's built-in benchmark feature has been unstable (on nightly channel only) for many years
   and will likely be deprecated.

## Comparison of Popular Benchmark Tools for Rust

1. [criterion](https://crates.io/crates/criterion)
   was the most popular choice for benchmarking code.

1. [divan](https://github.com/nvzqz/divan)
   is a newer modern alternative to criterion with many more features.

1. [Gungraun](https://github.com/gungraun/gungraun)
   is another rising tool for benching Rust code.
   It leverages Valgrind's profiling tools like Callgrind, Cachegrind and DHAT
   to provide extremely accurate and consistent measurements of Rust code,
   making it perfectly suited to run in environments like a CI.

```{list-table} Rust Benchmarking Tool Comparison
---
header-rows: 1
---
* - Feature
  - [Criterion](https://crates.io/crates/criterion)
  - [Divan](https://github.com/nvzqz/divan)
  - [Gungraun](https://github.com/gungraun/gungraun)
* - Measurement
  - Wall-clock time
  - Wall-clock time
  - Instruction counts / Cache misses
* - CPU Cycles
  - via [criterion-perf-events](https://crates.io/crates/criterion-perf-events) [^criterion_perf_events]
  - Built-in support via TSC for x86.
  - Built-in support for estimated CPU cycles.
* - Method
  - Statistical (100+ runs)
  - Statistical (100+ runs)
  - One-shot (via Valgrind)
* - Noise
  - Sensitive to OS jitter
  - Sensitive to OS jitter
  - **Zero noise** (Deterministic)
* - Reports
  - HTML Graphs / Console
  - Console / Memory usage
  - Callgrind / Flamegraphs
* - Setup
  - High boilerplate
  - **Very Low** (Attributes)
  - Moderate (Requires Valgrind)
* - Platform
  - Cross-platform
  - Cross-platform
  - Linux/macOS only
```

## [Criterion](https://crates.io/crates/criterion)

1. With Rust stable,
   Criterion can only benchmark public functions/methods
   .

1. Criterion supports the same filtering behavior that the standard-library testing and benchmarking tools support,
   so you should be able to just run `cargo bench NAME`
   and it will only run benchmarks with "NAME" in the benchmark name or function name.

1. Even if Criterion is currently the best available benchmarking tool available in Rust,
   it still have a few issues.

   - It can only benchmark public functions/methods with Rust stable
   - If you benchmark WALL/CPU times,
     the benchmark results of the same function (without code change)
     might vary significantly with 2 benchmarks running at very close times.
     It is suggested that you benchmark Linux perf events instead,
     which gives you stable benchmark results.

1. There are lots of Criterion extensions enhancing features of Criterion.

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

## [divan](https://github.com/nvzqz/divan)

[divan](https://github.com/nvzqz/divan)
is a fast and simple benchmarking for Rust projects.

## [Gungraun](https://github.com/gungraun/gungraun)

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

[^criterion_perf_events]: Not recommended: Linux only; requires sudo access to set the kernel parameter kernel.perf_event_paranoid.
