---
title: Profile Rust Applications
created: '2021-11-08T10:19:34-08:00'
date: '2026-06-19T10:11:38-07:00'
authors:
  - bendu
label: profile-rust-applications
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - profile
  - profiling
  - speed
  - memory
  - CPU
  - FlameGraph
  - Bytehound
  - HeapTrack
  - perf
  - Valgrind
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips for Rust Optimization and Profiling

1. [std::mem::size_of](https://doc.rust-lang.org/std/mem/fn.size_of.html)
   returns the stack size of a type.

1. [memuse](https://crates.io/crates/memuse)
   contains traits for measuring the dynamic memory usage of Rust types.

1. [The Rust Performance Book](https://nnethercote.github.io/perf-book/title-page.html)
   has a comprehensive guide on optimizing Rust code.
   [Rust Performance Pitfalls](https://llogiq.github.io/2017/06/01/perf-pitfalls.html)
   discusses about some performance pitfalls that you want to avoid.

1. [rustfilt](https://crates.io/crates/rustfilt)
   demangles Rust symbol names using
   [rustc-demangle](https://github.com/rust-lang/rustc-demangle)
   .

## CPU Profiling

The table below summarizes the CPU profiling tools discussed here.

```{list-table} CPU profiling tools for Rust applications
---
header-rows: 1
widths: 12 14 22 16 8 28
---
* - Tool
  - Rust-internal
  - Cargo / benchmark integration
  - Install & use
  - Speed
  - Comments
* - [not-perf](https://github.com/koute/not-perf)
  - No (standalone sampling profiler for Linux)
  - None
  - Very easy; no special configuration required
  - Fast
  - Currently the best CPU profiling tool for Rust applications
* - [samply](https://github.com/mstange/samply)
  - No (standalone command-line profiler)
  - None
  - Easy
  - —
  - Uses the Firefox profiler as its UI
* - [pprof](https://crates.io/crates/pprof)
  - Yes (Rust crate)
  - Yes — integrates with [Criterion](https://crates.io/crates/criterion); profile via `cargo bench --bench bench_main <name> -- --profile-time` (see [criterion.rs example](https://github.com/tikv/pprof-rs/blob/master/examples/criterion.rs))
  - Easy (added as a crate dependency)
  - —
  - Internal perf tool; Criterion benchmarks by default, so `--profile-time` is needed to emit a profiling report
* - [Valgrind](cpu-profiling-of-rust-applications-using-valgrind)
  - No
  - Yes — via [cargo-valgrind](https://crates.io/crates/cargo-valgrind)
  - Easy to install, configure and use
  - Slow
  - Much slower than not-perf
* - [FlameGraph](profile-rust-applications-using-flamegraph)
  - No (based on Linux perf)
  - Yes — has cargo support
  - Hardest to install, configure and use
  - —
  - Relies on Linux perf
* - [puffin](https://github.com/EmbarkStudios/puffin)
  - Yes (Rust crate)
  - —
  - —
  - —
  - Friendly little instrumentation profiler for Rust
```

## Memory Profiling

[bytehound](tips-on-bytehound)
is the best available memory profiling tool for Rust currently.

### [bytehound](tips-on-bytehound)

[bytehound](tips-on-bytehound)
is a memory profiler for Linux.

### [dhat-rs](https://crates.io/crates/dhat)

[dhat-rs](https://crates.io/crates/dhat)
provides heap profiling and ad hoc profiling capabilities to Rust programs,
similar to those provided by
[DHAT](https://valgrind.org/docs/manual/dh-manual.html)
.

### [DHAT](https://valgrind.org/docs/manual/dh-manual.html)

[DHAT](https://valgrind.org/docs/manual/dh-manual.html)
is a dynamic heap analysis tool that comes with Valgrind.

### [heaptrack](https://github.com/KDE/heaptrack)

[heaptrack](https://github.com/KDE/heaptrack)
is a heap memory profiler for Linux

## References

- [CPU Profiling of Rust Applications Using Valgrind](cpu-profiling-of-rust-applications-using-valgrind)

- [Profile Rust Applications Using Flamegraph](profile-rust-applications-using-flamegraph)

- [Tips on Valgrind](tips-on-valgrind)

- [The Rust Performance Book - Profiling](https://nnethercote.github.io/perf-book/profiling.html)

- [Rust Performance Pitfalls](https://llogiq.github.io/2017/06/01/perf-pitfalls.html)

- [How To Write Fast Rust Code](http://likebike.com/posts/How_To_Write_Fast_Rust_Code.html)

- [Top-Down performance analysis methodology](https://easyperf.net/blog/2019/02/09/Top-Down-performance-analysis-methodology)

- [Profile Rust Applications Using Valgrind](cpu-profiling-of-rust-applications-using-valgrind)

- [Profile Rust Applications Using Flamegraph](profile-rust-applications-using-flamegraph)

- [Rust Crate - profiling](https://crates.io/crates/profiling)

- [How-to Optimize Rust Programs on Linux](http://www.codeofview.com/fix-rs/2017/01/24/how-to-optimize-rust-programs-on-linux/)

- [Is it possible to print the callgraph of a Cargo workspace?](https://users.rust-lang.org/t/is-it-possible-to-print-the-callgraph-of-a-cargo-workspace/50369)

- [Linux performance testing with perf, gprof and Valgrind](https://blog.appliscale.io/2018/04/30/tools-4-linux-performance-testing/)
