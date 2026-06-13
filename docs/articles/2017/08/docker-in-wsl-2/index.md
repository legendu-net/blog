---
title: Docker in WSL 2
created: '2017-08-10T09:05:45-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: docker-in-wsl-2
license: CC-BY-4.0
tags:
  - software
  - Docker
  - WSL
  - WSL 2
  - Windows
  - Bash
  - BashOnWindows
  - Bash on Windows
---

## Tips and Traps

1. Docker on WSL 2 works great.
   However,
   the performance of IO is extremely bad if it access the Windows filesystem.
   For more discussions,
   please refer to
   [WSL 2 Filesystem](wsl2-filesystem)
   .

1. Docker containers launched from a WSL (e.g., Ubuntu) shell will continue to run
   after the WSL shell is terminated,
   as long as the Docker daemon is alive.
   As a matter of fact,
   a WSL 2 shell is not must to start the Docker daemon (back by WSL 2) or to launch Docker containers.

## Install Docker in WSL 2

1. Install WSL 2 following instructions in
   [Tips on WSL 2](tips-on-wsl-2)
   .

1. Install `docker.io` in WSL 2.

   ```
    :::bash
    sudo apt-get install docker.io
   ```

1. Install Docker desktop for Windows.

1. Set Docker to use WSL 2 based engine.

   1. Open Docker desktop settings.
   1. Check the checkbox "Use the WSL 2 based engine" in the general tab.
   1. Click "Apply & Restart".

   ![docker-wsl2-engine](https://docs.docker.com/desktop/windows/images/wsl2-enable.png)

For more details,
please refer to
[Docker Desktop WSL 2 backend](https://docs.docker.com/docker-for-windows/wsl/)
.

## References

- [Tips on WSL 2](tips-on-wsl-2)

- [How to Boost Docker with WSL2](https://towardsdatascience.com/how-to-improve-docker-performance-with-wsl2-3a54402ab0f2)

- https://towardsdatascience.com/dual-boot-is-dead-windows-and-linux-are-now-one-27555902a128
