---
title: Pointers in C++
created: '2012-10-21T00:00:00-07:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: pointers-in-c++
license: CC-BY-4.0
tags:
  - C++
  - programming
  - pointer
---

## Pointers

0. No pointer, no polymorphism.

1. C/C++ is notorious for raw pointers.
   While pointers can boost up the speed of programs,
   it invites a trillion chances for making mistakes.
   You should avoid using raw pointers,
   instead,
   consider using `unique_ptr`, `shared_ptr` and `weak_ptr`.
   They are almost as efficient as raw pointers but much safer to use.

1. If `p` is a dynamically allocated array,
   you have to use `delete[] p` to delete it when it is no longer required.

1. `auto_ptr` objects cannot be stored in STL containers,
   because they are not copy-construable or assignable.
