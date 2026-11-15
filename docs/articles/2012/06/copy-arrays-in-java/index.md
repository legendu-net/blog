---
title: Copy Arrays in Java
created: '2012-06-19T13:48:18-07:00'
date: '2026-11-15T09:16:32-08:00'
authors:
  - bendu
label: copy-arrays-in-java
license: CC-BY-4.0
tags:
  - array
  - copy
  - Java
  - programming
---

There are several different ways to copy arrays of object (primitive types) in Java.
However,
the fastest way seems to be `System.arraycopy`.
This methed is implemented using native code and only performs a shallow copy.
Actually most methods for copying arrays in Java perform shallow copy.

```
int arr1[] = {0, 1, 2, 3, 4, 5};
int arr2[] = {0, 10, 20, 30, 40, 50};
// copies 3 elements from arr1 to arr2 
System.arraycopy(arr1, 0, arr2, 0, 3);
```
