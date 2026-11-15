---
title: The Non-Zero Exit Code 137 While Building a Docker Image
created: '2019-10-18T17:56:29-07:00'
date: '2026-11-15T09:21:55-08:00'
authors:
  - bendu
label: the-non-zero-exit-code-137-while-building-a-docker-image
license: CC-BY-4.0
tags:
  - software
  - Docker
  - exit code
  - '137'
  - OOM
  - out-of-memory
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

According to
[Container exits with non-zero exit code 137](https://success.docker.com/article/what-causes-a-container-to-exit-with-code-137),
there are 2 possible reasons that have caused this.

1. The container received a docker stop,
   and the application did not gracefully handle SIGTERM (kill -15) — whenever a SIGTERM has been issued,
   the docker daemon waits 10 seconds then issue a SIGKILL (kill -9) to guarantee the shutdown.

1. The application hit an out-of-memory (OOM) condition.

Since the exit code happened during the building of a Docker image,
it means that there is an out-of-meory (OOM) error happened.
You can try building your Docker image using a machine with a larger memory.
Notice that if you are running Docker in a VM (e.g., via Docker Machine or Docker for Mac),
you can increase the memory limit to the VM.
For example,
if you are building Docker images on Mac,
follow the instructions below to increase the memory limit for Docker.

1. Click on the whale icon of Docker.

1. Click on "Preferences..." in pop-up menu.

1. Click on the "Advanced" Tab.

1. Increase memory and swap to the desired amount.

## References

https://stackoverflow.com/questions/45363771/docker-build-from-dockerfile-with-more-memory
