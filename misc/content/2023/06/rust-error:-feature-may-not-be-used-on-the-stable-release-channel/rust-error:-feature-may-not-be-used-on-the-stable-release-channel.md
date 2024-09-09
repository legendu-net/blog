Status: published
Date: 2023-06-19 14:15:58
Modified: 2023-06-19 14:15:58
Author: Benjamin Du
Slug: rust-error:-feature-may-not-be-used-on-the-stable-release-channel
Title: Rust Error: error[E0554]: `#![feature]` May Not Be Used on the Stable Release Channel
Category: Computer Science
Tags: Computer Science, programming, Rust, error, E0554, feature, stable, release, channel

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

error[E0554]: `#![feature]` may not be used on the stable release channel
   --> .cargo/registry/src/index.crates.io-6f17d22bba15001f/thiserror-1.0.40/src/lib.rs:239:34
    |
239 | #![cfg_attr(provide_any, feature(provide_any))]
    |                                  ^^^^^^^^^^^

For more information about this error, try `rustc --explain E0554`.
error: could not compile `thiserror` (lib) due to previous error
warning: build failed, waiting for other jobs to finish..

## Solutions

If your Rust project has no dependencies which rely on the nightly version of Rust,
try `cargo clean` (or manually remove the `target` directory)
and then build again.

## References

- [anyhow - issue 250](https://github.com/dtolnay/anyhow/issues/250)
- [error[E0554]: #![feature] may not be used on the stable release channel Couldn't install racer using cargo](https://stackoverflow.com/questions/53136717/errore0554-feature-may-not-be-used-on-the-stable-release-channel-couldnt)
