---
title: Run Docker Containers inside a Docker Container
created: '2021-09-13T10:55:29-07:00'
date: '2026-08-11T22:39:32-07:00'
authors:
  - bendu
label: run-docker-containers-inside-a-docker-container
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Docker
  - container
  - socks
  - container in container
---

You can run Docker containers inside a Docker container.
To allow this,
you have to pass the docker socks into the container
using the option `-v /var/run/docker.sock:/var/run/docker.sock`.
For more discussions,
please refer to
[How To Run Docker in Docker Container [3 Easy Methods]](https://devopscube.com/run-docker-in-docker/#:~:text=To%20run%20docker%20inside%20docker,sock%20as%20a%20volume.&text=Just%20a%20word%20of%20caution,privileges%20over%20your%20docker%20daemon)
.
However,
be aware of potential security issues
as this essentially gives root access of the host system to the Docker container.

## References

- [How To Run Docker in Docker Container [3 Easy Methods]](https://devopscube.com/run-docker-in-docker/#:~:text=To%20run%20docker%20inside%20docker,sock%20as%20a%20volume.&text=Just%20a%20word%20of%20caution,privileges%20over%20your%20docker%20daemon)
