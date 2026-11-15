---
title: Regular Expression in R
created: '2012-11-14T11:56:44-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: regular-expression-in-r
license: CC-BY-4.0
tags:
  - R
  - regex
  - programming
  - CRAN
  - regular expression
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

There are two flavors of regular expression in R.
One is the regular expression (grep, sub, etc.) comes with base.
The other good one comes with the stringi package.
Both of the versions of regular expression support modifiers.
Generally speaking, regular expression modifiers overwrite function options if confliction happens.

### Regular Expression in the `stringi` Package

1. `.` matches anything except (by default) `\n`
   which is very confusing and error-prone
   as it is not the default behavior in other versions of regular expression.
   The modifier `(?s)` changes the default behavior of `.` and matches `\n`.

## Regular Expression in the `base` Package

1. Use `regexpr` instead of `grepl` in some cases if you want to check whether something exists.

1. Be default, many functions use regular expression match.
   If you do not want to use regular expression match,
   turn it off using the option `fixed = TRUE`.
   For example,
   if you want split strings by `|` using the function `strsplit`.
   You have to use

```R
strsplit(str, "|", fixed = TRUE)
```

instead of

```R
strsplit(str, "|")
```

which has `fixed = FALSE`.
