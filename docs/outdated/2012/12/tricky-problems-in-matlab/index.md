---
title: Tricky Problems in MATLAB
created: '2012-12-20T10:41:22-08:00'
date: '2026-11-15T09:34:47-08:00'
authors:
  - bendu
label: tricky-problems-in-matlab
license: CC-BY-4.0
tags:
  - trick
  - trap
  - programming
  - MATLAB
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. Sometimes you might find that you can use some built-in function in
   MATLAB at first, but later you cannot use it any. If so, you should
   probably check whether you are doing parallel computing in MATLAB.
   Parallel computing in MATLAB can cause some problem. What you can do
   is to use other functions that MATLAB accept in parallel computing
   to replace these which result in problems.

1. `dlmwrite` is convenient to write vector and matrix data to a file,
   but it might lose accuracy especially when you do not specify the
   accuracy attribute. So do not use `dlmwrite` to write data into text
   files when you works with high accuracy data, instead, you can use
   binary data.

1. `+` has priority over `:` in MATLAB which is different from R.

1. When MATLAB starts, it set the random number generator to the
   default one and set the seed to be the default seed. So if you run a
   simulation, reboot MATLAB and run the same simulation, you will get
   the same results.

1. Since most arithmetic objects in MATLAB are matrices, arithmetic
   operations in MATLAB are basically matrix operations. So `+`, `-`,
   `\*`, `/` are matrix addition operator, matrix subtraction
   operator, matrix multiplication operator and matrix division
   operator respectively.
   Notice that `/` is also called right matrix division operator. Suppose
   `B/A=X`, it means that `XA=B`. There is also another matrix division
   operator $\backslash$. Suppose $B\backslash A=X$, it means that
   `AX=B`.
   If you want to perform element wise
   operation rather than matrix operations, you have to put
   an extra dot (i.e. `.`) before the corresponding matrix
   operators.
