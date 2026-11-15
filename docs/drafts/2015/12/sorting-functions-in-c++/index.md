---
title: Sorting Functions in C++
created: '2015-12-16T00:05:32-08:00'
date: '2026-11-15T09:19:44-08:00'
authors:
  - bendu
label: sorting-functions-in-c++
license: CC-BY-4.0
tags:
  - programming
  - C++
  - sort
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

`std::sort`
`std::stable_sort`
`std::partial_sort`

Notice that only `std::stable_sort` is stable sort (at the cost of additional time/space complexity).
It is easy to achieve stable sort using `std::sort` or `std::qsort` by add extra criteria for sorting.
For example, if you have to sort some nodes by size and want to have stable results,
you want use the index/name of the nodes as a secondary sorting criteria.
You can do this by comparing `std::pair` of node size and node index/name.
