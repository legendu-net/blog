---
title: MATLAB for Visualization
created: '2012-12-03T10:08:36-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: matlab-for-visualization
license: CC-BY-4.0
tags:
  - image
  - visualization
  - programming
  - plot
  - graphics
  - MATLAB
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. To display a new graph on on top of an old one,
   you can use command `hold on`.
   In this way,
   you can create multiple plots in a same window.
   Though `plot` can already do multiple plot, command `hold on`
   can be very useful when you want to add some new points
   or curves to an existing graph (e.g. a histogram).

1. Function `subplot` displays multiple plots in the same window,
   which is similar to settings `par(mfrow=c(2,2))` or `par(mfcol=c(2,3))` in R.

1. Function `hist` and `histc` produces histograms.

1. Function `staris` produces step graph.

1. Function `plot` plots `2-D` graph
   while function `surf` plots `3-D` graphs.
   Function `surf` is usually used in conjugate with function `meshgrid`
   which can create a matrix of points over which the surface is to be plotted.
   You can also use `ndgrid` instead of `meshgrid` to generate a matrix of points.
   However,
   `ndgrid` is usually higher dimensions and the usage is a little different from `meshgrid`,
   so you have to be careful if you wan to use it.

1. After plotting figures using `plot`,
   you can use `title` to add titles for the figures,
   `axis` to set configurations for the axies,
   and `xlabel` and `ylabel` to set labels for the x and y axes.
   You can also use `set` to set all configurations for the plots.
   To do this,
   you have to first get the handle of the elements in the plots that you want to modify,
   and then apply `set` on it.

1. `inpolygon` can check whether given points are inside a polygon or not.

1. `spy` visualizes sparse matrices.

1. `image` can not only display images but also make mosaic plot
   (sometimes called heat plot or level plot) of a matrices.
   For example, to show the mosaic plot of matrix `x`,
   you can use `image(x,'CDataMap','CDataMapping','scaled')`.
