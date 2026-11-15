---
title: Tips on Bytehound
created: '2023-01-08T21:33:57-08:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: tips-on-bytehound
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - Bytehound
  - memory
  - profiling
---

Bytehound works with Rust stable
(Rust nightly is not required)
.

## Installation

```bash
apt-get install gcc nodejs npm
npm install -g yarn
cargo build --release -p bytehound-preload
cargo build --release -p bytehound-cli
```

Or if you use
[icon](https://github.com/legendu-net/icon),

```bash
icon bytehound -ic
```

## Usage

Run your application with bytehound to collect memory usage data.

```bash
export MEMORY_PROFILER_LOG=warn
LD_PRELOAD=./libbytehound.so ./your_application
```

Below is an example script,
which build the "release-debug" version of the Rust project and run it.

```bash
cargo build --profile release-debug
export MEMORY_PROFILER_LOG=warn
LD_PRELOAD=~/.local/lib/libbytehound.so ../../target/release-debug/ofcp_test play_r1 \
    --five-cards "7c Js Qs 3d 2s" \
    --num-sim1 10 \
    --num-sim2 10 \
    --num-sim3 10 \
    --num-sim4 10
```

Start a web server to visualize the memory profiling data.

```bash
bytehound server --port 9090 -i 0.0.0.0 memory-profiling_*.dat
```

## References

- [ByteHound @ GitHub](https://github.com/koute/bytehound)
