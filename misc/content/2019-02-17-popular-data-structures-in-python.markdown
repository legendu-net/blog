Status: published
Date: 2019-02-17 19:53:49
Author: Benjamin Du
Slug: popular-data-structures-in-python
Title: Popular Data Structures in Python
Category: Programming
Tags: programming, Python, data structure

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## list

1. `list` is essentially a resizable array of objects in Python.

1. Almosts all methods of list are in-place.

2. use `+` to concatenate 2 lists.

3. `list.pop` is inplace and returns the removed element.

4. To get unique elements in a list,
    you can first coerce the list to a set and then convert the set back to a list.

        unique_list = list(set(alist))

2. To check whether an object `x` is a in a list `alist`,
    you can use

        x in alist

    If you want to know the position of the element,
    use a Look Before You Leap (LBYL) style with a conditional expression as below.

        i = alist.index(x) if x in alist else None

## tuple

`tuple` is the immutable version of list.

## dict

`dict` is ordered hash table in Python 3.6+.

## str

## pandas.DataFrame