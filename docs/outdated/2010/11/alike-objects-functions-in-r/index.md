---
title: Alike Objects/Functions in R
created: '2010-11-05T00:19:25-07:00'
date: '2026-11-15T09:31:25-08:00'
authors:
  - bendu
label: alike-objects-functions-in-r
license: CC-BY-4.0
tags:
  - programming
  - regex
  - data frame
  - matrix
  - R
  - warning
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

## Matrix VS Data Frame:

1. The data in a matrix must be of the same type while different columns
   in a data frame can have different types.

1. A data frame is much bigger than a matrix with the same dimension.
   If possible, always use matrix instead of data frame to do computation.
   Especially,
   when you creating arrays using the function `array`,
   you should avoid using a data frame as the data source
   (even if all columns of the data frame have the same type).
   A way to work around this is to first convert a data frame to a matrix
   and then use the matrix as the data source.

1. A data frame has names for rows and columns by default while a matrix not.

## `sub` VS `gsub`

1. The function `sub` substitute only the first occurrence of the string
   that matches the given pattern
   while function `gsub` substitute all occurrences of strings that matches the given pattern.

## `warning` VS `warnings`

3. The function `warning` shows a user-defined warning message
   while the function `warnings` displays previously generated warning messages.
