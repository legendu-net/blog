---
title: Special Functions in MATLAB
created: '2012-12-04T00:00:00-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: special-functions-in-matlab
license: CC-BY-4.0
tags:
  - function
  - programming
  - MATLAB
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. `sin` calculates sine of arguments in radian
   while `sind` calculates sine of arguments in degrees;
   `asin` calculates inverse of sine resulting in radian
   while `asind` calculates inverse of sine resulting in degrees.
   Other triangular functions behave similarly.

1. The modified Bessel function of the first kind `$I_n(x)$`
   is implemented as `besseli` in MATLAB.
   Notice that for large value ` x`, `$I_n(x)$` is huge,
   so it is better to use scaled Bessel function for large `x`.
   To do this, you just need specify an extra argument for `besseli`.
   Notice that other kind of Bessel functions are also implemented in MATLAB.

1. Incomplete Beta function is implemented as `betainc`
   and incomplete Gamma function is implemented as `gammainc` in MATLAB.

1. The logarithm of Gamma function is implemented as `gammaln`
   and the logarithm of Beta function is implemented as `betaln` in MATLAB.

1. `cart2sph, cart2pol, pol2crt, sph2cart, hsv2rgb` and `rgb2hsv` can
   transform coordinates between different coordinate systems.

1. `mfun` can help evaluate special mathematica functions numerically,
   but you should be aware of the fact that the result return by
   calling `mfun` is not as accurate as invoking these special function
   directly in MATLAB, especially when a function is near its root and
   its arguments are relatively large. Also `mfunlist` can list special
   functions for use with `mfun`.
