---
title: Git Implementations and Bindings in Python
created: '2021-05-02T12:31:26-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: git-implementations-and-bindings-in-python
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Git
  - Python
  - Dulwich
  - pygit2
  - GitPython
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are multiple Git implementations/bindings in Python:
[pygit2](https://github.com/libgit2/pygit2),
[Dulwich](https://github.com/dulwich/dulwich)
and
[GitPython](https://github.com/gitpython-developers/GitPython)
.

Below is a simple comparison of the 3 packages.

|                | pygit2              | dulwich       | GitPython                   |
| -------------- | ------------------- | ------------- | --------------------------- |
| Status         | Active              | Active        | Maintenance mode            |
| Implementation | bindings to libgit2 | pure Python   | bindings to the git command |
| License        | GPLv2               | Apache, GPLv2 | BSD 3                       |
| Feature        | complete            | incomplete    | complete                    |

Overall,
dulwich is recommended.

## References

- [Hands on Dulwich](hands-on-dulwich)
