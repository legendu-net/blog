---
title: CPU Profiling of Rust Applications Using Valgrind
created: '2022-01-13T01:02:06-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: cpu-profiling-of-rust-applications-using-valgrind
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - profile
  - profiler
  - Valgrind
  - KCacheGrind
  - CPU
  - profiling
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

It is suggested that you profile Rust application using
[not-perf](https://github.com/koute/not-perf)
.
For more discussions,
please refer to
[Profile Rust Applications](profile-rust-applications)
.

## Installation on Ubuntu

```bash
sudo apt install valgrind
```

## Profile Your Application Using CallGrind

```bash
valgrind --tool=callgrind --dump-instr=yes --simulate-cache=yes --collect-jumps=yes \
    your-program [program options]
```

Below is an example.

```bash
cargo build --profile release-debug
valgrind --tool=callgrind --dump-instr=yes --simulate-cache=yes --collect-jumps=yes \
    ../ofcp_utils/target/release-debug/ofcp_utils score_r4_it_sim_prof \
    --file ../ofcp_utils/data/plays_r4_21.csv \
    --method sim \
    --runs 1000
```

## Visualization

[KCacheGrind](https://github.com/KDE/kcachegrind)

## General Tips and Traps

1. Profiling an application using valgrind is about 50-200 times slower
   than running the application.
   It is suggested that you use not-perf for profiling long-running Rust applicaitons.

1. Valgrind seems to have some issues with Rust applications.
   Only performance data of public methods are dumped.
   A hack way to fix this issue
   is to mark all methods
   that you want to profile as `pub` in your Rust code.

## References

- [Tips on Valgrind](tips-on-valgrind)

- [Profile Rust Applications](profile-rust-applications)

- [Profile Rust Applications Using Flamegraph](profile-rust-applications-using-flamegraph)

- [Profiling with Valgrind](https://developer.mantidproject.org/ProfilingWithValgrind.html)

- [Callgrind: a call-graph generating cache and branch prediction profiler](https://valgrind.org/docs/manual/cl-manual.html)

- [KCacheGrind](https://github.com/KDE/kcachegrind)

- [Rust and Valgrind](https://nnethercote.github.io/2022/01/05/rust-and-valgrind.html)
