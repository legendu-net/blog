---
title: Debug C/C++ Code Using GDB
created: '2015-04-22T13:58:39-07:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: debug-c-c++-code-using-gdb
license: CC-BY-4.0
tags:
  - programming
  - C++
  - C
  - debug
  - GDB
  - cpp
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. lines use : while functions use ::

1. use relative path from the executable to implementation files!!!

   ```
    :::gdb
    b ../../tree.cpp:31 if knot->name()=="GO:0006139"
   ```

1. it seems that there is a bug in GDB?
   Sometimes the results of running an executable directly and within GDB are different!

## References

<http://www.unknownroad.com/rtfm/gdbtut/gdbtoc.html>
