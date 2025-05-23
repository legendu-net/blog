Status: published
Date: 2022-05-22 08:44:04
Modified: 2023-01-07 12:45:14
Author: Benjamin Du
Slug: read-and-write-parquet-files-in-rust
Title: Read and Write Parquet Files in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, Parquet, IO, crate, Polars, Arrow, Apache Arrow

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are a few crates in Rust which can help read and write Parquet files,
among which
[Polars](https://crates.io/crates/polars)
is the best one. 
As a matter of fact,
polars is a DataFrame implementation in Rust
which is way beyond Parquet IO.
The 
[parquet](https://crates.io/crates/parquet)
crate might still be useful if you want to scan Parquet files row by row.
Other Parquet related crates are low-level ones
and are not average user oriented.

## [Polars](https://crates.io/crates/polars)
The 
[polars](https://crates.io/crates/polars)
crate is a blazingly fast DataFrames library implemented in Rust 
using Apache Arrow Columnar Format as memory model.
It supports reading/writing Parquet files of course.

## [parquet](https://crates.io/crates/parquet)

The 
[parquet](https://crates.io/crates/parquet)
crate contains the official Native Rust implementation of Apache Parquet, 
which is part of the Apache Arrow project.


## [arrow](https://crates.io/crates/arrow)

The 
[arrow](https://crates.io/crates/arrow)
crate contains the official Native Rust implementation of Apache Arrow in memory format, 
governed by the Apache Software Foundation. 


## [parquet2](https://crates.io/crates/parquet2)

The 
[parquet2](https://crates.io/crates/parquet2)
crate is a re-write of the official 
[parquet](https://crates.io/crates/parquet)
crate with performance, 
parallelism and safety in mind.
The 
[parquet2](https://crates.io/crates/parquet2)
decouples reading (IO intensive) from computing (CPU intensive)
and delegates parallelism to downstream.
It cannot be used directly to read parquet (except metadata). 
To read data from parquet, checkout arrow2.


## [arrow2](https://crates.io/crates/arrow2)

The 
[arrow2](https://crates.io/crates/arrow2)
crate is an unofficial implementation of Apache Arrow spec in safe Rust.
It is the most feature-complete implementation of the Arrow format 
after the C++ implementation.



## References

- [Hands on the Rust Crate Parquet](http://www.legendu.net/misc/blog/hands-on-the-rust-crate-parquet/)

- [Hands on Polars in Rust](https://www.legendu.net/misc/blog/hands-on-polars-in-rust/)

- [Data Frame Implementations in Rust](https://www.legendu.net/misc/blog/data-frame-implementations-in-rust/)

