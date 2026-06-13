---
title: Constraints on Types in Rust
created: '2023-08-29T14:56:50-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: constraints-on-types-in-rust
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - type
  - struct
  - constraint
  - restriction
  - bound
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Ways to Make Sure that a Type in Rust Satisfy Certain Conditions

1. type bounds using the `where` clause

1. disable users from constructing instances of a struct
   and provide initialized instances (with conditions satisfied) for users to use

1. use `assert` to make sure that parameters passed to construction methods satisfy required conditions

1. make construction methods return instances satisfying required conditions

1. Define a sealed trait which representing the required conditions
   and define types implementing the sealed trait.
   Make the struct take a generic parameter implementing the sealed trait.

## Libraries on Type Constraints

### [nutype](https://github.com/greyblake/nutype)

[Nutype](https://github.com/greyblake/nutype)
embraces the simple idea: the type system can be leveraged
to track the fact that something was done, so there is no need to do it again.
If a piece of data was once sanitized and validated
we can rely on the types instead of sanitizing and validating again and again when we're in doubt.

### [validator](https://github.com/Keats/validator)

[Validator](https://github.com/Keats/validator)
provides custom derive to simplify struct validation inspired by marshmallow and Django validators.

## References

- [Trait Bound in Rust](trait-bound-in-rust)
