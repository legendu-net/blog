---
title: String in C++11
created: '2012-08-20T00:00:00-07:00'
date: '2026-11-15T09:15:12-08:00'
authors:
  - bendu
label: string-in-c++11
license: CC-BY-4.0
tags:
  - auto
  - iteration
  - programming
  - C/C++
  - string
  - loop
  - char
---

1. `auto s = "abcd"` creates `const char *` not string, so use `auto` with caution.

1. Since a string in C++ is an array of chars,
   you can operate it like an array.
   For example, you can use range-based for loop and so on.

1. It is recommended that you use `std::string` in function which are not intended to be
   interfaces, and you use `const char *` as parameters of function that are intended to be
   interfaces (e.g., compiled as shared library and so on).

1. You can use `==` to compare whether the content of two `std::string` are the same,
   but you cannot use `==` to compare the content of `const char *`.
