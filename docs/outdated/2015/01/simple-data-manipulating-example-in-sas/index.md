---
title: Simple Data Manipulating Example in SAS
created: '2015-01-22T13:33:00-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: simple-data-manipulating-example-in-sas
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - IML
  - R
  - CRAN
  - example
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Suppose there is a data `s` in SAS containing a variable `x`.

```
x
3
3
4
5
2
3
9
7
1
100
3
5
0
```

Now we want to create another variable `y` such that

```
y = 3 if x =3
y = B_2 y + 2, o.w.
```

This is very hard to using the data step in SAS
while very easy to do in R or the SAS IML procedure.
