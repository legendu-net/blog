Status: published
Date: 2023-02-02 17:21:12
Modified: 2023-07-05 10:29:05
Author: Benjamin Du
Slug: cell-and-refcell-in-rust
Title: Cell and RefCell in Rust
Category: Computer Science
Tags: Computer Science, programming, Cell, RefCell, borrow checker, interior mutability

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**



https://doc.rust-lang.org/std/cell/

https://doc.rust-lang.org/std/cell/struct.RefCell.html

[Rust Cell and RefCell](https://blog.iany.me/2019/02/rust-cell-and-refcell/)

Rc + RefCell is another alternative to circumvent Rust's borrow checker at compile time.
Checks at runtime and might might panic if there are borrowing issues in your code.

comes at a performance penalty as it is slower to track borrowing at runtime.

1. Avoid use Cell and RefCell 
    unless you have to rely on them to circumvent Rust's borrow checker at compile time.

## References

- [Cell and RefCell](https://subscription.packtpub.com/book/programming/9781789616705/6/ch06lvl1sec44/cell-and-refcell)

