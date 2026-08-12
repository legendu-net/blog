---
title: 'Neovim: liblua5.1-luv.so.0 Not Found on Debian'
created: '2024-08-26T17:49:56-07:00'
date: '2026-08-11T22:19:20-07:00'
authors:
  - bendu
label: neovim-liblua5.1-luv.so.0-not-found-on-debian
license: CC-BY-4.0
tags:
  - computer science
  - programming
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

`liblua5.1-luv.so.0` is not present under `/lib/x86_64-linux-gnu/`.
Manually make a symbolic link from
`liblua5.1-luv.so.1.0.0` resolved the problem.
