Status: published
Date: 2023-01-18 20:30:28
Modified: 2023-01-18 20:30:28
Author: Benjamin Du
Slug: debug-stack-overflow-issues-in-rust
Title: Debug Stack Overflow Issues in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, stack, overflow, trace, backtrace

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The Rust crate
[backtrace-on-stack-overflow](https://crates.io/crates/backtrace-on-stack-overflow)
helps printing the stack backtrace 
when your Rust program encounters stack overflow issues.

1. Add
    [backtrace-on-stack-overflow](https://crates.io/crates/backtrace-on-stack-overflow)
    as a dependency into your project.

        :::bash
        cargo add backtrace-on-stack-overflow

2. Add the line 
    `unsafe { backtrace_on_stack_overflow::enable() };`
    into the beginning of your main function.

        
        fn main() {
            unsafe { backtrace_on_stack_overflow::enable() };
            /*
               your code ...
            */
        }

3. Run your project again.
