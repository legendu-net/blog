Status: published
Date: 2019-10-28 15:27:01
Author: Benjamin Du
Slug: the-non-zero-exit-code-137-while-building-a-docker-image
Title: the Non-Zero Exit Code 137 While Building a Docker Image
Category: Software
Tags: software, Docker, exit code, 137, OOM, out-of-memory

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

According to
[Container exits with non-zero exit code 137](https://success.docker.com/article/what-causes-a-container-to-exit-with-code-137),
there are 2 possible reasons that have caused this.
Since the exit code happened during the building of a Docker image,
it means that there is an out-of-meory (OOM) error happend.
You can try building your Docker image using a machine with a larger memory.

1. The container received a docker stop,
    and the application did not gracefully handle SIGTERM (kill -15) — whenever a SIGTERM has been issued,
    the docker daemon waits 10 seconds then issue a SIGKILL (kill -9) to guarantee the shutdown.

2. The application hit an out-of-memory (OOM) condition.

