---
title: Input and Output in C++
created: '2012-10-24T22:22:41-07:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: input-and-output-in-c++
license: CC-BY-4.0
tags:
  - C/C++
  - IO
  - C++
  - programming
---

Check the `io` directory on the page <https://bitbucket.org/dclong/cpp-learn/src>
for some illustrative examples for the following discussions.

0. You can format output of numbers using functions
   `std::setpresicion` and `std::setw` in the <imanip> header.

1. When you read data from a file into an array or write data from an array to a file,
   you can just use the address of the array.
   However,
   if a vector (e.g., vector `x`) is used instead of an array,
   you have to use the address of the underlying data in the vector `x` which is `&x[0]`.
   Also,
   when you read/write data into/from a vector,
   you have use the size of the vector `x` multiplied by the memory used by each element
   to calculate the total number of bytes,
   i.e.

```C++
x.size() * sizeof(x[0]);
```

or if `x` is a vector of double values you can use

```C++
x.size() * sizeof(double);
```

You cannot use `sizeof(x)`,
because it is the size of the vector itself
(without counting the underlying array) and is always the same (12 bytes).
