---
title: Good C++ Libraries
created: '2012-10-18T11:46:12-07:00'
date: '2026-11-15T09:16:51-08:00'
authors:
  - bendu
label: good-c++-libraries
license: CC-BY-4.0
tags:
  - library
  - programming
  - GSL
  - package
  - GMP
  - boost
  - it++
  - C++
  - armadillo
  - NTL
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Good C++ Libraries

1. Armadillo: linear algebra
1. it++: signal processing
1. shogun: a large scale machine learning toolbox
1. boost: an advanced general purpose C++ library
1. dlib: a general purpose cross-platform C++ library designed using contract programming and modern C++ techniques.
1. R: a popular statistic software.
1. Blitz++: linear algebra and random number generator
1. GMP: the GNU Multiple Precision Arithmetic Library
1. NTL: a library for doing number theory
1. HPX: high performance parallel library
1. Cinder (graphics, audio, video, networking, image processing and computational geometry)
1. libcurl: a free and easy-to-use client-side URL transfer library
1. GSL: a comprehensive C/C++ scientific library
1. ODB: an object-relational mapping (ORM) system for the C++ language.

## Database

1. sqlpp11

## Scitific Computing

### Armadillo

1. The C++ standard library supports methods `at` and `operator[]` for accessing elements of containers.
   Armadillo supports these two methods as no-bound-checking versions.
   `operator()` is the bound-checking (and thus preferred) version for accessing elements of matrices and arrays.

1. Armadillo use `*` for matrix multiplication and `%` element-wise multiplication,
   which is different from R and MATLAB.

### GSL

1. The GSL library implements popular special functions many of which
   are not implemented in other libraries
   (e.g., the Lambert-W function is not implemented in Boost).

1. The distribution related functions (quantile, cdf, PDF, etc) in
   GSL is more convenient to use than the Boost library.
   You can define macros to match the GSL version of distribution functions with
   R version of distribution functions.

### R

There are some useful distribution related C functions in R.h.
You can use these C functions which do not require an session of R
(random number generating functions require a session of R and thus cannot be used in C/C++ code directly)
in your C/C++ code.
A more general and powerful way to call R related functions is via the "Rinside" package.
Using the "Rinside" package,
you can call any R function not just C functions in R header files.
On the contrary, "Rcpp" is a way to extend R via C++.
The most convenient way to use "Rcpp" is to expose C++ classes/methods/functions to R via `RCPP_MODULE`.
Note that "Rcpp" is for R users not C/C++ users,
i.e., you must come back to R.
Trying to compile C/C++ based on "Rcpp" and the binary code will result in segmentation fault.

## Unit Testing

1. Catch

## Other General Purpose Libraries

## Boost

0. The boost random library (and thus the standard library of C++11) does not have a way to generate
   random numbers from the beta distribution directly,
   however, you use $X/(X+Y)$ where $X$ and $Y$ are independent
   random variables from the gamma distribution.

1. `boost::accumulator` is good for incremental calculations,
   especially when several quantities having dependent relationships need
   be calculated.

## Debugging Tools

1. [gdb](http://www.gnu.org/software/gdb/)

1. [Valgrind](http://valgrind.org/)

1. [CppCheck](http://cppcheck.sourceforge.net/)

## Compilers

1. gcc/g++
1. clang/clang++
1. xlc (for IBM AIX)
