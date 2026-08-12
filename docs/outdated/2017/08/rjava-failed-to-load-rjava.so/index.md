---
title: rJava Failed to Load rJava.so
created: '2017-08-06T08:01:26-07:00'
date: '2026-08-11T22:19:33-07:00'
authors:
  - bendu
label: rjava-failed-to-load-rjava.so
license: CC-BY-4.0
tags:
  - programming
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

\*\*
Things under legendu.net/outdated are outdated technologies
that the author does not plan to update any more.
Please look for better alternatives.
\*\*

rJava failed to load rJava.so and libjvm.so

Reconfigure Java for R using the command below resolves the issue.

```
sudo R CMD javareconf
```
