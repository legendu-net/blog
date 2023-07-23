Status: published
Date: 2023-07-22 11:27:41
Modified: 2023-07-22 22:43:20
Author: Benjamin Du
Slug: the-deref-trait-in-rust
Title: The Deref Trait in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, Trait, Deref, smart pointer

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. In short, 
    do NOT implement the `Deref` trait unless you are absolutely sure that it's needed!
    According to [Rust Official Doc - Deref](https://doc.rust-lang.org/std/ops/trait.Deref.html),
    Deref should only be implemented for smart pointers.
    The Rust Programing Language book has a chapter covering 
    [smart pointers](https://doc.rust-lang.org/book/ch15-00-smart-pointers.html)
    ,
    however,
    the definition is vague.
    In the context of implementing `Deref` for smart pointers,
    smart pointers are types that act like pointers but are not supposed to have methods on their own
    (so ambiguity during method resolution are avoid).
    For example, 
    `Box` implements `Deref` so that you can conveniently use methods of the target type. 
    But if you look at the documentation of `Box`,
    the things you can do with the Box itself, 
    like `Box::leak`,
    are non-method functions. 
    This means that you always have to qualify them, 
    like `Box::leak(my_box)`.

2. If you do implement `Deref<Target = U>` on a type `T`, 
    and it proved necessary to implement a generic trait `Trait<S>` on `T`. 
    Then one should ensure that the implementations of `Trait<S>` 
    for different parameters `S` are not scattered across `T` and `U`.
    Put simply, 
    either `T` or `U` should host all existing `Trait<S>` implementations. 
    Note that the preceding "or" is inclusive, 
    meaning that both `T` and `U` can host some `Trait<S>` implementations, 
    as long as they both host all of them.

## References

- [Rust Official Doc - Deref](https://doc.rust-lang.org/std/ops/trait.Deref.html)

- [Deref Confusion](https://www.fuzzypixelz.com/blog/deref-confusion/)

- [Is Deref bad for caching?](https://www.reddit.com/r/rust/comments/vxfu8c/is_deref_bad_for_caching/)

- [Mistakes with Rust smart pointers: when Deref goes wrong (fuzzypixelz.com)](https://news.ycombinator.com/item?id=36662385)

- [Rust Issue - Deref documentation: Remove references to "smart pointers"](https://github.com/rust-lang/rust/issues/91004)

