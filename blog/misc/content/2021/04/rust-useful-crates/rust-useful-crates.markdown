Status: published
Date: 2021-04-09 23:34:03
Author: Benjamin Du
Slug: useful-rust-crates
Title: Useful Rust Crates
Category: Computer Science
Tags: Computer Science, programming, Rust, crate, useful
Modified: 2021-06-09 23:34:03
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://crates.io/crates?sort=downloads

## Databases

### [serde](https://crates.io/crates/serde)
[serde](https://crates.io/crates/serde)
is a framework for serializing and deserializing Rust data structures efficiently and generically.

### [sled](https://github.com/spacejam/sled)
[sled](https://github.com/spacejam/sled)
is an embedded key-value pair databases written in Rust.

### [indradb](https://github.com/indradb/indradb)
[indradb](https://github.com/indradb/indradb)
is a graph database written in rust.

### [oxigraph/](https://github.com/oxigraph/oxigraph/)
[oxigraph/](https://github.com/oxigraph/oxigraph/)
Oxigraph is a graph database implementing the SPARQL standard.
Its goal is to provide a compliant, safe, 
and fast graph database based on the RocksDB and Sled key-value stores. 
It is written in Rust. 
It also provides a set of utility functions for reading, writing, and processing RDF files.
Oxigraph is in heavy development and SPARQL query evaluation has not been optimized yet.

### [bolt-rs](https://github.com/lucis-fluxum/bolt-rs)
[bolt-rs](https://github.com/lucis-fluxum/bolt-rs)
aims to provide a comprehensive set of libraries 
that allow for interaction with graph database servers 
that support the Bolt protocol, namely, Neo4j. 
This set of libraries allows interacting with servers 
supporting versions 1 through 4.1 of the protocol, 
which includes Neo4j 3.1 through 4.2.

### [neo4rs](https://github.com/yehohanan7/neo4rs)
[Neo4rs](https://github.com/yehohanan7/neo4rs)
is a Neo4j rust driver implemented using bolt specification.
This driver is compatible with neo4j 4.x versions

## Numeric Computation

### [num-derive](https://crates.io/crates/num-derive)
[num-derive](https://crates.io/crates/num-derive)
providess procedural macros to derive numeric traits in Rust.

### [num-traits](https://crates.io/crates/num-traits)
[num-traits](https://crates.io/crates/num-traits)
provides numeric traits for generic mathematics in Rust.

### [enum_primitive](https://crates.io/crates/enum_primitive)
[enum_primitive](https://crates.io/crates/enum_primitive)
is a macro to generate `num::FromPrimitive` instances for enum that works in Rust 1.0+.

## Parallell, Concurrency and Async
### [futures](https://crates.io/crates/futures)
[futures](https://crates.io/crates/futures)
is an implementation of futures and streams featuring zero allocations, 
composability, and iterator-like interfaces.
It is a library providing the foundations for asynchronous programming in Rust. 
It includes key trait definitions like Stream, 
as well as utilities like `join!`, `select!`, 
and various futures combinator methods which enable expressive asynchronous control flow.

### [tokio](https://crates.io/crates/tokio)
[tokio](https://crates.io/crates/tokio)
is an event-driven, non-blocking I/O platform for writing asynchronous I/O backed applications.

### [rayon](https://crates.io/crates/rayon)
[rayon](https://crates.io/crates/rayon)
is a data-parallelism library for Rust. 
It is extremely lightweight and makes it easy to convert a sequential computation into a parallel one. 
It also guarantees data-race freedom. 

## Command-line Parsing

### [clap](https://crates.io/crates/clap)
[clap](https://crates.io/crates/clap)
is a simple to use, efficient, and full-featured Command Line Argument Parser.

## File System

### [ripgrep](https://github.com/BurntSushi/ripgrep)
[ripgrep](https://github.com/BurntSushi/ripgrep)
recursively searches directories for a regex pattern while respecting your gitignore.



## Other

### [itertools](https://crates.io/crates/itertools)
[itertools](https://crates.io/crates/itertools)
provides extra iterator adaptors, iterator methods, free functions, and macros.

### [lazy_static](https://crates.io/crates/lazy_static)
[lazy_static](https://crates.io/crates/lazy_static)
is a macro for declaring lazily evaluated statics in Rust.
Using this macro, 
it is possible to have statics that require code to be executed at runtime in order to be initialized. 
This includes anything requiring heap allocations, 
like vectors or hash maps, 
as well as anything that requires non-const function calls to be computed.

### [derive_builder](https://crates.io/crates/derive_builder)
[derive_builder](https://crates.io/crates/derive_builder)
provides a Rust procedural macro to automatically implement the builder pattern for arbitrary structs.

### [bitflags](https://crates.io/crates/bitflags)
[bitflags](https://crates.io/crates/bitflags)
is a Rust macro to generate structures which behave like a set of bitflags.

## References

https://crates.io/

[12 Killer Rust Libraries You Should Know](https://jondot.medium.com/12-killer-rust-libraries-you-should-know-c60bab07624f)

[Awesome Rust](https://github.com/rust-unofficial/awesome-rust)

