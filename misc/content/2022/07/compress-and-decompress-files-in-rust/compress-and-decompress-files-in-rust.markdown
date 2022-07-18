Status: published
Date: 2022-07-16 18:37:46
Modified: 2022-07-18 00:26:49
Author: Benjamin Du
Slug: compress-and-decompress-files-in-rust
Title: Compress and Decompress Files in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, compress, decompress, zip, tar, DEFLATE, flate2

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Please refer to
[Rust Crates - Compression Related](https://crates.io/categories/compression?sort=downloads)
for details.

1. [tar](https://crates.io/crates/tar)
    is a Rust implementation of a TAR file reader and writer. 
    This library does not currently handle compression, but it is abstract over all I/O readers and writers. 
    Additionally, great lengths are taken to ensure that the entire contents are never required to be entirely resident in memory all at once.

2. [flate2](https://crates.io/crates/flate2)
    provides DEFLATE compression and decompression exposed as Read/BufRead/Write streams. 
    Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.

2. [snap](https://crates.io/crates/snap)
    is a pure Rust implementation of the Snappy compression algorithm 
    including streaming compression and decompression.

2. [zip](https://crates.io/crates/zip)
    is a library to support the reading and writing of zip files.


