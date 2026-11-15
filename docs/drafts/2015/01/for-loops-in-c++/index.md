---
title: For Loops in C++
created: '2015-01-01T14:03:21-08:00'
date: '2026-11-15T09:18:34-08:00'
authors:
  - bendu
label: for-loops-in-c++
license: CC-BY-4.0
tags:
  - programming
  - C++
  - for loop
  - container
  - range
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are 3 for loops in C++,
the usual for loop, the range-based for loop (introduced in C++11) and the `std::for_each` for loop.

1. Both the range-based for loop and the `std::for_each` for loop
   applies operations on each element in a specified container/range.
   Both of them are able to mutate elements of a container/range,
   but you should never use them to erase elements from a container.
   You have to use the usual for loop to erase elements from a container.

1. It is suggested that you use the range-based for loop (introduced in C++11)
   in place of `std::for_each` when applicable
   as the range-based for loop is simpler and more readable.
