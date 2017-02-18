UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Loops in Java
Date: 2016-07-13 22:19:53
Tags: R, loop, Java, programming, MATLAB
Category: Programming
Slug: loops-in-java
Author: Ben Chuanlong Du

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


1. As is known to all, 
the loop condition in a usual `for` or `while` loop 
is checked before each iteration in almost all programming languages. 
In Java, a loop condition is checked in each
iteration, i.e. the boolean value of the loop condition is
recalculated in each iteration. Not only the change of loop
variables but also other variables involved in the loop condition
affect the loop. While this true for most compiled languages, it's
not the case for most interpreted languages, e.g. R and MATLAB. (...
see whether for each is as R and MATLAB ...)

2. You can use enhanced for loop in java almost any time you want. It
really beautifies your code. Unfortunately, you cannot use it
everywhere. Consider, for example, the expurgate method. The program
needs access to the iterator in order to remove the current element.
The for-each loop hides the iterator, so you cannot call remove.
Therefore, the for-each loop is not usable for filtering. Similarly
it is not usable for loops where you need to replace elements in a
list or array as you traverse it.

        for(Type elem : someList){
            /* operations */
        }

3. On a computer support multithreading, multiple small loops runs a
little (not significant at all) faster than a big loop with the same
number of iterations.

