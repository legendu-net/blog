---
title: Cluster Management Made Easy with the Python Package Fabric
created: '2017-06-29T22:26:41-07:00'
date: '2026-06-12T22:31:50-07:00'
authors:
  - bendu
label: cluster-management-made-easy-with-the-python-package-fabric
license: CC-BY-4.0
tags:
  - Python
  - programming
  - Fabric
  - Ansible
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Ansible is a better alternative to Fabric.
It is suggested that you use Ansible instead.

1. Docstring will be displayed when you type the command `fab -l`.

1. Invoke is for local use.
   Fabric 2 will be based on invoke.

## Issues

UnicodeEncodeError: 'ascii' codec can't encode character '\\u2018' in position 33: ordinal not in range(128)

It is suggested that minimize output to avoid this issue.

Fabric has issues with Unicode-only characters right now.
Supressing outputs (of shell commands) containing unicode can help avoid potential `UnicodeEncodeError`.

## Question

Is it possible to surpress logging information?

## References

[Run Commands on Remote Machines](run-commands-on-remote-machines)
