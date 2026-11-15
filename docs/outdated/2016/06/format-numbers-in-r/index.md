---
title: Format Numbers in R
created: '2016-06-11T16:55:27-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: format-numbers-in-r
license: CC-BY-4.0
tags:
  - programming
  - R
  - CRAN
  - formatting
  - numbers
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

When working with dates,
it is desirable to format months and days as 2 digits numbers with a leading 0.

```R
sprintf("%02d", 1)
# or 
formatC(1, width = 2, flag = 0)
```

Note: I encounter a bug in formatC before.
Instead of produce an output like `04`,
it produced ` 4`.
Unfortunately,
I had to deliver the project,
so I quickly fix the problem by substituting spaces with `0's`
instead of figuring out what really happen.

2. Comma delimited numbers.

```R
> formatC(1:10 * 100000, format = "d", big.mark = ',')
 [1] "100,000"   "200,000"   "300,000"   "400,000"   "500,000"   "600,000"  
 [7] "700,000"   "800,000"   "900,000"   "1,000,000"
```
