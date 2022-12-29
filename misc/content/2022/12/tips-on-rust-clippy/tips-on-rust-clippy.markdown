Status: published
Date: 2022-12-28 18:23:37
Modified: 2022-12-28 18:23:37
Author: Benjamin Du
Slug: tips-on-rust-clippy
Title: Tips on Rust Clippy
Category: Computer Science
Tags: Computer Science, programming, Rust, Clippy, lint, check, cargo

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**



    cargo clippy --fix -- -A unused_imports -A unused_variables -A dead_code -A clippy::all -W clippy::collapsible_else_if
    
[Lint Levels](https://doc.rust-lang.org/rustc/lints/levels.html)

[Lint Groups](https://doc.rust-lang.org/rustc/lints/groups.html)

[Allowed-by-default Lints](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html)

[Warn-by-default Lints](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html)

[Deny-by-default Lints](https://doc.rust-lang.org/rustc/lints/listing/deny-by-default.html)

## References

- [Most commonly ignored lints](https://github.com/rust-lang/rust-clippy/issues/5418)
- [Rust Clippy Lints](https://rust-lang.github.io/rust-clippy/master/)

