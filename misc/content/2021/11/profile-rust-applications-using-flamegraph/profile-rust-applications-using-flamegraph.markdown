Status: published
Date: 2021-11-09 10:28:40
Modified: 2022-01-13 13:28:01
Author: Benjamin Du
Slug: profile-rust-applications-using-flamegraph
Title: Profile Rust Applications Using Flamegraph
Category: Computer Science
Tags: Computer Science, programming, Rust, flamegraph, perf, profile, profiling

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Ubuntu
```
wajig update 
wajig install linux-tools-common linux-tools-generic linux-tools-`uname -r`
cargo install flamegraph
```

## Usage

Run the following command to generate a SVG visualization of performance profiling.

    :::bash
    cargo flamegraph

If `sudo` permission is needed, 
then add the `--sudo` option.

    :::bash
    cargo flamegraph --sudo

If you encounter issues 
(see 
[#62](https://github.com/flamegraph-rs/flamegraph/issues/62)
and
[#159](https://github.com/flamegraph-rs/flamegraph/issues/159)
) with the above commands,
you can try run the `flamegraph` on rust binary directly.

    :::bash
    sudo ~/.cargo/bin/flamegraph target/release/your_binary

Notice that it is best to

1. Start a Docker container with the option `--cap-add SYS_ADMIN`
    if you use `flamegraph` in a Docker container.
    For more discussions,
    please refer to
    [running `perf` in docker & kubernetes](https://medium.com/@geekidea_81313/running-perf-in-docker-kubernetes-7eb878afcd42)
    .

1. Enable debug info (if you are profiling the release build which is the default).
    You can achive this by adding the following configuration into your `Cargo.toml` file.

        [profile.release]
        debug = true

2. View the generated SVG file using a browser (e.g., Chrome)
    instead of using a image viewer app.

## perf

[Running `perf` in docker & kubernetes](https://medium.com/@geekidea_81313/running-perf-in-docker-kubernetes-7eb878afcd42)

[Security implications of changing “perf_event_paranoid”](https://unix.stackexchange.com/questions/519070/security-implications-of-changing-perf-event-paranoid)

[Run perf without root-rights](https://superuser.com/questions/980632/run-perf-without-root-rights)

[Flamegraph shows every caller is [unknown]?](https://users.rust-lang.org/t/flamegraph-shows-every-caller-is-unknown/52408)
echo 0 |sudo tee /proc/sys/kernel/kptr_restrict

## References

- [Profile Rust Applications](http://www.legendu.net/misc/blog/profile-rust-applications/)

- [flamegraph](https://github.com/flamegraph-rs/flamegraph)
