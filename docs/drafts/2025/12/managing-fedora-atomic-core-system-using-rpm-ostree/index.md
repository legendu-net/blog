---
title: Managing Fedora Atomic Core System Using rpm-ostree
created: '2025-12-07T18:19:15-08:00'
date: '2026-11-15T09:28:38-08:00'
authors:
  - bendu
label: managing-fedora-atomic-core-system-using-rpm-ostree
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Linux
  - atomic
  - Fedora
  - rpm
  - ostree
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Fedora Atomic Linux distributions use
`rpm-ostree` to install system tools.

## Upgrade

```
sudo ostree admin pin 0
rpm-ostree rebase
rpm-ostree rebase fedora:fedora/43/x86_64/kinoite
```
