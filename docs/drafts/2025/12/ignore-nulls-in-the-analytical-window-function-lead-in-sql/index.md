---
title: Ignore Nulls in the Analytical Window Function Lead in SQL
created: '2025-12-17T11:08:59-08:00'
date: '2026-11-15T09:28:34-08:00'
authors:
  - bendu
label: ignore-nulls-in-the-analytical-window-function-lead-in-sql
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - SQL
  - analytical
  - window
  - function
  - lead
  - first_value
  - 'null'
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The analytical window function `lead`
does not support ignoring `NULL` values.
One workaround is to to use the analytical window function `first_value`
which supports ignoring `NULL` values.

```
first_value(my_col IGNORE NULLS) OVER (
  PARTITION BY pcol1, pcol2
  ORDER BY ts
  ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING
)
```

For more discussions,
please refer to
[Chat with Gemini: GoogleSQL Lead Ignoring NULL](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221ZzZSSL-X6cinZUn9Vov7TxTLNtmjdVTw%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.
