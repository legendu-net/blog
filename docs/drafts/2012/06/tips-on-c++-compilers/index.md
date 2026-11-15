---
title: Tips on C++ Compilers
created: '2012-06-01T14:46:42-07:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: tips-on-c++-compilers
license: CC-BY-4.0
tags:
  - C++
  - programming
  - GCC
  - thread
  - compiler
  - link
  - cpp
  - clang
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## GCC

1. User option `-lpthread` to link the thread library when your code use the thread library.
   If you do not use, the option `-lpthread`, you can probably compile your coe without any
   error or warning, but you will probably get the following error when you run the code.

   ```
    terminate called after throwing an instance of 'std::system_error'
      what():  Operation not permitted
      Aborted
   ```

1. User option `-std=c++0x` to compile C++11 code.

1. Some thumb rules for compiler optimization:

   - when you need to debug, use the option `-O0`
     (and the option `-g` to generate debugging symbols.)

   - when you are preparing to ship it,
     use the option `-O2`.

   - when you really care about performance (e.g., for use on Gentoo),
     use the option `-O3`.
     However, this is not always safe.

   - when you need to put it on an embedded system, use `-Os`
     (optimize for size, not for efficiency.)

1. use to `-D` to predefine macros

## Clang

1. use `libc++` instead `libstdc++`
