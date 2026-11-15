---
title: Recursion in Scala
created: '2017-06-22T13:34:25-07:00'
date: '2026-11-15T09:25:20-08:00'
authors:
  - bendu
label: recursion-in-scala
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - recursion
  - tail recursion
  - tail recursive call
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tricks to Write Tail Recursive Calls

1. A useful trick to write tail recursive function is
   to include the result to return as a parameter.
   If the result to return is a tuple (or so),
   you just need to include those elements that are not already parameters.

## Tricks that Do Not Need Tail Recursive Calls

Sometimes you don't bother to write a tail recursive function (and don't want use while loop either)
but still want to have good performance and avoid stack overflow issue.

1. A good trick is to return Iterator or Stream.

1. If the results to return is numbers or strings,
   you can cache the results using a HashMap to avoid writing tail recursive functions.

1. Say that you want to reduce a seq.
   Instead of writing a method to handle the situation of multiple elements,
   you can just write a method to handle the situation of 2 elements,
   and then call the `reduce` method.

```scala
seq.reduce(_ youOperator _)
```
