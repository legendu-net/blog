Status: published
Date: 2021-11-08 10:19:34
Modified: 2022-07-31 11:39:06
Author: Benjamin Du
Slug: profile-rust-applications
Title: Profile Rust Applications
Category: Computer Science
Tags: Computer Science, programming, Rust, profile, profiling, speed, memory, CPU, FlameGraph, ByteHound, HeapTrack

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## Tips for Rust Optimization and Profiling

1. [The Rust Performance Book](https://nnethercote.github.io/perf-book/title-page.html)
    has a comprehensive guide on optimizing Rust code.
    [Rust Performance Pitfalls](https://llogiq.github.io/2017/06/01/perf-pitfalls.html)
    discusses about some performance pitfalls that you want to avoid.

2. [rustfilt](https://crates.io/crates/rustfilt)
    demangles Rust symbol names using 
    [rustc-demangle](https://github.com/rust-lang/rustc-demangle)
    . 

## CPU Profiling

### [Valgrind](http://www.legendu.net/misc/blog/profile-rust-applications-using-valgrind/)
[Valgrind](http://www.legendu.net/misc/blog/profile-rust-applications-using-valgrind/)
is a great profiler for Rust applications.

### [FlameGraph](http://www.legendu.net/misc/blog/profile-rust-applications-using-flamegraph)

[FlameGraph](http://www.legendu.net/misc/blog/profile-rust-applications-using-flamegraph)
is another good profiler for Rust applications 
which is has integration support for cargo.

[Valgrind](http://www.legendu.net/misc/blog/profile-rust-applications-using-valgrind/)
is preferred for several reasons.

1. Valgrind is easier to install, configure and use.
    Flamegraph relies on `perf` which is not user-friendly.

2. The Flamegraph project is no longer in active development.

3. Valgrind is more powerful and flexible 
    and can be used for profiling other porgramming languages too.

## Memory Profiling

[bytehound](https://github.com/koute/bytehound)
is a memory profiler for Linux.

[heaptrack](https://github.com/KDE/heaptrack)
is a heap memory profiler for Linux


## References

- [The Rust Performance Book - Profiling](https://nnethercote.github.io/perf-book/profiling.html)

- [Rust Performance Pitfalls](https://llogiq.github.io/2017/06/01/perf-pitfalls.html)

- [How To Write Fast Rust Code](http://likebike.com/posts/How_To_Write_Fast_Rust_Code.html)

- [Top-Down performance analysis methodology](https://easyperf.net/blog/2019/02/09/Top-Down-performance-analysis-methodology)

- [Profile Rust Applications Using Valgrind](http://www.legendu.net/misc/blog/profile-rust-applications-using-valgrind/)

- [Profile Rust Applications Using Flamegraph](http://www.legendu.net/misc/blog/profile-rust-applications-using-flamegraph/)

- [Rust Crate - profiling](https://crates.io/crates/profiling)

- [How-to Optimize Rust Programs on Linux](http://www.codeofview.com/fix-rs/2017/01/24/how-to-optimize-rust-programs-on-linux/)

- [Is it possible to print the callgraph of a Cargo workspace?](https://users.rust-lang.org/t/is-it-possible-to-print-the-callgraph-of-a-cargo-workspace/50369)

- [Linux performance testing with perf, gprof and Valgrind](https://blog.appliscale.io/2018/04/30/tools-4-linux-performance-testing/)

