---
title: Boolean Values in C++
created: '2012-10-07T21:56:02-07:00'
date: '2026-11-15T09:15:45-08:00'
authors:
  - bendu
label: boolean-values-in-c++
license: CC-BY-4.0
tags:
  - boolean
  - C++
  - programming
  - cpp
---

1. Boolean expressions are evaluated from left to right (the same in Java),
   so it is totally OK to write code like

   ```
    if(a < x.size() && x[a]){
        ...
    }
   ```

   where `x` is a vector.

1. There is no `&&=` and `||=` operators in C++,
   instead you can use `&=` and `|=`.
   Though `&=` and `|=` are not specially for boolean values,
   they work perfectly for boolean values.

1. If the numbers you work with support infinity or NaN,
   boolean expressions become tricky.
   For example, suppose `nan` is a variable representing Nan,
   both `2 < nan` and `2 >= nan` return `false`,
   which is not what we want.
   A safer way is to first check whether numbers involved are NaNs.
   Hopefully, ternary boolean type will be introduced into C++ in future.
