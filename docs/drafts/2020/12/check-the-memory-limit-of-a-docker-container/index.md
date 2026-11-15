---
title: Check the Memory Limit of a Docker Container
created: '2020-12-19T11:39:17-08:00'
date: '2026-11-15T09:25:40-08:00'
authors:
  - bendu
label: check-the-memory-limit-of-a-docker-container
license: CC-BY-4.0
tags:
  - computer science
  - Docker
  - container
  - memory limit
  - cgroup
  - cgget
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Docker 1.13+

Docker 1.13+ mounts the container's cgroup to /sys/fs/cgroup (this could change in future versions).
You can check the limit using

```bash
cat /sys/fs/cgroup/memory/memory.limit_in_bytes
```

## Older Version of Docker

1. Install [cgroup-tools](https://github.com/mk-fg/cgroup-tools).

   ```bash
   sudo apt update
   sudo apt install cgroup-tools
   ```

1. Query the memory limit of the Docker container.

   ```bash
   cgget -n --values-only --variable memory.limit_in_bytes /
   ```

Notice that if a memory limit is not,
both of the above methods will return a extremely large number.
So to be safe,
you'd take the minimum value before the above result and the memory of the host
which can be get from the file `/proc/memoinfo`.

## References

https://stackoverflow.com/questions/42187085/check-mem-limit-within-a-docker-container
