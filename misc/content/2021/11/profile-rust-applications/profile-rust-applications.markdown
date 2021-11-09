Status: published
Date: 2021-11-08 10:19:34
Modified: 2021-11-09 10:21:29
Author: Benjamin Du
Slug: profile-rust-applications
Title: Profile Rust Applications
Category: Computer Science
Tags: Computer Science, programming, Rust, profile, profiling

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## FlameGraph

[flamegraph](https://github.com/flamegraph-rs/flamegraph)

```
wajig update 
wajig install linux-tools-common linux-tools-generic linux-tools-`uname -r`
cargo install flamegraph
```
Run the following command to generate a SVG visualization of performance profiling.
Do not use `cargo flamegraph` directly 
unless you are using the root account.
```
sudo ~/.cargo/bin/flamegraph -o flamegraph.svg /path/to/rust_app_binary
```

## perf

[Running `perf` in docker & kubernetes](https://medium.com/@geekidea_81313/running-perf-in-docker-kubernetes-7eb878afcd42)

[Security implications of changing “perf_event_paranoid”](https://unix.stackexchange.com/questions/519070/security-implications-of-changing-perf-event-paranoid)

[Run perf without root-rights](https://superuser.com/questions/980632/run-perf-without-root-rights)

## References

[The Rust Performance Book - Profiling](https://nnethercote.github.io/perf-book/profiling.html)

https://easyperf.net/blog/2019/02/09/Top-Down-performance-analysis-methodology

https://crates.io/crates/profiling