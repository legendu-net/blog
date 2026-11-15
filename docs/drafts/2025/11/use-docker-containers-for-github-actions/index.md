---
title: Use Docker Containers for GitHub Actions
created: '2025-11-23T10:57:08-08:00'
date: '2026-11-15T09:28:25-08:00'
authors:
  - bendu
label: use-docker-containers-for-github-actions
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - GitHub Actions
  - CICD
  - development
  - Docker
  - container
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips & Traps

1. Docker container is available in Ubuntu and Windows but not macOS in GitHub Actions due to license issues.
   To use Docker in macOS in GitHub Actions,
   you have to install it manually.
   Please refer to
   [Is it possible to install and configure Docker on MacOS runner?](https://github.community/t/is-it-possible-to-install-and-configure-docker-on-macos-runner/16981)
   for more details.

1. The `runner` account (even with `sudo`) in GitHub Actions VMs
   have restricted privileges.
   For example,
   the Linux perf (and equivalent) tools cannot be run in GitHub Actions VMs
   even if `sudo` is used.
   Docker containers running in GitHub Actions VMs are restricted too.
   For more details,
   please refer to
   [Supported Linux capabilities](https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions#supported-linux-capabilities)
   .

## Examples

- [fun-poker-game/poker-rs - profiling.yml](https://github.com/fun-poker-game/poker-rs/blob/dev/.github/workflows/profiling.yml)

- [fun-poker-game/poker-rs - pre-release_centos7.yml](https://github.com/fun-poker-game/poker-rs/blob/dev/.github/workflows/pre-release_centos7.yml)

- [fun-poker-game/poker-rs - on_merge.yml](https://github.com/fun-poker-game/poker-rs/blob/dev/.github/workflows/on_merge.yml)

- [fun-poker-game/poker-rs - lint.yml](https://github.com/fun-poker-game/poker-rs/blob/dev/.github/workflows/lint.yml)

- [fun-poker-game/poker-rs - bench_on_pr.yml](https://github.com/fun-poker-game/poker-rs/blob/dev/.github/workflows/bench_on_pr.yml)

- [legendu-net/aiutil - lint.yml](https://github.com/legendu-net/aiutil/blob/dev/.github/workflows/lint.yml)
