Status: published
Date: 2019-04-10 12:17:46
Modified: 2022-11-23 19:03:53
Author: Benjamin Du
Slug: rust-tips
Title: Tips on Rust
Category: Computer Science
Tags: programming, Rust, tips, Cargo, rustup

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation 

Please refer to
[Tips on rustup](http://www.legendu.net/misc/blog/tips-on-rustup)
for installing Rust using rustup (the recommended way for most users),
and
[Install a Standalone Version of Rust in Linux](https://www.legendu.net/misc/blog/install-a-standalone-version-of-rust)
for installing a global standalone version of Rust.

### Install a Newer Version of Rust via PPA on Ubuntu

    :::bash
    sudo apt-add-repository ppa:ubuntu-mozilla-security/rust-updates
    sudo apt-get update
    sudo apt-get install rustc

For details of the PPA ubuntu-mozilla-security/rust-updates,
please refer to
[PPA for preparing rust toolchain updates for Firefox](https://launchpad.net/~ubuntu-mozilla-security/+archive/ubuntu/rust-updates)
.

## Rust Toolchains

- [cargo](http://www.legendu.net/misc/blog/tips-on-cargo): package manager for Rust

- rustup: version manager for Rust

- [rustc](http://www.legendu.net/misc/blog/tips-on-rustc): compiler for Rust

- clippy

- rustfmt

## Conditional Compilation in Rust 

https://users.rust-lang.org/t/conditional-compilation-for-debug-release/1098
Conditional compilation for debug/release

    :::bash
    #[cfg(debug_assertions)]
    ...

## Key Concepts in Rust

[Moves, copies and clones in Rust](https://hashrust.com/blog/moves-copies-and-clones-in-rust/)

## General Tips and Traps

1. [Common newbie mistakes or bad practices](https://users.rust-lang.org/t/common-newbie-mistakes-or-bad-practices/64821)
    [Common Newbie Mistakes and Bad Practices in Rust: Bad Habits](https://adventures.michaelfbryan.com/posts/rust-best-practices/bad-habits/)

2. `Iterator::for_each` is preferred over a `for` loop;
    `Range` (`..`) is preferred over `RangeInclusive` (`..=`).
    For detailed discussions,
    please refer to
    [Big performance problem with closed intervals looping #45222](https://github.com/rust-lang/rust/issues/45222)
    ,
    [Performance difference among Range, RangeInclusive and reversed](https://users.rust-lang.org/t/performance-difference-among-range-rangeinclusive-and-reversed/20283)
    ,
    [Why is iterator so much faster?](https://www.reddit.com/r/rust/comments/eiwhkn/why_is_iterator_so_much_faster/)
    and
    [Why does iteration over an inclusive range generate longer assembly in Rust?](https://stackoverflow.com/questions/70672533/why-does-iteration-over-an-inclusive-range-generate-longer-assembly-in-rust)
    .

## Pattern Matching
Pattern matching 

https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html#matching-named-variables

## Popular Rust Libraries

Please refer to 
[Useful Rust Crates](http://www.legendu.net/misc/blog/useful-rust-crates)
for detailed discussions.

## Machine Learning

Please refer to
[Rust for Machine Learning](http://www.legendu.net/misc/blog/rust-for-machine-learning)
for detailed discussions.

## Parallel, Multithreading and Concurrency in Rust

### [loom](https://github.com/tokio-rs/loom)
is a concurrency permutation testing tool for Rust.

### [sanitizers](https://github.com/google/sanitizers)
This project is the home for Sanitizers: AddressSanitizer, MemorySanitizer, ThreadSanitizer, LeakSanitizer, 
and more The actual code resides in the LLVM repository. Here we keep extended documentation, bugfixes and some helper code.



[rayon](https://github.com/rayon-rs/rayon)
A data parallelism library for Rust.

http://worthe-it.co.za/programming/2018/10/03/going-four-times-faster-with-multithreading.html

https://skipworth.io/posts/rust-wc-threads/

https://crates.io/crates/scoped-threadpool

## [Rust GUI](http://www.legendu.net/misc/blog/develop-a-gui-application-in-rust)

## Optimize Compiling of Rust Projects

[Fast Rust Builds](https://matklad.github.io/2021/09/04/fast-rust-builds.html)
has a detailed discuss on how to optimize the compiling time of rust projects.

## Cool Rust Projects

https://github.com/rajasekarv/native_spark

https://github.com/andygrove/ballista

https://github.com/weld-project/weld

https://github.com/rbatis/rbatis

https://github.com/dclong?language=rust&tab=stars

https://github.com/rust-unofficial/awesome-rust

https://github.com/yewstack/yew

https://github.com/valeriansaliou/sonic

## Tutorials

[Rust Language Cheat Sheet](https://cheats.rs/)

[How to learn modern Rust](https://github.com/joaocarvalhoopen/How_to_learn_modern_Rust)

[Jon Gjengset's Video Tutorials (Medium to Advanced)](https://www.youtube.com/channel/UC_iD0xppBwwsrM9DegC5cQQ)

[Rust on YouTube](https://www.youtube.com/channel/UCaYhcUwRBNscFNUKTjgPFiA)

[Rust Crash Course | Rustlang](https://www.youtube.com/watch?v=zF34dRivLOw)

https://github.com/rust-unofficial/awesome-rust

https://kerkour.com/

## References

- [12 Rust Tips and Tricks you might not know yet](https://federicoterzi.com/blog/12-rust-tips-and-tricks-you-might-not-know-yet/)

- [Rust Programming Language Users Forum](https://users.rust-lang.org/)

- [Rust Reference](https://doc.rust-lang.org/stable/reference/)

- [Rust Language Cheat Sheet](https://cheats.rs/)

- [The Rust Programming Language](https://doc.rust-lang.org/book/title-page.html)

- [The Rustonomicon : The Dark Arts of Unsafe Rust](https://doc.rust-lang.org/nomicon/)

- [Are we async yet?](https://areweasyncyet.rs/)

- [The Rust Standard Library](https://doc.rust-lang.org/stable/std/)

- [Rust Blog](https://blog.rust-lang.org/)

- [Rust Compiler Explorer](https://rust.godbolt.org/)

- https://users.rust-lang.org/

- https://internals.rust-lang.org/

- https://play.rust-lang.org/

- [Are We Web Yet](http://www.arewewebyet.org/)

- [Are we game yet?](https://arewegameyet.rss)

- [The Best Rust Frameworks to Check out in 2019](https://blog.logrocket.com/the-best-rust-frameworks-to-check-out-in-2019/)

- [InfinyOn Blog](https://www.infinyon.com/blog/)
