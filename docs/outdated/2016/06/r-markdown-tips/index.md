---
title: R Markdown Tips
created: '2016-06-09T17:52:05-07:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: r-markdown-tips
license: CC-BY-4.0
tags:
  - programming
  - CRAN
  - R Markdown
  - markdown
  - R
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[RMarkdown Reference](https://www.rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf)

1. The `rmarkdown` package is preferred to the `markdown` package.
   There is also a small bug with the `markdown` package.
   `markdown::markdownToHTML` does not render markdown title of the format `##Title` correct.
   A space is required after `#` for `markdownToHTML` to work.
   However,
   `rmarkdown::render` works well on both situations.

1. There are several ways to pass values between the R workspace and R Markdown.
   One way is to use global variables (from the R workspace) in R Markdown directly.
   However,
   you have to tell R Markdown the right working environment using the option `envir = 0`.
   Without this,
   R Markdown uses the current working environment
   which might not be the global working environment
   (e.g., when `knit` is called inside a function).
   Sometimes,
   it is more convenient to substitute patterns in R Markdown with required values directly.
   Make sure to use unique patterns if you do it in this.
   For example,
   if you want to pass a variable `site` by substituting into R Markdown,
   a good way is to replace pattern `${site}` (instead of plain `site`) with the value of the variable `site`.

1. Avoid doing complicated calculations in RMakrdown.
   Separated the code for calculation, etc., and use rmakrdown for reporting purpose mostly ...,

1. `plotly` (for graphics) and `DT` (for tables) are great visualization tools to use with R Markdown.
