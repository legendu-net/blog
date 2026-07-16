---
title: Procs Is a Modern Alternative to ps
created: '2026-07-15T21:35:35.874581-07:00'
date: '2026-07-15T21:37:08-07:00'
authors:
  - bendu
label: procs-is-a-modern-alternative-to-ps
license: CC-BY-4.0
tags:
  - procs
  - ps
  - process
  - admin
  - Linux
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```
procs --insert State \
  --or (cat /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/user.slice/libpod-be131b155b6a8ac24cfbafd05aa72c1575512f60dd242b24eec1c3cbb05e543a.scope/container/cgroup.procs)
```
