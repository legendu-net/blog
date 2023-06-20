Status: published
Date: 2023-06-19 23:45:11
Modified: 2023-06-19 23:45:11
Author: Benjamin Du
Slug: const-generic-in-rust
Title: Const Generic in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, const, generic, parameter

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Starting from Rust 1.51, constant generics support integers, booleans, and enums, but not floating-point numbers.

2. The crate 
    [static_assertions](https://crates.io/crates/static_assertions)
    can be used to assert that a const generic parameter satisfy certain conditions at compile time.
    This is an alternative to const bounds using `where`
    before the `feature(generic-const-exprs)` is stablized.

If you want to define a generic type parameter that represents a usize value greater than 2, 
you can use a combination of trait bounds and associated types. 
Below is such an example.
You can achieve the same using a const Enum as the generic parameter.
```
trait GreaterThanTwo {
    const VALUE: usize;
}

struct MyStruct<T: GreaterThanTwo> {
    // Your struct fields here
}

impl<T: GreaterThanTwo> MyStruct<T> {
    fn new() -> Self {
        // Create and return an instance of MyStruct
        Self {
            // Initialize your struct fields here
        }
    }
}

impl GreaterThanTwo for const { 3 } {
    const VALUE: usize = 3;
}

fn main() {
    let my_struct: MyStruct = MyStruct::new();
    // Use my_struct and perform other operations
}
```

## References

- [Splitting the const generics features](https://blog.rust-lang.org/inside-rust/2021/09/06/Splitting-const-generics.html)

- [Const generics where-restrictions?](https://internals.rust-lang.org/t/const-generics-where-restrictions/12742)

- [Const Generics - how to ensure that usize const is > 0](https://stackoverflow.com/questions/72582671/const-generics-how-to-ensure-that-usize-const-is-0)

- [Tracking Issue for complex generic constants: feature(generic_const_exprs)](https://github.com/rust-lang/rust/issues/76560)

- [There's currently no way to specify bounds requiring constants in types to be well-formed](https://github.com/rust-lang/rust/issues/68436)
