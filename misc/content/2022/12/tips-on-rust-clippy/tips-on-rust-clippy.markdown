Status: published
Date: 2022-12-28 18:23:37
Modified: 2023-07-04 12:19:27
Author: Benjamin Du
Slug: tips-on-rust-clippy
Title: Tips on Rust Clippy
Category: Computer Science
Tags: Computer Science, programming, Rust, Clippy, lint, check, cargo

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

unused_variables
unused_imports
dead_code

## General Tips

1. Clippy does not support filtering by specific lint directly.
    However,
    it can be achieved via the old rustc flags hack.
    For example,
    you can use the following command 
    to fix only `clippy::collapsible_else_if` lints.

	:::bash
        cargo clippy --fix -- \
	    -A clippy::all -W clippy::collapsible_else_if

    If there are other non-Clippy lint warnings, 
    you can filter out them manually.
    For example,
    if you code still have unfixed `unused_variables` and `dead_code` lints,
    you can filter them out by adding more `-A` options.

	:::bash
        cargo clippy --fix -- \
	    -A unused_variables -A dead_code \
	    -A clippy::all -W clippy::collapsible_else_if

    [Lint Levels](https://doc.rust-lang.org/rustc/lints/levels.html)
    and
    [Lint Groups](https://doc.rust-lang.org/rustc/lints/groups.html)
    are important lint concepts 
    which help you better understand the above trick.

2. Not all lints can be automatically fixed by Clippy.
    If you have a large number of a specific kind of lint 
    which is not automatically fixable by Clippy,
    you can write a Python script 
    to help you fix those issues automatically
    instead of fixing them manually.

## Configuration

[Adding configuration to a lint](https://doc.rust-lang.org/clippy/development/adding_lints.html#adding-configuration-to-a-lint)

## References

- [Most commonly ignored lints](https://github.com/rust-lang/rust-clippy/issues/5418)

- [Rust Clippy Lints](https://rust-lang.github.io/rust-clippy/master/)

- [Lint Levels](https://doc.rust-lang.org/rustc/lints/levels.html)

- [Lint Groups](https://doc.rust-lang.org/rustc/lints/groups.html)

- [Allowed-by-default Lints](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html)

- [Warn-by-default Lints](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html)

- [Deny-by-default Lints](https://doc.rust-lang.org/rustc/lints/listing/deny-by-default.html)

