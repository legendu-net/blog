---
title: Immutable String vs Mutable String
created: '2013-11-13T22:22:11-08:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: immutable-string-vs-mutable-string
license: CC-BY-4.0
tags:
  - programming
  - string
  - mutable
  - immutable
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

advantage of immutable string:

```
trivially thread safe
    more secure
        more memory efficient in most use cases.
            cheap substrings (tokenizing and slicing)
```

however, if one has to create many small string,
e.g., concatenate strings a lot, immutable string has no advantage.
That's why we have StringBuffer and StringBuilder in Java.
Note that String in Java don't have any mutator methods.
A new string is returned ....
Java String is not suitable for manipulating elements,
use StringBuffer or StringBuilder instead.
The difference is that StringBuffer is synchronized
while StringBuilder is not.
StringBuilder has length method instead of size method.

Java char array has a fixed length, but for printing,
you do can use '\\0' (C-style ending of char array) to indicate the end of a string.

StringBuilder in Java is somehow similar to String in C++.
