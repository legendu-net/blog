UUID: c1376d5c-f08d-4704-b9cd-3a7f69d670e1
Status: published
Date: 2016-11-29 01:13:10
Author: Ben Chuanlong Du
Slug: rmarkdown-tips
Title: RMarkdown Tips
Category: Programming
Tags: programming, CRAN, RMarkdown, Markdown, R

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

[RMarkdown Reference](https://www.rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf)

1. There are several ways to pass values 
between the R workspace and RMarkdown.
One way is to use global variables (from the R workspace)
in RMarkdown directly.
However, 
you have to tell RMarkdown the right working environment 
using the option `envir = 0`.
Without this, 
RMarkdown uses the current working environment 
which might not be the global working environment
(e.g., when `knit` is called inside a function). 
Sometimes, 
it is more convenient to substitute patterns in RMarkdown with required values directly.
Make sure to use unique patterns if you do it in this.
For example, 
if you want to pass a variable `site` by substituting into RMarkdown,
a good way is to replace pattern `${site}` (instead of plain `site`) with the value of the variable `site`.

2. `rmarkdown::render` deprecates `knit2html` and `markdownToHTML`.
For example, 
markdown title must have spaces!!! while rmarkdown not ...

3. Avoid doing complicated calculations in RMakrdown. 
Separted the code for calculation, etc., and use rmakrdown for reporting purpose mostly ...,

