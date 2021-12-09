Status: published
Date: 2021-10-25 19:57:05
Modified: 2021-12-05 13:01:57
Author: Benjamin Du
Slug: tips-on-rustfmt
Title: Tips on Rustfmt
Category: Computer Science
Tags: Computer Science, programming, Rust, format, rustfmt, formating code, code formating

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[Configuring Rustfmt](https://rust-lang.github.io/rustfmt/?version=master&search=)

    :::toml
    tab_spaces = 4
    max_width = 90
    chain_width = 70
    newline_style = "unix"
    use_field_init_shorthand = true
    use_small_heuristics = "Max"

## References

https://github.com/rust-lang/rustfmt