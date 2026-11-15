---
title: Choose a Procedure for Modeling in SAS
created: '2015-05-10T21:12:54-07:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: choose-a-procedure-for-modeling-in-sas
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - procedure
  - proc
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. `proc glm` has many advantages over `proc reg` and `proc anova`.
   For example,
   `proc glm` supports categorical variables while `proc reg` does not.
   It is suggested that that you use `poc glm` in place of `proc reg` and `proc anova`.
   The only disadvantage of `proc glm` is that it is computationally heavier
   compared to `proc reg` and `proc anova`,
   but this is usually not a concern at all.
