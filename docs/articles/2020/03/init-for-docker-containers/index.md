---
title: Init for Docker Containers
created: '2020-03-05T11:08:32-08:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: init-for-docker-containers
license: CC-BY-4.0
tags:
  - software
  - Docker
  - container
  - init
  - s6
  - s6-overlay
  - tini
  - Supervisord
  - dumb-init
---

## Built-in Support

Docker has built-in support for init process (which is based on tini) now.
In short,
you just have to specify the option `--init`
when you start a container using `docker run`.
For more details,
please refer to
[Specify an init process](https://docs.docker.com/engine/reference/run/#specify-an-init-process)
.

## Old Approaches

The article [Choosing an init process for multi-process containers](https://ahmet.im/blog/minimal-init-process-for-containers/)
has very detailed comparisons among different init options.
[s6](https://skarnet.org/software/s6/) is recommended as thee best init for Docker.
The [s6-overlay-builder](https://github.com/just-containers/s6-overlay)
project is a series of init scripts and utilities to ease creating Docker images using s6 as a process supervisor.

## References

- https://docs.docker.com/engine/reference/commandline/run/

- https://github.com/krallin/tini

- [Supervisor with Docker: Lessons learned](https://advancedweb.hu/supervisor-with-docker-lessons-learned/)
