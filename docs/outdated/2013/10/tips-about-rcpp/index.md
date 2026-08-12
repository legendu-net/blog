---
title: Tips about Rcpp
created: '2013-10-09T18:53:10-07:00'
date: '2026-08-11T22:39:38-07:00'
authors:
  - bendu
label: tips-about-rcpp
license: CC-BY-4.0
tags:
  - tips
  - programming
  - Rcpp
  - C++
  - CRAN
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

\*\*
Things under legendu.net/outdated are outdated technologies
that the author does not plan to update any more.
Please look for better alternatives.
\*\*

1. The trick of using a macro `NORCPP` to indicate
   whether you are using the code in Rcpp.
   This makes it easier to using the code both natively and in Rcpp
   and makes it easier to debug the code.
   You have to use the option `-D NORCPP` when compiling the code natively using `g++/clang++`.

1. The Armadillo package is more conveinient to use
   than `NumericVector`, `NumericMarix`, etc. when using Rcpp.

1. Rcpp doesn't have a uniform integer generator curently,
   someone is working on sample equivalence currently.
   You can use `runif` to achive what you want.

1. I think you misunderstood `Rcpp::sugar`,
   I think vectorized version functions return `NumericVector`,
   it is just that they can be silently converted `arma::rowvec` and so on ...

1. Rcpp make vectorized version of random number generation functions,
   however these with prefix `Rf_` is non-vectorized.
   They are functions coming from `Rmath.h`.

1. It is suggested that you alwasy prefixed functions
   with their namespaces when using Rcpp.
   Without prefixed namespaces,
   function name conflictions happen a lot
   (e.g., `std::abs` and `Rcpp::abs`)
   And when this happens,
   it is very tricky and very hard to debug.

1. `RNGScope` easy to forget,
   the default seed no randomization at all if you do not use it ...
   so it is the first to check if you find some thing wrong with your randomization code.

1. Rcpp does not have bool equivalent.
   Use integers (0 and 1) instead.

1. It seems that type is not a big deal for Rcpp,
   because `as<type>` takes care of it.
   If you pass an object which is not exactly the required type,
   Rcpp tries cast it to the right type.

1. One way to avoid terminating R becuase of DLL problem by Rcpp
   is to remove all related object every time you restart R.
   Or if there is a better way to check this?

1. but you should check source code of `rnorm` in Rcpp to see what they used ...
   `Rf_pnorm` not defined either
   Rcpp, don't use functions with same names as r functions,
   potentially C functions, confliction ...
   `Rf_qbeta`, parameters can be inferred from R documentation
   problem of `Rf_qnorm`? not definied? what the heck
