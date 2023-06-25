Status: published
Date: 2023-01-08 21:33:57
Modified: 2023-06-24 16:47:16
Author: Benjamin Du
Slug: tips-on-bytehound
Title: Tips on Bytehound
Category: Computer Science
Tags: Computer Science, programming, Rust, Bytehound, memory, profiling

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Bytehound works with Rust stable 
(Rust nightly is not required)
.

## Installation

    :::bash
    apt-get install gcc nodejs npm
    npm install -g yarn
    cargo build --release -p bytehound-preload
    cargo build --release -p bytehound-cli

Or if you use 
[icon](https://github.com/legendu-net/icon),

    :::bash
    icon bytehound -ic

## Usage

Run your application with bytehound to collect memory usage data.

    :::bash
    export MEMORY_PROFILER_LOG=warn
    LD_PRELOAD=./libbytehound.so ./your_application

Below is an example script, 
which build the "release-debug" version of the Rust project and run it.

    :::bash
    cargo build --profile release-debug
    export MEMORY_PROFILER_LOG=warn
    LD_PRELOAD=~/.local/lib/libbytehound.so ../../target/release-debug/ofcp_test play_r1 \
        --five-cards "7c Js Qs 3d 2s" \
        --num-sim1 10 \
        --num-sim2 10 \
        --num-sim3 10 \
        --num-sim4 10

Start a web server to visualize the memory profiling data.

    :::bash
    bytehound server --port 9090 -i 0.0.0.0 memory-profiling_*.dat 

## References

- [ByteHound @ GitHub](https://github.com/koute/bytehound)
