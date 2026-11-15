---
title: Numeric Algorithms
created: '2013-10-22T13:37:34-07:00'
date: '2026-11-15T09:15:06-08:00'
authors:
  - bendu
label: numeric-algorithms
license: CC-BY-4.0
tags:
  - tips
  - algorithm
  - error tolerance
  - numerical issue
  - overflow
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. comparing lots of values that are very close is not a good idea. p-values, permutation test statistics.
   a better way is to work on integers instead, for example, permutation indexes ...
   if you do have to compare real numbers, give an error tolerance.

1. the error doesn't come from calculation but from storing numbers.
   I used to think that log(x) is problematic when x is small (I thought this can cause numeric problems).
   actually this won't cause problems at all as long as x is a positive double number.

1. overflow of double becomes inf, for arithematic calculating, this is probably not a problem
   overflow of positive double (to left) becomes 0, for many arithematic calculation, this is not a problem.

1. use log and then exp is a good way to avoid overflowing problem,
   this trick is used a lot in statistics but it seems that even boost library don't use this trick.
   so, don't trust these libraries totally, you own implementation might even be better.
