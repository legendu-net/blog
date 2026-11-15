---
title: MATLAB Tips
created: '2014-08-24T10:43:54-07:00'
date: '2026-11-15T09:28:48-08:00'
authors:
  - bendu
label: matlab-tips
license: CC-BY-4.0
tags:
  - programming
  - tips
  - MATLAB
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.

1. MATLAB uses float computing by default.
   `3/5` return 0.6 in MATLAB instead of 0
   as will be returned in some other programming languages (e.g., Python).

1. to get size of an object, md = whos(obj); md.bytes

1. do we have `x *= 2` in matlab, if not, use ultisnips to do it!!! and python, R, Mathematica, bash, etc.

1. nohup matlab -nodesktop -nosplash -r "run('./RunSimulation10.m');quit;"

1. num2str, numbers cannot be used as string directly

1. Subscript indices must either be real positive integers or logicals. you confused matlab with your variable and the built-in function size!!!

1. dlmwrite 'precision', edit the corresponding post

1. You can use `warning('off','all')` to suppress warnings in MATLAB.

1. fitlm support the table data structure in R2015a and after but it only support matrix and dataset in R2013b and before.

1. matlab's strength is for engineering uses, it is a piece of shit for statistical purposes ... stay away from matlab and live longer!

1. matlab about array of string is too stupid, you need to use cell array of string ...

## Statistics

4. Use categorical to create a categorical array from data with values from a finite set of discrete categories.
   To group numeric data into categories, use discretize.

## Data Structure

1. Table in matlab is the equivalent data structure of data frame in R.

1. table(c1, c2) to join tables/cells/variables horizontally

1. You can use the function `readtable` to read the content of a file into a table.
