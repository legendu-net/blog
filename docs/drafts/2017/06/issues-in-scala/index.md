---
title: Issues in Scala
created: '2017-06-22T13:32:43-07:00'
date: '2026-11-15T09:24:17-08:00'
authors:
  - bendu
label: issues-in-scala
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - issue
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## 2.12

1. Avoid using view of collections.

## 2.11

1. Iterator `++` non lazy, might cause stack overflow issues.
   This issue has been fixed in 2.12.

1. `Stream.filterNot`, not lazy, might cause stack overflow issues.
   `Stream.filter` is good.
   This issue has been fixed in 2.12.

1. Avoid using `view` of collections.
   Iterator is a better alternative most of the time.
