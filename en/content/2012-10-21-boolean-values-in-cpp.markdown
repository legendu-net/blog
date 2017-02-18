UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-02-19 13:47:49
Slug: boolean-values-in-cpp
Author: Ben Chuanlong Du
Title: Boolean Values in C++
Category: Programming
Tags: boolean, C++, programming

## Boolean Values

1. Boolean expressions are evaluated from left to right (the same in Java),
so it is totally OK to write code like 

        if(a<x.size() && x[a]){
            ...
        }

where `x` is a vector.

2. There is no `&&=` and `||=` operators in C++,
instead you can use `&=` and `|=`.
Though `&=` and `|=` are not specially for boolean values, 
they work perfectly for boolean values.

3. If the numbers you work with support infinity or NaN, 
boolean expressions become tricky. 
For example, suppose `nan` is a varialbe representing Nan,
both `2 < nan` and `2 >= nan` return `false`,
which is not what we want. 
A safer way is to first check whether numbers involved are NaNs. 
Hopefully, ternary boolean type will be introduced into C++ in future. 


