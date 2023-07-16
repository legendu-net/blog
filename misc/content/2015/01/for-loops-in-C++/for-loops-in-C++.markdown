UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-01-01 14:03:21
Author: Ben Chuanlong Du
Slug: for-loops-in-C++
Title: For Loops in C++
Category: Computer Science
Tags: programming, C++, for loop, container, range
Modified: 2015-03-01 14:03:21

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

There are 3 for loops in C++,
the usual for loop, the range-based for loop (introduced in C++11) and the `std::for_each` for loop.

1. Both the range-based for loop and the `std::for_each` for loop 
applies operations on each eleemnt in a specified container/range.
Both of them are able to mutate elements of a container/range,
but you should never use them to erase elements from a container.
You have to use the usual for loop to erase elements from a container.

2. It is suggested that you use the range-based for loop (introduced in C++11)
in place of `std::for_each` when applicable 
as the range-based for loop is simpler and more readable.

