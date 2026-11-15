---
title: Advanced Data Structures in VBA
created: '2014-08-14T02:09:10-07:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: advanced-data-structures-in-vba
license: CC-BY-4.0
tags:
  - programming
  - VBA
  - data structure
  - dictionary
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.

## Dictionary/Hashtable

1. Set a reference to MS Scripting runtime

   ```
    Set dict = CreateObject("Scripting.Dictionary")
   ```

or

```
    Dim dict As New Scripting.Dictionary 
```

2. Example of use:

   ```
    If Not dict.Exists(key) Then 
        dict.Add key, value
    End If 
   ```

1. Don't forget to set the dictionary to Nothing when you have finished using it.

   ```
    Set dict = Nothing 
   ```

## Your Own Data Structure

You can define your own type in VBA.

```
    Dim numbers = New Integer() {1, 2, 4, 8}
    Dim doubles = {1.5, 2, 9.9, 18}

    Dim myarray As Variant
    myarray = Array("Cat", "Dog", "Rabbit")
```
