Status: published
Date: 2022-01-13 01:02:06
Modified: 2022-01-13 13:28:01
Author: Benjamin Du
Slug: profile-rust-applications-using-valgrind
Title: Profile Rust Applications Using Valgrind
Category: Computer Science
Tags: Computer Science, programming, Rust, profile, profiler, Valgrind, KCacheGrind

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Ubuntu

    :::bash
    wajig install valgrind

## Profile Your Application Using CallGrind

    :::bash
    valgrind --tool=callgrind --dump-instr=yes --simulate-cache=yes --collect-jumps=yes your-program [program options]

## Visualization

[KCacheGrind](https://github.com/KDE/kcachegrind)

## References 

- [Profile Rust Applications](http://www.legendu.net/misc/blog/profile-rust-applications/)

- [Profiling with Valgrind](https://developer.mantidproject.org/ProfilingWithValgrind.html)

- [Callgrind: a call-graph generating cache and branch prediction profiler](https://valgrind.org/docs/manual/cl-manual.html)

- [KCacheGrind](https://github.com/KDE/kcachegrind)
