Status: published
Date: 2023-01-13 16:37:22
Modified: 2023-01-13 16:37:22
Author: Benjamin Du
Slug: useful-rust-crates-for-bit-manipulations
Title: Useful Rust Crates for Bit Manipulations
Category: Computer Science
Tags: Computer Science, programming, Rust, crate, useful, bit, operation, manipulation

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## [bytemuck](https://crates.io/crates/bytemuck)
[ByteMuck](https://crates.io/crates/bytemuck)
is a crate for mucking around with piles of bytes.
It lets you safely perform "bit cast" operations between data types. 
That's where you take a value and just reinterpret the bits 
as being some other type of value, 
without changing the bits.
It is like `f32::to_bits`, 
just generalized to let you convert between all sorts of data types.

## [bitflags](https://crates.io/crates/bitflags)
[bitflags](https://crates.io/crates/bitflags)
is a Rust macro to generate structures which behave like a set of bitflags.

## [bitvec](https://crates.io/crates/bitvec)
[bitvec](https://crates.io/crates/bitvec)
addresses memory by bits, for packed collections and bitfields

## [byteorder](https://crates.io/crates/byteorder)
[byteorder](https://crates.io/crates/byteorder)
is a library for reading/writing numbers in big-endian and little-endian.

## [bytes](https://crates.io/crates/bytes)
[bytes](https://crates.io/crates/bytes)
is a utility library for working with bytes.


