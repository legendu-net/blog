---
title: Regular Expression in Bash
created: '2019-04-28T11:53:55-07:00'
date: '2026-06-12T22:31:33-07:00'
authors:
  - bendu
label: regular-expression-in-bash
license: CC-BY-4.0
tags:
  - programming
  - Bash
  - regular expression
  - regex
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[Fish Shell](tips-on-the-fish-shell)
is preferred to Bash/Zsh.
The following content is for Bash/Zsh only.

It is suggested that you **use Python script instead of Shell script** as much as possible.
If you do have to stick with Shell script,
you can use `=~` for regular expression matching in Bash.
This make Bash syntax extremely flexible and powerful.
For example,
you can match multiple strings using regular expression.

```
if [[ value =~ ^(v1|v2|v3)$ ]]; then
    ...
fi
```
