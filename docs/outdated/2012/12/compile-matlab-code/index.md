---
title: Compile MATLAB Code
created: '2012-12-07T23:48:09-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: compile-matlab-code
license: CC-BY-4.0
tags:
  - compile
  - compiler
  - programming
  - MATLAB
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. MATLAB code can be compile to C/C++ code or stand alone applications.
   Usually you can run the stand-alone application in Windows system directly,
   but for Linux system it is a little headachy.
   The stand-alone application usually takes less than 50% of the time
   that the original MATLAB code takes to run.
   This depend on different situations.
   It can happen that the stand-alone application runs slower than the original MATLAB code.

1. To compile MATLAB code to c code,
   you can use `mcc -mc mainfn sub1fn sub2fn`,
   and to produce an stand alone executable file from c files,
   you can use `mbuild mainfun sub1fn sub2fn`.

1. To compile MATLAB code to c++ code
   and to create a corresponding stand-alone executable file
   you can use `mcc -p mainfn sub1fn sub2fn`.
   To compile MATLAB code that contains Handle Graphics functions into C++
   and to create a corresponding stand-alone executable file,
   you can use `mcc -B sglcppp mainfn sub1fn sub2fn`.

1. To compile MATLAB code to c and to create corresponding stand-alone executable file,
   you can use `mcc -m mainfn sub1fn sub2fn`.
   To compile MATLAB code that contains Handle Graphics functions into c
   and to crate a corresponding stan-alone executable file,
   you can use `mcc -B sgl mainfn sub1fn sub2fn`.

1. If you use parallel computing,
   you will not be able to run the compiled application (at least before version 2010b)
   unless you have MATLAB Distributed Computing Server (MDCS) available on a computer cluster.
   If you have access to a MDCS,
   there is little necessary for you to compile your MATLAB parallel code to a stand-alone application,
   so just do not bother to compile your MATLAB parallel code.
