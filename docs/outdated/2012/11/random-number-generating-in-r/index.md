---
title: Random Number Generating in R
created: '2012-11-05T00:21:35-08:00'
date: '2026-11-15T09:33:49-08:00'
authors:
  - bendu
label: random-number-generating-in-r
license: CC-BY-4.0
tags:
  - R
  - programming
  - RNG
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. Functions for sampling random numbers from distributions
   share a same "basic" random number generator (RNG).
   If one set a seed for the "basic" RNG in use,
   it affects all functions for generating observations from distributions.
   The kind of "basic" RNG can be queried and set by `RNGkind`.
   The default RNG in R is Mersenne-Twister.

1. When doing a big simulation,
   some people like to split the simulation into smart parts
   and run each part on a different machine.
   Theoretically speaking,
   this can cause problems,
   because random numbers generated on different machines might not come
   from disjoint parts of a same seed
   (or even not a same kind of random number generator).
   Parallel computing is an alternative to this approach.
