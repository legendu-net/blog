---
title: Comparison of Values Involving NA in R
created: '2016-05-10T20:33:23-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: comparison-of-values-involving-na-in-r
license: CC-BY-4.0
tags:
  - programming
  - R
  - comparison
  - NA
  - missing
  - CRAN
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

The best way to compare values containing `NA` in R is to define customized comparison functions.
Here is an example.

```R
equals = function(x1, x2, na_as_na = FALSE, reverse = FALSE) {
    if (reverse) {
        return(!equals(x1, x2, na_as_na, reverse = FALSE))
    }
    if (na_as_na) {
        return(x1 == x2)
    }
    ifelse(
           is.na(x1), 
           ifelse(is.na(x2), TRUE, FALSE), 
           ifelse(is.na(x2), FALSE, x1 == x2)
       )
}
```
