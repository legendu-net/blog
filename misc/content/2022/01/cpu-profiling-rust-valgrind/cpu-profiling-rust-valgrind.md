Status: published
Date: 2022-01-13 01:02:06
Modified: 2023-04-17 14:30:28
Author: Benjamin Du
Slug: cpu-profiling-rust-valgrind
Title: CPU Profiling of Rust Applications Using Valgrind
Category: Computer Science
Tags: Computer Science, programming, Rust, profile, profiler, Valgrind, KCacheGrind, CPU, profiling

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

It is suggested that you profile Rust application using 
[not-perf](https://github.com/koute/not-perf)
.
For more discussions,
please refer to
[Profile Rust Applications](http://www.legendu.net/misc/blog/profile-rust-applications/)
.

## Installation on Ubuntu

    :::bash
    wajig install valgrind

## Profile Your Application Using CallGrind

    :::bash
    valgrind --tool=callgrind --dump-instr=yes --simulate-cache=yes --collect-jumps=yes \
        your-program [program options]

Below is an example.
    
    :::bash
    cargo build --profile release-debug
    valgrind --tool=callgrind --dump-instr=yes --simulate-cache=yes --collect-jumps=yes \
        ../ofcp_utils/target/release-debug/ofcp_utils score_r4_it_sim_prof \
            --file ../ofcp_utils/data/plays_r4_21.csv \
            --method sim \
            --runs 1000

## Visualization

[KCacheGrind](https://github.com/KDE/kcachegrind)

## General Tips and Traps 

1. Profiling an application using valgrind is about 50-200 times slower
    than running the application.
    It is suggested that you use not-perf for profiling long-running Rust applicaitons.

2. Valgrind seems to have some issues with Rust applications.
    Only performance data of public methods are dumped.
    A hack way to fix this issue 
    is to mark all methods 
    that you want to profile as `pub` in your Rust code.

## References 

- [Tips on Valgrind](https://www.legendu.net/misc/blog/tips-on-valgrind)

- [Profile Rust Applications](http://www.legendu.net/misc/blog/profile-rust-applications/)

- [Profile Rust Applications Using Flamegraph](http://www.legendu.net/misc/blog/profile-rust-applications-using-flamegraph/)

- [Profiling with Valgrind](https://developer.mantidproject.org/ProfilingWithValgrind.html)

- [Callgrind: a call-graph generating cache and branch prediction profiler](https://valgrind.org/docs/manual/cl-manual.html)

- [KCacheGrind](https://github.com/KDE/kcachegrind)

- [Rust and Valgrind](https://nnethercote.github.io/2022/01/05/rust-and-valgrind.html)
