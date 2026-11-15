---
title: Understand the Design of Python
created: '2019-10-04T20:19:41-07:00'
date: '2026-11-15T12:20:36-08:00'
authors:
  - bendu
label: understand-the-design-of-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - design
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Design

1. There is no constant variables in Python.
   If you need a constant variable in Python,
   just define one and never change it.
   It is suggested that you use UPPER_WITH_UNDERSCORE naming style for const variables in Python.
   There is no private variables/method in Python either.
   You can change/call any variable/method in a module/class.
   However,
   members that start with a single underscore (`_`) are considered as private by convention
   and you should avoid using them directly.

1. The bottom-most package in Java should be a file in Python.
   Do not use inner classes in Python.
   Just put classes in the same module.

1. Python is a dynamic language and thus does not support function/method overloading.
