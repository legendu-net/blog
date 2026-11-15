---
title: Tips on Rustfmt
created: '2021-10-25T19:57:05-07:00'
date: '2026-11-15T09:22:21-08:00'
authors:
  - bendu
label: tips-on-rustfmt
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - format
  - rustfmt
  - formatting code
  - code formatting
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[Configuring Rustfmt](https://rust-lang.github.io/rustfmt/?version=master&search=)

```
:::toml
tab_spaces = 4
max_width = 90
chain_width = 70
newline_style = "unix"
use_field_init_shorthand = true
use_small_heuristics = "Max"
```

## References

https://github.com/rust-lang/rustfmt
