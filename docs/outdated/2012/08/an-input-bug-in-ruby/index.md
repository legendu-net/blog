---
title: An Input Bug in Ruby
created: '2012-08-06T11:28:52-07:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: an-input-bug-in-ruby
license: CC-BY-4.0
tags:
  - programming
  - Bash
  - Ruby
  - bug
  - terminal
  - IO
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

<img src="/media/computer/bug.jpg" height="200" width="240" align="right"/>

If you run a ruby program though Bash
and the ruby program read multiple inputs from the console,
all inputs will be the same as the first argument.
I'm not very sure how to solve this problem.
