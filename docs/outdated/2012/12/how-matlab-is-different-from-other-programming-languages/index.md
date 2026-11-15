---
title: How MATLAB Is Different from Other Programming Languages
created: '2012-12-13T00:09:40-08:00'
date: '2026-11-15T09:34:39-08:00'
authors:
  - bendu
label: how-matlab-is-different-from-other-programming-languages
license: CC-BY-4.0
tags:
  - C++
  - programming
  - Java
  - SAS
  - R
  - MATLAB
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. MATLAB support command style (like Linux terminal commands).
   This means that you do not have to use parentheses when you call some
   functions, instead, you can use spaces to separate a function and
   its arguments.
   And when an argument of a function is string, you
   do not have to use single quotation mark when you call the function
   using command style. When a function does not take any arguments,
   you can call the function by parentheses with nothing in or you can
   ignore the parentheses and just use the name function to call it.
   For example, to generate a rand number between 0 and 1, you can use
   `rand()` or you can simply use `rand`. This is much more convenient
   compared to many other languages. e.g. R
   However, the support not as seamless as Ruby (in which you can use
   command style and function style freely). Not all functions in MATLAB have
   command versions, and usually you
   cannot use command version of functions in user-defined functions.
   (not very sure whether you can use it in m file or not, check it
   later.)

1. In most languages (e.g. ,C++, Java, SAS, etc),
   it is required that you end a statement with `;`.
   In some other languages (e.g., R), it does not matter much (if write multiple statements on a line in R, `;` can be used to separate them).
   In MATLAB, you are not required to put a `;` at the end of a statement.
   However, it is recommended that you use `;` at the end of each statement,
   otherwise the result of the statument will be printed out to the console.

1. The normal MATLAB statements are continued on new line by putting
   three dots (`...`), which is different from other popular languages.
   Many programming languages allows you to start a new line freely,
   e.g. ,C++, Java, etc. R allows one to start a new line if no ambiguity is introduced.
   Three dots (`...`) is often used in other languages (e.g., R and C++11) for variadic functions.

1. Though MATLAB support multiple styles of syntax, its
   syntax is still more strict than the syntax of R, which make it more
   efficient in the cost of convenience.

1. MATLAB use $\sim$ to stand for logical `NOT`, which is different
   from most of other languages. Usually a programming language uses `NOT`, `!`, or `$<>$` to stand
   for logical `NOT`.

1. MATLAB uses `disp` to display text of array to the console, which is
   different from most other programming languages.
   Most programming languages use functions/routines/methods related
   to words `print` (printf, print, println, etc) and `write` (write, writeln, etc) to print message to the standout put of a file.

1. In other programming languages, you have `packages` (e.g. Java,
   Mathematica and R), `libraries` (e.g. C). In MATLAB, a
   similar concept which is called `toolbox`, however, it is not exactly
   the same as `packages` or `libraries` in other languages.
   You can use functions in a toolbox as long as the toolbox is installed.
   In R, you have to first load a package in order to use functions in it (or you have to full name of the function).

1. To use strings in MATLAB, you must use single quotation marks,
   which is different from many other languages.
   For example, in C/C++ and Java, you have to use double quotation marks;
   in languages which have Linux blood (e.g., R, Python, Bash and so on),
   you can use either double or single quotation marks (though there might be slight difference between single and double quotations).

1. MATLAB is not completely case sensitive. MATLAB is case sensitive
   for variable names and built-in functions. For scripts and functions
   stored in a MATLAB file with a .m extension, case sensitivity is
   preserved on UNIX platforms but not on Windows platforms.

1. Loops in MATLAB is faster than loops in R.
