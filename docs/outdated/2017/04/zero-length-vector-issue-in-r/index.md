---
title: Zero-length Vector Issue in R
created: '2017-04-10T19:21:27-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: zero-length-vector-issue-in-r
license: CC-BY-4.0
tags:
  - programming
  - CRAN
  - R
  - issue
  - trick
  - trap
  - vector
  - zero-length
  - 0-length
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

The corner case of 0-length vectors is not well considered in R.
It causes issues in several situations.
First, `1:n` is probably not what you want when `n = 0`.
Second, `df$col = 0` throws error when `df` is an empty (0 row) data frame.
To avoid these issues,
it is suggested that you write more robust R code.

```R
# use 
seq_len(n)
# instead of 
1:n
```

```R
# use 
for (i in seq_len(n)) {
    ...
}
# instead of 
for (i in 1:n) {
    ...
}
```

```R
# use 
df$col = rep(x, nrow(df))
# instead of 
df$col = x             
```

Strings function in base R do not behavior well when zero-length vectors are involved.
For example,
`paste('a', character(0))` returns a character vector of length 1
rather than length 0.
Functions in the `stringi` packages works well when zero-length vectors are involved.
For example, the code below returns a 0-length vector.

```
library(stringi)
'a' %s+% character(0)
```

It is suggested that you always use string functions in the `stringi` package
rather than string functions in base R.
