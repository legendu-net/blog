---
title: Collections and Iterators in C++
created: '2012-10-12T10:45:08-07:00'
date: '2026-11-15T09:15:51-08:00'
authors:
  - bendu
label: collections-and-iterators-in-c++
license: CC-BY-4.0
tags:
  - C++
  - cpp
  - programming
  - list
  - set
  - map
  - iterator
  - collection
  - C/C++
  - vector
---

## Collections

1. Prefer `std::deque` to `std::vector` when the size of the collection is unknown.

1. Suppose set `A` and `B` are two set with the same type
   and set `C` is another set with the same value type but a different comparison function,
   then it is still valid to insert results of set operations
   (union, difference, intersection, symmetric difference and so on)
   on A and B into set `C`.
   It is just that values in C are sorted according to
   the comparison function of `C` not comparison function of `A` and `B`.

1. It is known to all that a set is sorted (according to its comparison function).
   You cannot sort the set in place using `std::sort` with another comparison function.
   To sort elements in the set with another comparison function,
   you have to create a new collection (e.g. a vector), copy the elements over and sort them.

1. You can use `std::set::count` to check whether a set contains a value or not.

1. Removing an element from a set/list/map only
   affects reference to the remove element not references to other elements.
   However,
   removing an element from a vector affects references to elements after the removed elements.
   A good way to works with vector is to operate on it backwards.
   That is iterating a vector backwards,
   removing elements from a vector backwards, etc.

1. `std::map` is similar to `std::set` from many aspect.
   For example,
   `std::map` contains values with unique and sorted keys while `std::set` contains unique and sorted keys.;
   both `std::map` and `std::set` have a `count` method which helps to check whether a `map/set` contains a key or not;
   both `std::map` and `std::set` have a `find` method which helps to find the position of a key in a `map/set`.
   Actually,
   a `std::set` can be considered as a special case of `std::map` where the value is of no interest.

1. The `std::map::at` method is preferred over the `std::map::operator[]`.

1. Associative collections such as `std::map` and `std::set` have methods related binary search
   (e.g., `count` and `find`)
   while sequence collections such as `std::vector` and `std::list` do not have these methods.
   If a sequence collection is sorted (e.g., use `std::sort`),
   you can apply functions `std::count` and `std::find` on it.
   Sequence collections have methods which can access and modify elements at the front and back of the collection
   (e.g., `std::front`, `std::pop_front`, `std::back`, `std::pop_back`)
   while associative collections do not have such methods.
   To access the first and last element of an associative collection,
   you have to use iterators.
   For example,
   to get the last element of a set `x`,
   you can use

   ```
    :::cpp
    *x.rbegin();
   ```

## Iterator

1. The difference between points/iterator is of type std::ptrdiff_t,
   which is essentially a "signed" integer.

1. The result of `std::reverse_iterator::base` decreased
   by 1 is the corresponding (non-reversed) iterator.
   For example,
   if you want to erase the last element from a set `s`,
   you can use

   ```
    :::cpp
    s.erase(--(s.rbegin().base()));
   ```
