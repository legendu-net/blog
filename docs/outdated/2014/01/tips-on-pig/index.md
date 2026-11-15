---
title: Tips on Pig
created: '2014-01-09T23:40:44-08:00'
date: '2026-11-15T09:28:18-08:00'
authors:
  - bendu
label: tips-on-pig
license: CC-BY-4.0
tags:
  - programming
  - big data
  - Pig
  - Hadoop
  - tips
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

## Tips

1. Pig uses `--` (at the beginning of lines) to comment out lines.
   It also support C-style comment, i.e., using `/* ... */`

1. Filter out records that you don't want before you do expensive transformations
   such as joining, crossing, etc.

1. Pig uses single quotes instead of double quotes for strings.

1. prefer filtering and then joining rather than joining and then filtering

1. Use dot/period to access fields when use aggregation functions,
   otherwise, use double colons (::) to access fields/columns.
   but this is weird

1. -p or -param

## Common Mistakes

1. forget to assign relation to a name

1. use lower case of functions

1. use double quotes for strings
