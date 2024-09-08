Status: published
Date: 2023-06-12 20:54:23
Modified: 2023-06-12 20:54:23
Author: Benjamin Du
Slug: cargo-build-script-add-wings-to-cargo-build
Title: Cargo Build Script Add Wings to Cargo Build
Category: Computer Science
Tags: Computer Science, programming, Rust, cargo, build, script, build.rs

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. `build.rs` is located in the root directory of the project.

2. `build.rs` can be used to directly generate a module
    or generate some Rust code to be included in another Rust file using the macro `include!`.

3. Environment variables for `build.rs` can be configured in `.cargo/config.toml`.

## References

- [Generating static arrays during compile time in Rust](https://dev.to/rustyoctopus/generating-static-arrays-during-compile-time-in-rust-10d8)

- [Automatically Generate Rust Modules With Cargo Build Scripts](https://dev.to/deciduously/automatically-generate-rust-modules-with-cargo-build-scripts-157h)

- [include! macro in rust](https://www.sudipg.com.np/posts/include-macro-rust/)

- [Macro std::include](https://doc.rust-lang.org/std/macro.include.html)

- [Rust Official Doc - Build Script](https://doc.rust-lang.org/cargo/reference/build-scripts.html)
