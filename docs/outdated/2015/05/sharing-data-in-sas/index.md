---
title: Sharing Data in SAS
created: '2015-05-17T17:09:52-07:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: sharing-data-in-sas
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - data
  - dataset
  - macro
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

There are basically 2 ways to share data among procedures
and data steps in SAS.
The first way is to use datasets (or SQL table/views),
and the second way is to use global macro variables.
None of the solutions are elegant in my opinion
as both datasets and global variables are "global",
however,
that is you what you can do in SAS.
