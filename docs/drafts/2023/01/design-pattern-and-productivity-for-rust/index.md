---
title: Design Pattern and Productivity for Rust
created: '2023-01-13T16:29:29-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: design-pattern-and-productivity-for-rust
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - design
  - pattern
  - productivity
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [derive_more](https://crates.io/crates/derive_more)

[derive_more](https://crates.io/crates/derive_more)
adds \`\`#[derive(x)]\` macros for more traits.

## [derive_builder](https://crates.io/crates/derive_builder)

[derive_builder](https://crates.io/crates/derive_builder)
provides Rust macro to automatically implement the builder pattern for arbitrary structs.
A simple `#[derive(Builder)]` will generate a FooBuilder for your struct Foo
with all setter-methods and a build method.

## [derive-adhoc](https://crates.io/crates/derive-adhoc)

[derive-adhoc](https://crates.io/crates/derive-adhoc)
allows you to write macros
which are driven by Rust data structures,
just like proc macro derive macros,
but without having to wrestle with the proc macro system.

## [bon](https://github.com/elastio/bon)

[bon](https://github.com/elastio/bon)
is a Rust crate for generating compile-time-checked builders for functions and structs.

## Design Patterns

[Improve your Rust APIs with the type state pattern](https://www.youtube.com/watch?v=_ccDqRTx-JU)

## Constraints on Types

Please refer to
[Constraints on Types in Rust](constraints-on-types-in-rust)
for detailed discussions.

## References

- [Pointer, Reference and Ownership in Rust](pointer-reference-and-ownership-in-rust)

- [After NLL: Interprocedural conflicts](http://smallcultfollowing.com/babysteps/blog/2018/11/01/after-nll-interprocedural-conflicts/)

- [Shared Mutability in Rust](https://medium.com/swlh/shared-mutability-in-rust-part-1-of-3-21dc9803c623)

- [Tips on Code Design](tips-on-code-design)
