UUID: 57c3e6af-6f49-40ea-876e-26a64ee3b59a
Status: published
Date: 2016-06-11 17:53:43
Author: Ben Chuanlong Du
Slug: R-configuration
Title: R Configuration
Category: Programming
Tags: programming, R, CRAN, configuration, settings

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. You can customize R libraries to use 
by puting a line `R_LIBS="path_to_library"` in the `.Renviron` file.
However, 
a tricky thing is that if the specified path does not exist,
then it is ignored without any warning.
So sometimes you think have set up a customized library 
but it does not show up as expected. 
It is probably because you specified a incorrect path.

2. R: update Renviron.site, not Renviron!!!
