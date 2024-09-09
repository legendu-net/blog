Status: published
Date: 2023-06-19 23:45:11
Modified: 2023-06-27 23:12:35
Author: Benjamin Du
Slug: const-generic-in-rust
Title: Const Generic in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, const, generic, parameter

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Starting from Rust 1.51,
    [constant generics](https://blog.rust-lang.org/2021/03/25/Rust-1.51.0.html#const-generics-mvp)
    is supported for integral types.

2. The crate 
    [static_assertions](https://crates.io/crates/static_assertions)
    can be used to assert that a const generic parameter satisfy certain conditions at compile time.
    This is an alternative to const bounds using `where`
    before `feature(generic-const-exprs)` is stablized.
    
## Disable Users From Constructing Instances of a Public Struct

1. Make sure the struct has at least one private field
    so that users cannot construct instances directly.
    If all fields of a struct are public,
    just add a dumpy private filed into the struct.
2. Do not privede construction methods or make construction methods as private.

## Sealed Trait

[A definitive guide to sealed traits in Rust](https://predr.ag/blog/definitive-guide-to-sealed-traits-in-rust/)

To disable a trait to be implemented by downstream users,
simply use a marker trait which is not visible to downstream users.

https://rust-lang.github.io/api-guidelines/future-proofing.html#sealed-traits-protect-against-downstream-implementations-c-sealed

## Ways to Make Sure that a Type in Rust Satisfy Certain Conditions

Please refer to
[Constraints on Types in Rust]( https://www.legendu.net/misc/blog/type-constraints-in-rust )
for detailed discussions.

## References

- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/about.html)

- [Const generics MVP hits beta!](https://blog.rust-lang.org/2021/02/26/const-generics-mvp-beta.html)

- [Splitting the const generics features](https://blog.rust-lang.org/inside-rust/2021/09/06/Splitting-const-generics.html)

- [Const generics where-restrictions?](https://internals.rust-lang.org/t/const-generics-where-restrictions/12742)

- [Const Generics - how to ensure that usize const is > 0](https://stackoverflow.com/questions/72582671/const-generics-how-to-ensure-that-usize-const-is-0)

- [Tracking Issue for complex generic constants: feature(generic_const_exprs)](https://github.com/rust-lang/rust/issues/76560)

- [There's currently no way to specify bounds requiring constants in types to be well-formed](https://github.com/rust-lang/rust/issues/68436)
