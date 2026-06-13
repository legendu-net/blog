---
title: Profile Rust Applications Using Flamegraph
created: '2021-11-09T10:28:40-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: profile-rust-applications-using-flamegraph
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - FlameGraph
  - perf
  - profile
  - profiling
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Traps

1. [not-perf](https://github.com/koute/not-perf)
   is the best CPU profiling tool for Rust application.

1. [Valgrind](cpu-profiling-of-rust-applications-using-valgrind)
   is another good alternative to flamegraph
   if performance is not a big issue.
   However,
   profiling an application using valgrind is about 50-200 times slower than running the application,
   so it might not be a good option for long-running applications.
   [not-perf](https://github.com/koute/not-perf)
   is a better alternative in this case.

1. It is suggested that you use Flamegraph in a virtual machine (via multipass) or a Docker container.
   This is because Flamegraph relies on `perf` which require sudo permission to install and configure,
   which is easier and safer to do in an isolated environment.
   If you use a Docker container,
   <span style="color:red">
   make sure that the Docker image is compatible with the Linux kernel on the host machine
   </span>
   !
   Otherwise,
   you will either fail to install `perf`
   or install a non-compatible one.
   Generally speaking,
   it is a good choice to run a Ubuntu Docker container
   on a Ubunut host machine
   with matching releasing versions.

1. You have to configure `perf_event_paranoid` to be `-1`.
   This can be done by manually setting the value in the file
   `/proc/sys/kernel/perf_event_paranoid`
   to be `-1`.
   Or equivalently,
   you can run the following command

   ```bash
   sudo sysctl -w kernel.perf_event_paranoid=-1
   ```

   Changes made by the above approaches are temporary.
   To persist the above setting,
   you can add a line `kernel.perf_event_paranoid = -1`
   into the file `/etc/sysctl.conf`
   .
   You can of course edit the file manually.
   Below is a comamnd for doing this (and applying changes) automatically.

   ```sh
   sudo $(which uvx) --from aiutil etc_sysctl kernel.perf_event_paranoid -1 --apply
   ```

   If you work in a Docker environemnt,
   you have to

   1. Configure `kernel.perf_event_paranoid = -1` on the host machine.
   1. Configure `kernel.perf_event_paranoid = -1` in the Docker image.
   1. Launch a Docker container with the right permission.

   [dclong/vscode-server](https://github.com/legendu-net/docker/tree/dev/docker-vscode-server)
   is such a Docker image that is properly configure.
   And if you launch it using `ldc dclong/vscode-server -dm`,
   the permission is handle properly
   given that `kernel.perf_event_paranoid = -1` is configured on the host machine.
   See
   [Start a Container using ldc](start-a-container-using-ldc)
   for detailed discussions.

## Installation on Debian

```
sudo apt update
sudo apt install linux-perf
cargo install flamegraph
```

## Installation on Ubuntu

```
sudo apt update 
sudo apt install linux-tools-common linux-tools-generic linux-tools-`uname -r`
cargo install flamegraph
```

## Usage

Run the following command to generate a SVG visualization of performance profiling.

```bash
cargo flamegraph
```

If `sudo` permission is needed,
then add the `--sudo` option.

```bash
cargo flamegraph --sudo
```

If you encounter issues
(see
[#62](https://github.com/flamegraph-rs/flamegraph/issues/62)
and
[#159](https://github.com/flamegraph-rs/flamegraph/issues/159)
) with the above commands,
you can try run the `flamegraph` on rust binary directly.

```bash
sudo ~/.cargo/bin/flamegraph -- target/release/your_binary [options]
```

Notice that it is best to

1. Start a Docker container with the option `--cap-add SYS_ADMIN`
   if you use `flamegraph` in a Docker container.
   For more discussions,
   please refer to
   [running `perf` in docker & kubernetes](https://medium.com/@geekidea_81313/running-perf-in-docker-kubernetes-7eb878afcd42)
   .

1. Enable debug info (if you are profiling the release build which is the default).
   You can achive this by adding the following configuration into your `Cargo.toml` file.

   ```
    [profile.release]
    debug = true
   ```

1. View the generated SVG file using a browser (e.g., Chrome)
   instead of using a image viewer app.

## perf

[Running `perf` in docker & kubernetes](https://medium.com/@geekidea_81313/running-perf-in-docker-kubernetes-7eb878afcd42)

[Security implications of changing “perf_event_paranoid”](https://unix.stackexchange.com/questions/519070/security-implications-of-changing-perf-event-paranoid)

[Run perf without root-rights](https://superuser.com/questions/980632/run-perf-without-root-rights)

[Flamegraph shows every caller is [unknown]?](https://users.rust-lang.org/t/flamegraph-shows-every-caller-is-unknown/52408)
echo 0 |sudo tee /proc/sys/kernel/kptr_restrict

## References

- [Profile Rust Applications](profile-rust-applications)

- [Profile Rust Applications Using Valgrind](cpu-profiling-of-rust-applications-using-valgrind)

- [flamegraph](https://github.com/flamegraph-rs/flamegraph)

- [Is it possible to print the callgraph of a Cargo workspace?](https://users.rust-lang.org/t/is-it-possible-to-print-the-callgraph-of-a-cargo-workspace/50369)

- [2022-03-20 – Dealing with slow `perf script` on Debian](https://michcioperz.com/post/slow-perf-script/)
