---
title: Performance Tips for C++
created: '2012-10-20T10:36:42-07:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: performance-tips-for-c++
license: CC-BY-4.0
tags:
  - tips
  - performance
  - C++
  - programming
---

## Performance

1. If there is some block of useless code,
   the compile is smart enough to ignore it and thus speed up the program.

1. Use the option `-O2` to generate optimized code when you are ready to publish your code.

1. Define variables only when needed to avoid the overhead of creating and deleting temporary variables.
   It is suggested that you put variables into the smallest possible enclosing brace.

1. When shuffling data, it is better to shuffle in place
   if objects/data to be shuffled are not expensive to copy
   (e.g., when data are double or integers).
   Otherwise, it is better to shuffle indexes/iterators of the container.

1. It is STRONGLY suggested that you specify the size/capacity of a vector
   if you know it.
   Even if you do not know the exactly size of a vector,
   it is often a good idea to initialize the vector with an rough estimate of its final size.
