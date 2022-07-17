Status: published
Date: 2022-07-16 18:37:46
Modified: 2022-07-16 18:37:46
Author: Benjamin Du
Slug: compress-and-decompress-files-in-rust
Title: Compress and Decompress Files in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, compress, decompress, zip, tar

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. [tar](https://crates.io/crates/tar)
    is a Rust implementation of a TAR file reader and writer. 
    This library does not currently handle compression, but it is abstract over all I/O readers and writers. 
    Additionally, great lengths are taken to ensure that the entire contents are never required to be entirely resident in memory all at once.

2. [zip](https://crates.io/crates/zip)
    is a library to support the reading and writing of zip files.


