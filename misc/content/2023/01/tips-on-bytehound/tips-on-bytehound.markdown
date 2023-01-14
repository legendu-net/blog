Status: published
Date: 2023-01-08 21:33:57
Modified: 2023-01-08 23:12:24
Author: Benjamin Du
Slug: tips-on-bytehound
Title: Tips on Bytehound
Category: Computer Science
Tags: Computer Science, programming, Rust, Bytehound, memory, profiling

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## Installation

    apt-get install gcc nodejs npm
    npm install -g yarn
    cargo build --release -p bytehound-preload
    cargo build --release -p bytehound-cli

## Usage

    ./bytehound server --port 9090 -i 0.0.0.0 memory-profiling_*.dat 

## References

- [ByteHound @ GitHub](https://github.com/koute/bytehound)
