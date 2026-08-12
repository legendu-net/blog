---
title: What Are the Two Integers?
created: '2013-02-08T11:41:48-08:00'
date: '2026-08-11T22:19:14-07:00'
authors:
  - bendu
label: what-are-the-two-integers
license: CC-BY-4.0
tags:
  - puzzle
  - fun problems
  - number
---

I met a friend majored in math on a bus home today.
He held a piece of paper with a question
(probably an interview question since he is trying to find a job recently).
He asked the question to me and I found it to be an interesting one.

A very large positive integer is divisible by all
but two of the integers

$$1, 2, 3, \dots, 10000,$$

and the two excepted numbers are consecutive integers.
What are the two integers?

I did not get the answer before my friend get off the bus.
However, as soon as arriving home I get the key to the questions.
The outline of my thoughts leading to the answer is as follows.

1. Assume the question is valid,
   i.e., there is a unique answer to this problem.

1. Both of the two numbers (indivisible to the large integer)
   have prime factorization of the form: $a^b$,
   where $b$ is the largest possible value.

1. Since one of two consecutive integers is even,
   one of the two numbers (indivisible to the large integer) has
   the form $2^b$ and thus is $2^{13}=8192$.

1. The other number must be either `8193` or `8191`.
   Since `8193` is divisible to `3` but not `9`
   (`8 + 1 + 9 + 3 = 21` is a multiple of `3` but not `9`),
   it does not have the form mentioned in step 2.
   So the other number is `8191`.
