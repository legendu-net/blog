Status: published
Date: 2021-12-04 17:41:10
Modified: 2023-01-13 17:30:22
Author: Benjamin Du
Slug: speed-up-rust-build-with-cache
Title: Speed Up Rust Build With Cache
Category: Computer Science
Tags: Computer Science, programming, Rust, build, cache, Cargo, Cachepot, Rust Cache

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The article
[How to alleviate the pain of Rust compile times](https://vfoley.xyz/rust-compile-speed-tips/)
has a good summary on ways to speed up compilation of Rust projects.

## Tips and Traps

1. The best tool to cache the compiling of a Rust application
    is to use sccache
    [sccache](https://github.com/mozilla/sccache)
    .
    [cachepot](https://github.com/paritytech/cachepot)
    is another such good tool.
    It is essentially sccache with extra security. 

2. [sccache](https://github.com/mozilla/sccache)
    can be used in a Jupyter/Lab notebook with the evcxr kernel as well.
    Just specify the command `:sccache 1`
    to enable compilation cache using sccache.

3. The 
    [cargo-cache](https://crates.io/crates/cargo-cache)
    tool 
    is useful for managing compilation cache of Rust applications. 

4. [actions/rust-cache](https://github.com/marketplace/actions/rust-cache)
    is a GitHub Action that implements smart caching 
    for rust/cargo projects with sensible defaults.

## References

- [Improve Rust compile times with sccache](https://www.bitfalter.com/rust-development-environment-improvements)

- [Speed up Rust Builds with Cachepot](https://kflansburg.com/posts/rust-cachepot/)

- [cachepot](https://github.com/paritytech/cachepot)

- [cargo-cache](https://crates.io/crates/cargo-cache)

- [actions/rust-cache @ GitHub](https://github.com/marketplace/actions/rust-cache)

- [Is coding in Rust as bad as in C++?](https://quick-lint-js.com/blog/cpp-vs-rust-build-times/)

- [Optimizing the Rust build](https://quick-lint-js.com/blog/cpp-vs-rust-build-times/#optimizing-rust-build)

