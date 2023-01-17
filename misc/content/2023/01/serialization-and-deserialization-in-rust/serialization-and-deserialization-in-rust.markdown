Status: published
Date: 2023-01-13 16:44:56
Modified: 2023-01-14 00:49:54
Author: Benjamin Du
Slug: serialization-and-deserialization-in-rust
Title: Serialization and Deserialization in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, serialization, deserialization, binary, encoding

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [serde Based Serialization and Deserialization](https://www.legendu.net/en/blog/hands-on-the-Rust-library-serde/)

### [serde](https://www.legendu.net/en/blog/hands-on-the-Rust-library-serde/)
[serde](https://www.legendu.net/en/blog/hands-on-the-Rust-library-serde/)
is a generic serialization/deserialization framework
.

### https://crates.io/crates/serde_with
This crate provides custom de/serialization helpers 
to use in combination with serde's with-annotation and with the improved serde_as-annotation.

https://crates.io/crates/ciborium
Ciborium contains CBOR serialization and deserialization implementations for serde.

### [serde_yaml](https://www.legendu.net/misc/blog/handle-duplicated-keys-in-serde-yaml/)
[serde_yaml](https://www.legendu.net/misc/blog/handle-duplicated-keys-in-serde-yaml/)
is a YAML data format for Serde
.

https://crates.io/crates/serde-big-array
Big array helper for serde. The purpose of this crate is to make (de-)serializing arrays of sizes > 32 easy. This solution is needed until serde adopts const generics support.



### [serde_stacker](https://crates.io/crates/serde_stacker)
[serde_stacker](https://crates.io/crates/serde_stacker)
is a serde adapter that avoids stack overflow by dynamically growing the stack
.

## https://crates.io/crates/minicbor
A small CBOR codec suitable for no_std environments.

## [bincode](https://github.com/bincode-org/bincode)
[bincode](https://github.com/bincode-org/bincode)
is a compact encoder / decoder pair that uses a binary zero-fluff encoding scheme. 
The size of the encoded object will be the same or smaller 
than the size that the object takes up in memory in a running Rust program.


## Other Crates
Strictly speaking,
the following crates are not serialization/deserialization crates.
There are more like binary encoding/decoding crates. 
However,
they can be very useful when you work with primitive types in Rust.

## [parquet](https://crates.io/crates/parquet)
[parquet](https://crates.io/crates/parquet)
is an Apache Parquet implementation in Rust.

## [atoi-rs](https://github.com/pacman82/atoi-rs)
[atoi-rs](https://github.com/pacman82/atoi-rs)
parses integers directly from [u8] slices in safe code
.

## References

- [  Hands on the Rust Library Serde  ](https://www.legendu.net/en/blog/hands-on-the-Rust-library-serde)  |  en/content/2021/04/hands-on-the-Rust-library-serde/hands-on-the-Rust-library-serde.ipynb

- [  Parse TOML Files in Rust  ](https://www.legendu.net/misc/blog/parse-toml-files-in-rust)  |  misc/content/2022/05/parse-toml-files-in-rust/parse-toml-files-in-rust.ipynb

- [  Data Frame Implementations in Rust  ](https://www.legendu.net/misc/blog/data-frame-implementations-in-rust)  |  misc/content/2021/06/dataframe-implementations-in-rust/dataframe-implementations-in-rust.markdown
