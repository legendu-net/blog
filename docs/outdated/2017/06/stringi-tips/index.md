---
title: stringi Tips
created: '2017-06-06T08:03:00-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: stringi-tips
license: CC-BY-4.0
tags:
  - programming
  - stringi
  - CRAN
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. It is suggested that you use the package `stringi` instead of string utilities in R base.
   There are multiple reasons.

   ```
    - stringi has consistent namings and signatures
    - the behavior of functions in stringi is more reasonable from engineering perspective
   ```

## Regular Expression

1. Use `$1` instead of `\\1` to capture the nth capture group,
   and similarly for other capture groups.
