Status: published
Date: 2021-11-08 10:19:34
Modified: 2022-01-13 13:28:01
Author: Benjamin Du
Slug: profile-rust-applications
Title: Profile Rust Applications
Category: Computer Science
Tags: Computer Science, programming, Rust, profile, profiling, speed, memory, CPU, FlameGraph, ByteHound, HeapTrack

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## Tips for Rust Optimization and Profiling

1. [The Rust Performance Book](https://nnethercote.github.io/perf-book/title-page.html)
    has a comprehensive guide on optimizing Rust code.

2. [rustfilt](https://crates.io/crates/rustfilt)
    demangles Rust symbol names using 
    [rustc-demangle](https://github.com/rust-lang/rustc-demangle)
    . 

## CPU Profiling
### [FlameGraph](http://www.legendu.net/misc/blog/profile-rust-applications-using-flamegraph)

[FlameGraph](http://www.legendu.net/misc/blog/profile-rust-applications-using-flamegraph)
is a great profiler for Rust application.

### Valgrind

## Memory Profiling

[bytehound](https://github.com/koute/bytehound)
is a memory profiler for Linux.

[heaptrack](https://github.com/KDE/heaptrack)
is a heap memory profiler for Linux


## References

- [The Rust Performance Book - Profiling](https://nnethercote.github.io/perf-book/profiling.html)

- [Top-Down performance analysis methodology](https://easyperf.net/blog/2019/02/09/Top-Down-performance-analysis-methodology)

- [Rust Crate - profiling](https://crates.io/crates/profiling)

- [Is it possible to print the callgraph of a Cargo workspace?](https://users.rust-lang.org/t/is-it-possible-to-print-the-callgraph-of-a-cargo-workspace/50369)

- [How-to Optimize Rust Programs on Linux](http://www.codeofview.com/fix-rs/2017/01/24/how-to-optimize-rust-programs-on-linux/)

- [Is it possible to print the callgraph of a Cargo workspace?](https://users.rust-lang.org/t/is-it-possible-to-print-the-callgraph-of-a-cargo-workspace/50369)

