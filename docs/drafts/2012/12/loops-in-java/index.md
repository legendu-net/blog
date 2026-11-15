---
title: Loops in Java
created: '2012-12-06T21:46:23-08:00'
date: '2026-11-15T09:17:44-08:00'
authors:
  - bendu
label: loops-in-java
license: CC-BY-4.0
tags:
  - programming
  - loop
  - Java
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. The condition(s) in a regular `for` or `while` loop is recomputed before each iteration.
   Not only the change of loop variables but also other variables involved in the loop condition(s) affect the loop.
   The `break` statement is often used to jump out of a loop.
   Sometimes,
   we want to jump out of nested loops.
   It is hard to use `break` to achieve this.
   One simple way is just change variables involved in the loop condition(s)
   to make the nest loops terminate completely.

1. The foreach loop makes things makes things convenient but it has limitations.
   You cannot (should not) use a foreach loop to change the structure of the container
   (even though you can still use a foreach loop to update elements in th container).
   Consider, for example, the expurgate method.
   The program needs access to the iterator in order to remove the current element.
   The for-each loop hides the iterator, so you cannot call remove.
   Therefore, the for-each loop is not usable for filtering.
   Similarly it is not usable for loops where you need to replace elements in a list or array as you traverse it.

   ```
    :::java
    for(Type elem : someList){
        /* operations */
    }
   ```

1. On a computer support multithreading,
   multiple small loops runs a little (not significant at all) faster than a big loop
   with the same number of iterations.

1. The foreach loop in Java preserves the original order to containers.

## References

https://stackoverflow.com/questions/35010846/does-javas-foreach-loop-preserve-order
