---
title: Statistics
created: '2013-10-13T22:40:14-07:00'
date: '2026-11-15T09:15:35-08:00'
authors:
  - bendu
label: statistics
license: CC-BY-4.0
tags:
  - tips
  - Statistics
  - modele
  - modeling
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. in real problems, the true value of (some quantity) are usually unknown/defined,
   even if we can collect data about it,
   e.g., Amazon goods, what is the true cost of a good?
   You must first give a definition ...

1. it seems that many problems are related to survey (as long as data collection)
   though data might not be good, we can correct for sampling bias
   the way to deal with unbalanced data in logistic regression is inspring ...

a) weight minor class (over-sampling), recommended

b) under-sampling, throw away some observations in the larger group
hard to do model validation

c) use similar idea as random forest, bagging ...
similar to give more weights to minor group
sample 90% of minor group and some part of larger group (approximately equal obs)
repeat this ..., inherit many pros of random forest ...

some people recommend random forest as a better alternative to logistic
regression when data is unbalanced, but random forest need more data than logistic regression

3. if model is not good, adjust it to correct bias ...
   use simple rules, better than nothing ...

1. general effect of unbalance data? bernoulli example, central limit theorem ... confidence
   interval, simulation and so on ...

1. ways people deal with extremely unbalanced data in business ...

1. when you solve a stat problem,
   the first thing to do is to get clear about your purpose,
   what the goal of the project?
   e.g., the bayesian, portfolio, loan, PD example, one was talking about conservative while
   I thought about correctness

1. 模型里面，multinomial还有一种是保留顺序的，更好！

1. complex model in the sake of complex won't help,
   but complex model to address real problems helps.

1.
