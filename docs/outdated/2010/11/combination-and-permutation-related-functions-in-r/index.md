---
title: Combination and Permutation Related Functions in R
created: '2010-11-20T00:00:00-08:00'
date: '2026-11-15T12:20:41-08:00'
authors:
  - bendu
label: combination-and-permutation-related-functions-in-r
license: CC-BY-4.0
tags:
  - R
  - statisitcs
  - combination
  - permutation
  - programming
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. `expand.grid` creates a data frame from all possible combinations of supplied vectors or factors.
   For example,

   ```
    > expand.grid(letters[1:2], 1:3, c("+", "-"))
       Var1 Var2 Var3
    1     a    1    +
    2     b    1    +
    3     a    2    +
    4     b    2    +
    5     a    3    +
    6     b    3    +
    7     a    1    -
    8     b    1    -
    9     a    2    -
    10    b    2    -
    11    a    3    -
    12    b    3    -
   ```

1. `combn` generates all combinations of $n$ elements taking $m$ at a time.
