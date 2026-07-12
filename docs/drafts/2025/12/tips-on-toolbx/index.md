---
title: Tips on Toolbx
created: '2025-12-14T16:59:01+00:00'
date: '2026-07-12T11:52:36-07:00'
authors:
  - bendu
label: tips-on-toolbx
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - toolbx
  - toolbox
  - DistroBox
  - icon
  - Docker
  - image
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

I personally devoted effort on [Docker Images](my-docker-images)
which makes it easy to develop in Docker containers.

- Create a user with same uid/gid as the user on the host on the fly
  so that permissions are handled seamlessly.
- Lots of useful tools are pre-installed and configured.

Toolbx / DistroBox share similarities with my effort on Docker images.
Of course,
Toolbx / DistroBox are superior in many ways.

- Toolbx / DistroBox are NOT based on Docker but rather podman (which is more secure).
- Toolbx / DistroBox have seamless integraito with the host.
  Tools installed in Toolbx / DistroBox feel native.

I've migrated those Docker images to leverage Podman + Toolbx.
See more discussions in
[My Podman Container Images](my-podman-container-images)
.

## General Tips

1. Since the home directory is shared between the host and the container,
   binaries under the home directory (e.g., ~/.local/bin/)
   will be available in the container as well.
   They might just work inside the container.
   For example,
   if you have Claude CLI installed on the host machine (under ~/.local/bin),
   you will be able to use it inside the container as well
   without installing it again inside the container.

1. Information of the running container is stored in `/run/.containerenv` inside the container.

## Different Ways of Running Commands Insdie the Container

```{list-table} Toolbox Command Comparison
---
header-rows: 1
name: toolbox-comparison-table
---
* - Command
  - What it does
  - Best Used For
* - **`toolbox enter`**
  - Drops you into an interactive shell inside the container.
  - Active development, installing packages, or exploring the environment.
* - **`toolbox run`**
  - Runs a single command inside a container, **creating/starting it automatically** if needed.
  - One-off scripts, CI/CD automation, or running an app without "entering".
* - **`toolbox exec`**
  - Runs a single command inside an **already running** container (lower-level native podman wrapper).
  - Background automation or scripts where you know the container is already active.
```

## Toolbox

https://github.com/containers/toolbox

toolbox create --distro ubuntu --release 24.04

## DistroBox

https://github.com/ranfdev/DistroShelf

https://distrobox.it/#quick-start
