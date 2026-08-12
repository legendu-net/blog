---
title: Calculate Covariance between Multinomial Categories by Hand
created: '2013-11-17T15:14:27-08:00'
date: '2026-08-11T22:19:13-07:00'
authors:
  - bendu
label: calculate-covariance-between-multinomial-categories-by-hand
license: CC-BY-4.0
tags:
  - fun problem
  - Statistics
  - probability
  - multinomial
  - covariance
---

Let $(X_1, \ldots, X_k)\sim\text{Multinomial}(n, p_1, \ldots, p_k)$.
I'll show how to calculate $Cov(X_i, X_j), i\ne j$.
The main purpose of doing this is to illustrate the little trick
of reducing complexity of problems by decomposing a complicated random variable
into simple ones.

Let $(Y_{i1}, \ldots, Y_{ik})\overset{iid}{\sim}\text{Multinomial}(1, p_1, \ldots, p_k), i\ge1$,
then
\$$
X_j = \sum_{i=1}^n Y_{ij}, 1\le j \le k.
$\$
So,
\\begin\{align}
Cov(X_i,X_j) &= Cov(\\sum\_{l=1}^n Y\_\{li}, \\sum\_{m=1}^n Y\_\{mj})\\nonumber\\newline
&= \\sum\_{l=1}^n\\sum\_{m=1}^n Cov(Y\_\{li}, Y\_\{mj})\\nonumber\\newline
&= \\sum\_{m=1}^n Cov(Y\_\{mi}, Y\_\{mj})\\nonumber\\newline
&= nCov(Y\_\{1i}, Y\_\{1j}) = n(EY\_\{1i}Y\_\{1j} - EY\_\{1i}EY\_\{1j})\\nonumber\\newline
&= -np_ip_j\\nonumber\\newline
\\end\{align}
