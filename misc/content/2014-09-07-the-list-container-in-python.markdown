UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-03-11 15:54:38
Author: Ben Chuanlong Du
Slug: the-list-container-in-python
Title: The List Container in Python
Category: Programming
Tags: programming, Python, list, container

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. almosts all methods of list are in place

2. use + to combine list

3. pop is inplace and returns the removed element.

4. To get unique elements in a list, 
you can first coerce the list to a set and then convert the set back to a list.

        unique_list = list(set(alist))

2. To check whether an object `x` is a in a list `alist`, 
you can use 

        `x in alist` 

If you want to know the position of the element,
use a Look Before You Leap (LBYL) style with a conditional expression as below.

        i = alist.index(x) if x in alist else None


