---
title: Sweave
created: '2012-11-13T00:05:31-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: sweave
license: CC-BY-4.0
tags:
  - LaTeX
  - programming
  - Sweave
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. Do not use sweave unless you are sure that you have run to the same
   code again and again on different data sets, and you want the report
   to be generate automatically each time.

1. You must start `<<...>>` at the beginning a line.

1. If you want to do simulation, you'd better set a seed for the random
   number generator (RNG). In this way, you can reproduce your simulation
   and the running result of the R code will always be the same. Sometime,
   the result of R code will different every time you run it. For example,
   if you want to test the speed of some algorithms, the time needed for
   each algorithm will be different each time you run the code even if you
   use the computer and use a same seed for RNG (if simulation used). For
   this kind of output, you'd better not use Sweave. A better way is to
   write the auto-write the result into a tex document, and then include
   the file in your main tex file. In this way, you can still redo old work
   easily but without worrying out having different outputs every time.
