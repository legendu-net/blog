---
title: Count Number of Fields in Each Line
created: '2016-06-13T23:08:03-07:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: count-number-of-fields-in-each-line
license: CC-BY-4.0
tags:
  - programming
  - data manipulation
  - R
  - awk
  - number
  - field
  - text file
---

Sometimes,
a structured text file might be malformatted.
A simple way to verify it is to count the number of fields in each line.

## Using awk

You can count the number of fields in each line
using the following awk command.
Unfortunately,
awk does not take escaped characters into consideration.
So this only works for simple formatted (without escaped characters) text files.

```
:::bash
awk '{print NF}' filename
```

## Using R

There is a function named `count.field` in R.
