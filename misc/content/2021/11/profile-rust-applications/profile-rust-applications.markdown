Status: published
Date: 2021-11-08 10:19:34
Modified: 2023-01-18 22:10:26
Author: Benjamin Du
Slug: profile-rust-applications
Title: Profile Rust Applications
Category: Computer Science
Tags: Computer Science, programming, Rust, profile, profiling, speed, memory, CPU, FlameGraph, ByteHound, HeapTrack

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips for Rust Optimization and Profiling

1. [std::mem::size_of](https://doc.rust-lang.org/std/mem/fn.size_of.html)
    returns the stack size of a type.

2. [memuse](https://crates.io/crates/memuse)
    contains traits for measuring the dynamic memory usage of Rust types.

3. [The Rust Performance Book](https://nnethercote.github.io/perf-book/title-page.html)
    has a comprehensive guide on optimizing Rust code.
    [Rust Performance Pitfalls](https://llogiq.github.io/2017/06/01/perf-pitfalls.html)
    discusses about some performance pitfalls that you want to avoid.

4. [rustfilt](https://crates.io/crates/rustfilt)
    demangles Rust symbol names using 
    [rustc-demangle](https://github.com/rust-lang/rustc-demangle)
    . 

## CPU Profiling

### [pprof](https://crates.io/crates/pprof)
[Pprof](https://crates.io/crates/pprof)
is an internal perf tools for rust programs.
It provides integration with 
[Criterion](https://crates.io/crates/criterion)
which is the most popular benchmark tool in Rust.
Please refer to
[pprof-rs/examples/criterion.rs](https://github.com/tikv/pprof-rs/blob/master/examples/criterion.rs)
for such an example.
However,
Criterion performs measuring/benchmarking instead of profiling by default.
To generate profiling report/visualization,
you can run the following command.

    :::bash
    cargo bench --bench bench_main name_of_benchmark -- --profile-time

### [Valgrind](http://www.legendu.net/misc/blog/profile-rust-applications-using-valgrind/)
[Valgrind](http://www.legendu.net/misc/blog/profile-rust-applications-using-valgrind/)
is a great profiler for Rust applications.
The crate
[cargo-valgrind](https://crates.io/crates/cargo-valgrind)
provides integration of valgrind and cargo.

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
is the best available memory profiling tool for Rust currently.

### [bytehound](https://github.com/koute/bytehound)
[bytehound](https://github.com/koute/bytehound)
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

- [CPU Profiling of Rust Applications Using Valgrind](https://www.legendu.net/misc/blog/cpu-profiling-rust-valgrind)  |  misc/content/2022/01/cpu-profiling-rust-valgrind/cpu-profiling-rust-valgrind.markdown

- [Profile Rust Applications Using Flamegraph](https://www.legendu.net/misc/blog/profile-rust-applications-using-flamegraph)  |  misc/content/2021/11/profile-rust-applications-using-flamegraph/profile-rust-applications-using-flamegraph.markdown

- [Tips on Valgrind](https://www.legendu.net/misc/blog/tips-on-valgrind)

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

