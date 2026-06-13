---
title: Generating Random Numbers in Java
created: '2014-10-19T19:40:40-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: generating-random-numbers-in-java
license: CC-BY-4.0
tags:
  - programming
  - random number generating
  - Java
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. The java.util.Random class provides a low-quallity generator
   suitable for "informal" uses of random numbers.

1. It is suggested that you use the classs
   [org.apache.commons.math3.random.RandomDataGenerator](http://commons.apache.org/proper/commons-math/javadocs/api-3.6/org/apache/commons/math3/random/RandomDataGenerator.html)
   for generating random numbers if quality is of a concern.
   Please refer to
   [Summary on Random Number Generators](summary-on-random-number-generators)
   for more details.
