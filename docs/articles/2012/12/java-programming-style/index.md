---
title: Java Programming Style
created: '2012-12-03T00:00:00-08:00'
date: '2026-11-15T09:17:44-08:00'
authors:
  - bendu
label: java-programming-style
license: CC-BY-4.0
tags:
  - style
  - Java
  - programming
---

## Good Writing Style

1. It is recommend to always use `{}` if even there is only one statement inside it.
   The reason is that you never know whether you are going to add more statements into it or not.
   And it will make the code more readable.

1. Feel free to declare the variable in the smallest `{}` block possible.
   The compiler will optimize this kind of code for us.
   So it is better to make the code more readable.

1. It is always good to write code similar to how you would solve the problem naturally.
   It is easy to make mistakes when we try to make the code more concise.
   Unless you can dramatically improve the performance of the code,
   do not change the code for conciseness.

1. Avoid using a same name for a different types (instance, local and argument) of variables.
