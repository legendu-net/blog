---
title: MATLAB IDE
created: '2012-12-04T00:00:00-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: matlab-ide
license: CC-BY-4.0
tags:
  - IDE
  - software
  - MATLAB
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. Command `help` offers help on functions, classes, packages and so on,
   but it support command style only,
   i.e. it can only be used without parentheses.

1. The `Shift+F1` hot key in command window opens the function browser in MATLAB.
   The `F1` hot key opens the help document for function
   where the cursor is.
   The `Ctrl+SPACE` hot key pop out parameter hint for the function where the cursor is.

1. The `Ctrl+C` hot key in command window halts the current execution if any.
   This is helpful if you want to stop a time-consuming evaluation,
   e.g. when you forget to put an semicolon
   after an expression which produces a very large output.
   Note that this can also be dangerous
   if you do want to run a time-consuming program in MATLAB.
   A safe way is to lock the computer
   if you do not have to use it while the code is running,
   or at least you should minimize the MATLAB command window
   so that it will not be interrupted by your misoperation.
