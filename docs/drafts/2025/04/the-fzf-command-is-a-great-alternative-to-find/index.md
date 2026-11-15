---
title: The fzf Command Is a Great Alternative to find
created: '2025-04-29T23:37:05-07:00'
date: '2026-11-15T09:28:02-08:00'
authors:
  - bendu
label: the-fzf-command-is-a-great-alternative-to-find
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - fzf
  - find
  - fuzzy
  - bat
  - preview
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Example Usages

- [Some Useful Shell Functions - fzf](https://github.com/legendu-net/icon/blob/dev/utils/data/bash-it/custom.plugins.bash)

- [Advanced fzf examples](https://sourcegraph.com/github.com/junegunn/fzf/-/blob/ADVANCED.md)

## Speed up `fzf`

1. By default,
   `fzf` uses `find` to find files.
   A different command can be configured via the environment variable `FZF_DEFAULT_COMMAND`.
   It is suggested that you use `fd`
   which is both more intuitive and way much faster.

## References

- [fzf @ GitHub](https://github.com/junegunn/fzf)

- [FZF very slow on mounted NTFS drives #2330](https://github.com/junegunn/fzf/issues/2330)

- [fzf is slow in large directory #1419](https://github.com/junegunn/fzf/issues/1419)

- [FZF Vim integration](https://github.com/junegunn/fzf/blob/master/README-VIM.md)

- [fzf Explained by the Author](https://junegunn.github.io/fzf/)

- [A Practical Guide to fzf: Building a File Explorer](https://thevaluable.dev/practical-guide-fzf-example/)

- [A Practical Guide to fzf: Shell Integration](https://thevaluable.dev/fzf-shell-integration/)

- [A Practical Guide to fzf: Vim Integration](https://thevaluable.dev/fzf-vim-integration/)

- [A Practical Guide to fzf: Building a Git Explorer](https://thevaluable.dev/fzf-git-integration/)

- [Advanced fzf examples](https://sourcegraph.com/github.com/junegunn/fzf/-/blob/ADVANCED.md)

- [4 Useful fzf Tricks for Your Terminal](https://pragmaticpineapple.com/four-useful-fzf-tricks-for-your-terminal/)
