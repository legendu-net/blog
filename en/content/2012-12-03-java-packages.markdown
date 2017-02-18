UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Java Packages
Date: 2012-12-03 00:00:00
Tags: programming, package, Java
Category: Programming
Slug: java-packages
Author: Ben Chuanlong Du


## Appach CommonMath

1. StatUtils.varance is OK.

## Colt

1. `sample` of `RandomSample` is OK.

## Parallel Colt

1. ParallelColt does not make RNG parallized.

## Comparison of Packages

1. Colt is faster in random number generating than CommonMath,
especially for simple random number generation (e.g. normal random numbers), 
but Colt is no longer maintained.

2. The RNGs in Colt, Parallel Colt and CommonMath are all OK from statistical view.

