---
title: Sum Type in Rust
created: '2022-01-15T14:09:38-08:00'
date: '2026-11-15T09:23:06-08:00'
authors:
  - bendu
label: sum-type-in-rust
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - sum
  - type
  - enum
  - either
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Enum is the preferred way to construct a sum type of several types
(which does not implement the same trait).

The Rust crate
[either](https://crates.io/crates/either)
provides an enum `Either` (with variants `Left` and `Right`)
which is a general purpose sum type with two cases.
