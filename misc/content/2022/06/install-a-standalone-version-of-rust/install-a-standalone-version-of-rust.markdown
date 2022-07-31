Status: published
Date: 2022-06-02 15:21:12
Modified: 2022-07-30 21:21:55
Author: Benjamin Du
Slug: install-rust-globally
Title: Install Rust Globally in Linux
Category: Computer Science
Tags: Computer Science, programming, Rust, standalone, Linux, rust-src

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are basically 2 ways to install a global standalone version of Rust in Linux.

## Using a Package Management Tool

Some Linux distributions provide packages for Rust.
Taking Debian/Ubuntu based Linux distributions as an example,
you can install a global version of Rust using the command below.

    :::bash
    wajig install rust rust-src cargo rustfmt 

Notice that the Rust version installed by this way is relatively old. 
Taking Ubuntu 22.04 as example,
the above comamnd installs Rust 1.58.1 
while the latest stable Rust version is 1.61.0 as of May 2022.

## Using Environment Variable + rustup 

By default,
rustup installs Rust locally.
However,
you can configure environment variables to install Rust globally.

    :::bash
    export RUSTUP_HOME=/usr/local/rustup
    export CARGO_HOME=/usr/local/cargo
    export PATH=/usr/local/cargo/bin:$PATH
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

## Manually Install Rust Globally

1. Download Rust.

        :::bash
        curl -sSL https://static.rust-lang.org/dist/rust-1.61.0-x86_64-unknown-linux-gnu.tar.gz -o /tmp/rust.tar.gz

2. Untar the downloaded file.

        :::bash
        tar -zxvf /tmp/rust.tar.gz

3. Go to the untarred directory 
    `rust-1.61.0-x86_64-unknown-linux-gnu`
    and install Rust and necessary components.

        :::bash
        ./install.sh --without=rust-demangler-preview,rls-preview,rust-analysis-x86_64-unknown-linux-gnu

3. Go to the directory
    `/usr/local/lib/rustlib`
    and remove non-needed files.
    You only to keep the 3 directories `etc`, `src` and `x86_64-unknown-linux-gnu`.

        :::bash
        rm -rf !(etc|src|x86_64-unknown-linux-gnu)

4. Download Rust source code.

        :::bash
        curl -sSL https://static.rust-lang.org/dist/rustc-1.61.0-src.tar.gz -o /tmp/rust.tar.gz

5. Untar the downloaded source file into the directory
    `/usr/local/lib/rustlib/src/rust/`
    .

        :::bash
        mkdir -p /usr/local/lib/rustlib/src/rust
        tar -zxvf /tmp/rust.tar.gz -C /usr/local/lib/rustlib/src/rust --strip-components=1

