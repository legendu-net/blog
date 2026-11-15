---
title: Good Ways to Do Scientific Computing
created: '2012-06-15T19:07:49-07:00'
date: '2026-11-15T09:17:06-08:00'
authors:
  - bendu
label: good-ways-to-do-scientific-computing
license: CC-BY-4.0
tags:
  - research
  - scientific computing
---

1. Break down the work into smaller modules and develop pipelines (consists of module) for the work.
   Be sure to save (important) intermediate results so that you can resume failed modules withouting rerunning succeeded ones.

1. Manage your project in GitHub and use issues to manage tasks to do and their priorities.

1. Keep your code clean.
   Make sure to follow good coding (especially naming) styles no matter which programming language you use.

1. Write help documents for your code (classes, methods, etc.)
   and keep a up-to-date readme file (explaining design, TODO or refer to other docs) for your project.
   Bullets 2 and 3 are critical to make sure sustainable progress on projects that last for a long time.

1. Use seeds when you generate random numbers.
   This makes sure that your work can be reproduced later.

1. Test running your code using a small dataset or complexity degree
   to estimate the time needed to run at full scale.

1. Update the progress of running regularly if a program is time-consuming.
   It is good practice to log both the time elapsed and the amount of work that has been done
   so that you can estimate the ETA.
