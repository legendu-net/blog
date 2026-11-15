---
title: Tuple in SAS
created: '2015-05-26T02:34:45-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: tuple-in-sas
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - tuple
  - comma
  - space
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

A tuple can be used both in a sql procedure or a data step.
Values are usually separated by commas,
e.g., `(v1, v2, v3)`.
However, commas are not necessary.

```SAS
where x in (v1, v2, v3) 
```

can also be

```SAS
where x in (v1 v2 v3) 
```
