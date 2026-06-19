---
title: Tips on Valgrind
created: '2023-01-08T18:58:25-08:00'
date: '2026-06-18T20:12:24-07:00'
authors:
  - bendu
label: tips-on-valgrind
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Valgrind
  - profiling
  - memory
  - CPU
  - memcheck
  - callgrind
  - dhat
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Ubuntu

```sh
sudo apt install valgrind
```

## Installation on Fedora

```sh
sudo dnf install valgrind
```

```{list-table}
---
header-rows: 1
widths: auto
---
* - Valgrind Tool
  - Description
* - callgrind
  - CPU profiling.
* - dhat
  - Dynamic heap analysis.
* - memcheck
  - Check for memory errors (leak, invalid access, etc.).
* - [Massif](https://valgrind.org/docs/manual/ms-manual.html)
  - A heap profiler.
```
