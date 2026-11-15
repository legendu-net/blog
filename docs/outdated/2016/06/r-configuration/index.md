---
title: R Configuration
created: '2016-06-11T17:53:43-07:00'
date: '2026-11-15T09:28:19-08:00'
authors:
  - bendu
label: r-configuration
license: CC-BY-4.0
tags:
  - programming
  - R
  - CRAN
  - configuration
  - settings
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

\*\*
Things under legendu.net/outdated are outdated technologies
that the author does not plan to update any more.
Please look for better alternatives.
\*\*

1. You can customize R libraries to use
   by putting a line `R_LIBS="path_to_library"` in the `.Renviron` file.
   However,
   a tricky thing is that if the specified path does not exist,
   then it is ignored without any warning.
   So sometimes you think have set up a customized library
   but it does not show up as expected.
   It is probably because you specified a incorrect path.

1. R: update Renviron.site, not Renviron!!!
