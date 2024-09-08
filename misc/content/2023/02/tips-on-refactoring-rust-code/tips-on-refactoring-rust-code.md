Status: published
Date: 2023-02-02 14:15:04
Modified: 2023-02-02 14:15:04
Author: Benjamin Du
Slug: tips-on-refactoring-rust-code
Title: Tips on Refactoring Rust Code
Category: Computer Science
Tags: Computer Science, programming, Rust, code, refactor, 

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://rust-analyzer.github.io/manual.html#structural-search-and-replace


cargo clippy fix

## General Approach for Auto Refactoring

1. use `cargo build` or `cargo clippy` to generate error msgs for a specific kind of issue
2. for each line of error (best to do it backwards), identify the place that need updates
3. update the code
4. iterate 1-3 multiple times until all issues are fixed


