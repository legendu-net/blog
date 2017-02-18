UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: General Tips for Java
Date: 2016-11-20 19:19:03
Tags: tips, programming, Java
Category: Programming
Slug: general-tips-for-java
Author: Ben Chuanlong Du

## Useful Skills

1. Even if a method returns a value, 
you can use it as if it were a void method. 
This means that it does not hurt for a method to return a value. 
This can be very convenient sometimes. 
For example, if you want to insert an element into a list in order, 
it is natural to define a void method which does the operation for you. 
However, 
you can also make the method return the location where the element is insert to. 
This is what `add` in `ArrayList` does. 
You can use it insert an element only, 
and you can also extract the location information 
(where the element is inserted to) at the same time if you like.

2. If even if you make an object `final`, 
you might still be able to mutate it. 
This is because `final` describes the name of the object,
which means that the variable cannot point to a new address, but the
content of the address (where the variable points to) might still be
changed. For example, if you define 

         `public final int[] a = new int[10]`

you cannot point `a` to another address, but you are
still able to change the elements of `a`, i.e., you're able to
change the value of `a[i]` for $i=0,\ldots,9`\). This is one reason
that defensive copy is preferred when you pass around a mutable
object. Generally speaking, defensive copy is preferred if it
doesn't affect performance badly. Also, if a getter method returns a
mutable object, you'd better make a defensive copy.

3. Always print some indicating information to the console when you
expect some input from the console. Otherwise, you when you run the
application, it waits for your input but you might think that it's
not running. Also if you do an intensive computing in Java, you'd
better print the progress (if you can) to the console. At least you
should print message to the console after the simulation is done!

4. There're many operators in C/C++ which makes which makes operations
faster and calculation faster, e.g. `++`, `–`, `+=`, `\*=`, and so
on. Similarly to C/C++, we can also use them in Java. Specially, for
the increase (`++`) and decrease `–` operator, we can use them both
before and after numerical variables in Java.

5. In many programming languages, we can print out more than one
variables (not necessarily the same type) at a time. In Java, the
method `println()` (or other similar methods) of `System.out` can
only accept one parameter. However, by concatenating different
variables (not necessarily the same type) we can print them out at a
time.

6. We can use `break` to stop current loop, however, sometimes there
might be nested loops and we want to stop all nested loops. To do
this, we can simply modify these loop variables so that all
conditions in the loops are not satisfied.

7. To end a running Java program, we can throw out exceptions, or we
can use method `System.err.println()` to print error information to
the console and end the program.

8. To jump out a single loop, we can use statement `break;`. However,
this doesn't work if there're nest loops. To jump out nested loops,
we can either use `goto` (which is not a good code style) or we can
just modify the loop variables so that the conditions of all loops
are violated.

9. Sometimes after being modified, the code is no longer tidy any more.
We can use `format` button under `source` menu to tidy the code.

10. For multi-threads programs in Java, it's hard to debug the whole
program directly. To make sure that the program works, we can test
each class in the program by writing a testing class for each of
them.

11. We don't have `goto` statement in Java, however we have several ways
to make the program in Java jump to other place.

    - The `break` and `continue` statements allow you to jump out of a
    block in a loop or switch statement.

    - A labeled statement and `break label;` allow you to jump out of
    an arbitrary compound statement to any level within a given
    method (or initializer block).

    - Throwing and catching exceptions allows you to (effectively)
    jump out of many levels of method call. (However, exceptions is
    relatively expensive, and are considered to be a bad way to do
    "ordinary" control flow.)

    - And of course, there is `return`.

12. Since we do not have to assign the returned value of method to any
object in Java, we can use any method as if it is a `void` method.
This means that for any method that is `void` it does not hurt to
declare it as a method that returns some object (or primitive type
value). Actually this might be very convenient sometimes, because by
doing so we can do the operation we want and at the time we have
extra information about the operation. For example, if we want to
insert a value to a sorted array, we can make the method return an
integer which is the index of the inserted place. This extra
information (the index of the inserted place) is highly useful in
may cases.

13. It is expensive to allocating a new block of memory (not only in Java
but also in other languages), so we should avoid allocating new
block of memory all the time. If it is impossible to avoid allocating
memory, we can allocate a bigger memory than needed each time. In
this way, we waste some space, but might save much time.

14. Method `getClass` can return the class of an object.

15. We can use `Arrays.fill` to change all elements of an array at a
time, which is convenient.

16. If we have an array of objects of some super class, we can cast the
whole array to sub class at a time. However, usually we cannot cast
all elements of an array at a time. For example, if we have an array
of `double`, we cannot cast the whole array into `int` at a time,
instead, we must cast each element one by one.

17. If you want let the compiler know that a number you use in your code
is a double precision number you can add suffix `d` to the number.
For example if you want to do double precision calculation for
`3/6`, you can write it as `3/6d` instead of casting integer to
double using `(double)`.

1. Avoid using a local variable which has the same name as an instance variable. 

2. Need hash of a pair of integers. 
You'd better write a pair class instead of using hash of string 
by concatenate the 2 integers.

## Const

1. use final to make an object constant. const is reserved but not used in Java.

## Project Management
1. besides IDE, you can maven or sbt to manage dependencies
