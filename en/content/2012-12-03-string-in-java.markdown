UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-02-20 10:58:20
Slug: string-in-java
Author: Ben Chuanlong Du
Title: String in Java
Category: Programming
Tags: Java, programming, string, character

## String

1. String is a immutable class in Java. 
Extensive operations on strings (e.g., `+` in a big loop) is usually very slow before Java 7
(the `+` operator is optimized by the compiler automatically starting from Java 7).
To avoid this problem (in older versions of Java), 
you can use the `StringBuilder` class instead to improve performance. 
The `StringBuilder` class is mutable. 
When you make operations on a `StringBuilder` object, 
the original object is mutated (unlike the `String` class)
and returns the (mutated) original object.
Except improvement of performance, 
the `StringBuilder` class also offer many other useful methods 
for string operations that are not included in the `String` class. 

2. If you want to read or write large text (e.g. more than 100M), 
you can use `BufferedRead` and `BufferedWriter` to improve performance.

3. There is no built-in sort method for String. 
To sort characters in a string,
you can first convert the string into a char array,
sort the char array and convert back.

4. You want to the equals method to compare string most of time 
unless you know for sure that comparing references is the right way.

