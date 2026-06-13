---
title: Advanced Use of head and tail
created: '2016-06-06T18:22:00-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: advanced-use-of-head-and-tail
license: CC-BY-4.0
tags:
  - Linux
  - shell
  - command line
  - head
  - tail
  - sed
  - awk
  - rows
  - lines
  - text manipulation
---

It is suggested that you **use Python instead of Shell** to manipulate text files!!

Besides passing an unsigned integer as parameter to the option `-n`,
you can also pass a signed integer to it.
When a signed integer is passed to `-n`,
it means from/to (inclusive/exclusive similar to most programming languages) the row with this index (1-based).
More specifically,
`head -n +/-k` means take rows 1 (inclusive) to `+/-k` (exclusive).
`tail -n +/-k` means take rows `+/-k` (inclusive) to the last row.
Below are some examples to help you fruther understand how it works.

1. Print all but the last `5` lines.

   ```
    # -5 means without the last 5 lines  
    head -n -5 file_name
   ```

1. Print lines 6 and after (i.e., all but the first `5` lines).

   ```
    # +6 means starting from line 6  
    tail -n +6 file_name 
   ```

1. Print lines 10 to 20.

   ```
    head -n 20 file_name | tail -n +10  
    # or you can use (11 = 20 - 10 + 1)
    tail -n +10 file_name | head -n 11
   ```

   Please refer to
   [Print Rows from a Text File](print-rows-from-a-text-file)
   for better ways using `sed` and `awk`.
