---
title: Tips for AWK
created: '2013-10-19T10:22:17-07:00'
date: '2026-11-15T09:19:38-08:00'
authors:
  - bendu
label: tips-for-awk
license: CC-BY-4.0
tags:
  - tips
  - awk
  - text manipulation
---

[AWK Tutorial](http://www.grymoire.com/Unix/Awk.html)

1. For small structured text files,
   it is suggested that you use the [q](http://harelba.github.io/q/)
   command to manipulate it.

   For complicated logic,
   it is suggested that you use a scripting language (e.g., Python) instead.
   I personally discourage using of `awk`
   unless you have a large file (that q cannot handle)
   and the operations you want do are simple.

1. Basic syntax of `awk`

   ```
    awk 'BEGIN {start_action} {action} END {stop_action}' file_name
   ```

1. Whether to user single or double quote depends on
   whether you use column variables in the expression.
   This is consistent with shell variable substitution.

1. `awk` ignorecase when working on files make unnecessary redundant output
   very annoying, not sure why

1. `awk` does not recognize escaped characters in CSV formatted.
   Make sure that the file `awk` works on is in simple format.

## Field Delimiter

1. The delimiter must be quoted.
   For example,
   if the field delimiter is tab,
   you must use `awk -F'\t'` rather than `awk -F\t`.

1. The filed delimiter of AWK supports can be a regular expression.

   ```
    awk -F'[/=]' '{print $3 "\t" $5 "\t" $8}' file_name
   ```

## Column/Field Filtering/Manipulation

1. Select 1st and 3rd column (separated by tab)

   ```
    awk '{print $1 "\t" $3}' file_name
   ```

1. Sum of the 5th filed.

   ```
    awk 'BEGIN {s=0} {s=s+$5} END {print s}' file_name
   ```

## Rows Filtering/Manipulation

1. Print rows of the file with the first field greater than 3.

   ```
    awk '{ if($1 > 3) print }' file_name
   ```

1. Print Docker image IDs that has no repositories names.

   ```
    docker images | awk '{ if ($1 == "<none>") print $3 }'
   ```

1. Print Docker image IDs whose name contains `che` using regular expression match.

   ```
    docker images | awk '{if ($1 ~ "che") print $3}'
   ```

1. Print rows with 2 fields.

   ```
    awk 'NF == 2' file_name
   ```

   Or more verbosally (and more portable)

   ```
    awk 'NF == 2 {print} {}' file_name
   ```

1. Count the number of fields in each line.

   ```
    awk '{print NF}' file_name
   ```

## References

https://stackoverflow.com/questions/15386632/awk-4th-column-everything-matching-wildcard-before-the
