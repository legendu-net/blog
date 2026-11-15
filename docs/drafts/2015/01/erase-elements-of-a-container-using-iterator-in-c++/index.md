---
title: Erase Elements of a Container Using Iterator in C++
created: '2015-01-29T23:08:20-08:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: erase-elements-of-a-container-using-iterator-in-c++
license: CC-BY-4.0
tags:
  - programming
  - C++
  - iterator
  - erase
  - container
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

@TODO: make a general discuss about removing elements form containers ...

vector -> best to remove backwards ...

You cannot erase elements from a container
using the function `std::for_each`
or the range-based for loop (introduced in C++11).
It is easy to make mistakes while you erases elements using iterator in C++.

the following discussion is for set only

Suppose `numbers` is a container with integer number,
and we want to erase the even numbers from it.
The following code is a correct way to do this.

```C++
for(auto it=numbers.begin(); it!=numbers.end(); ){
    // copy the current iterator then increase it
    auto cit = it;
    ++it;
    if((*cit) % 2 == 0){
        // won't invalidate iterator it, 
        // because it is already pointing to the next element
        numbers.erase(cit);
    }
}
```
