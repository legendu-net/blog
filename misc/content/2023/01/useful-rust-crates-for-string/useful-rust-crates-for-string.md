Status: published
Date: 2023-01-13 15:42:22
Modified: 2023-01-24 20:15:58
Author: Benjamin Du
Slug: useful-rust-crates-for-string
Title: Useful Rust Crates for String
Category: Computer Science
Tags: Computer Science, programming, Rust, string, str, manipulation

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [bstr](https://crates.io/crates/bstr)
[bstr](https://crates.io/crates/bstr)
A string type that is not required to be valid UTF-8.

## [arcstr](https://crates.io/crates/arcstr)
[arcstr](https://crates.io/crates/arcstr)
is a better reference-counted string type, 
with zero-cost (allocation-free) support for string literals, and reference counted substrings.


## [atoi-rs](https://github.com/pacman82/atoi-rs)
[atoi-rs](https://github.com/pacman82/atoi-rs)
parses integers directly from [u8] slices in safe code
.

## [lazy_format](https://crates.io/crates/lazy_format)
[lazy_format](https://crates.io/crates/lazy_format)
is a [no_std] library for lazily formatting things,
which avoids allocating temporary strings 
when writing to a buffered stream. 

## [Askama](https://github.com/djc/askama)
[Askama](https://github.com/djc/askama)
implements a template rendering engine based on Jinja. 
It generates Rust code from your templates at compile time 
based on a user-defined struct to hold the template's context.

## [human_bytes](https://crates.io/crates/human_bytes)
[human_bytes](https://crates.io/crates/human_bytes)
converts bytes into human-readable values.

## [scraper](https://crates.io/crates/scraper)
[scraper](https://crates.io/crates/scraper)
provides HTML parsing and querying with CSS selectors.

## [semver](https://crates.io/crates/semver)
[semver](https://crates.io/crates/semver)
provides parser and evaluator for Cargo's flavor of Semantic Versioning.

## [jetscii](https://github.com/shepmaster/jetscii)
[jetscii](https://github.com/shepmaster/jetscii)
A tiny library to efficiently search strings for sets of ASCII characters 
and byte slices for sets of bytes.

## [fluent-rs](https://github.com/projectfluent/fluent-rs)
[fluent-rs](https://github.com/projectfluent/fluent-rs)
Rust implementation of Fluent 
which is a localization system
for natural-sounding translations.

