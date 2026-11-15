---
title: Tips on Excel
created: '2011-08-22T13:10:13-07:00'
date: '2026-11-15T09:17:40-08:00'
authors:
  - bendu
label: tips-on-excel
license: CC-BY-4.0
tags:
  - Statistics
  - MS Office
  - software
  - Excel
  - bug
  - tips
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## About Statistics Functions

1. Excel is not a reliable software for statistical analysis.
   It's not even capable for simple operations such as calculating
   mean and standard deviation when numbers are very big
   (at least before version 2007, not sure about later versions).
   If you do have to use Excel for statistical analysis,
   you'd better verify the results.

1. A bug in Excel 2007 (not sure about later versions)
   is that the degrees of freedoms of the Chisquare distribution can only be positive integers.
   If you pass a real number to related functions (density, cdf, etc),
   the degrees of freedom will first be coerced to an integer
   (I forget the exact behavior, but it's probably rounding down) and then do the calculation.
   No warning is shown in this process. Fotunately,
   the Gamma distribution behaves right in Excel.
   Be aware of the relationship between Chisquare distribution and Gamma distribution, you can circumambulate this bug.

1. It seems that the F distribution in Excel can only have integer
   degrees of freedom. If not, the degrees of freedoms will changed to
   integers first. I don't know how to circumvent this problem easily.
   Sure we can write our own functions but it's not worth doing that.

## Tips

1. To unhide a workbook,
   click the "View" tab and then click the "unhide" button in the window group.

1. You can use the hotkey CTRL + Left/Right/Up/Down Arrow to quickly jump to the end of a used range.

1. You can use macros/functions defined in a workbook if it is open.
   So you can use put all your macros/functions into a single workbook
   and just open it for use when needed.
   Or you can put all your macros/functions into "PERSONAL.xlsb" which is a hidden workbook that is always open.

1. insert multiple lines at the same time, select multiple lines, right click and insert

1. after selecting a bunch of cells, right bottom, statistics, you can add more ...
   However,
   hidden cells in the selection are ignore when calculating statistics.

1. On the Home tab, in the Editing group, click the arrow next to the Clear button Button image, and then do one of the following:
   To clear all contents, formats, and comments that are contained in the selected cells, click Clear All.
   To clear only the formats that are applied to the selected cells, click Clear Formats.
   To clear only the contents in the selected cells, leaving any formats and comments in place, click Clear Contents.
   To clear any comments that are attached to the selected cells, click Clear Comments.

1. counting number of selected cells: bottom right bar trick -> select ... -> bottom right, summary

1. trust center -> trust location

## Chart

1. If you select 1 row/column of data with k cells and insert a chart,
   you get a chart of 1 series at k locations.
   However,
   if you select a block of data with m rows and n columns,
   you get a chart of m series at n locations.

## Functions

1. COUNTIF criteria is a string containing logical comparisons,
   criteria is a string containing comparison conditions

1. iVal = Application.WorksheetFunction.COUNTIF(Range("A1:A10"),"Green")

## Questions

1. how to open a workbook as hidden by default? You can hide it manually.

1. How to quickly check sum of a bunch of cells in a large table where no adjacent cells are available?
   Is it posisble to use some kind of prompt diaglog? Actually you can write such a function by yourself.

1. learn how to make plots in excel

1. how to adjust series unit? I don't like big long numbers

1. best way to add unit to y? and multiple lines in legends?

1. bar plot with %?

1. save to xlsx by default?

1. auto adjust column width in Excel 2007

1. the bottom line frame in chart?

1. How to use shortcut to quickly switch between worksheets?
