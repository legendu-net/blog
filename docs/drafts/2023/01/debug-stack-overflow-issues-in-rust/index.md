---
title: Debug Stack Overflow Issues in Rust
created: '2023-01-18T20:30:28-08:00'
date: '2026-11-15T12:20:39-08:00'
authors:
  - bendu
label: debug-stack-overflow-issues-in-rust
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - stack
  - overflow
  - trace
  - backtrace
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The Rust crate
[backtrace-on-stack-overflow](https://crates.io/crates/backtrace-on-stack-overflow)
helps printing the stack backtrace
when your Rust program encounters stack overflow issues.

1. Add
   [backtrace-on-stack-overflow](https://crates.io/crates/backtrace-on-stack-overflow)
   as a dependency into your project.

   ```bash
   cargo add backtrace-on-stack-overflow
   ```

1. Add the line
   `unsafe { backtrace_on_stack_overflow::enable() };`
   into the beginning of your main function.

   ```
    fn main() {
        unsafe { backtrace_on_stack_overflow::enable() };
        /*
           your code ...
        */
    }
   ```

1. Run your project again.
