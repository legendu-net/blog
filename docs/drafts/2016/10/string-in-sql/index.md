---
title: String in SQL
created: '2016-10-20T18:55:31-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: string-in-sql
license: CC-BY-4.0
tags:
  - programming
  - SQL
  - string
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Teradata

regexp_instr
REGEXP_LIKE
REGEXP_REPLACE
REGEXP_SUBSTR

1. trim
   trim specified pad characters or bytes from a character or byte string

1. like %, \_
   like, case-insensitive
   You can also
   `like any (pattern_1, pattern_2, ...)`
   `like all (pattern_1, pattern_2, ...)`

1. Collation can be simply thought of as sort order.

CHAR2HEXINT
convert a character string to hexadecimal representation

• INDEX
• POSITION
get the starting position of a substring within another string

LOWER
convert a character string to lowercase

SOUNDEX
get the Soundex code for a character string

• SUBSTRING
• SUBSTR
extract a substring from another string

TRANSLATE
translate a character string to another server character set

TRANSLATE_CHK
determine if TRANSLATE can successfully translate a character string to a specified server character set

UPPER
convert a character string to uppercase

VARGRAPHIC
convert a character string to VARGRAPHIC representation
