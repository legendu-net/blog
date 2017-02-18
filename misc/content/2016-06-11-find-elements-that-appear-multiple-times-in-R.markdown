UUID: 6168bfe8-c6d8-4521-ab98-ec8f388a6c11
Status: published
Date: 2016-06-11 15:31:16
Author: Ben Chuanlong Du
Slug: find-elements-that-appear-multiple-times-in-R
Title: Find Elements That Appear Multiple Times in R
Category: Programming
Tags: programming, CRAN, R, frequency, table, multiple times, unique

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

```R
freq = tapply(x, x, FUN=length, simplify=TRUE)
freq[freq > 1]
# or you can use
freq = table(x, useNA = "always")
freq[freq > 1]
```
