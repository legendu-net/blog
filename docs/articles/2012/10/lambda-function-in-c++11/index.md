---
title: Lambda Function in C++11
created: '2012-10-20T10:35:46-07:00'
date: '2026-11-15T09:16:06-08:00'
authors:
  - bendu
label: lambda-function-in-c++11
license: CC-BY-4.0
tags:
  - C++
  - lambda
  - programming
---

## Lambda Function

Check \[here\[(https://github.com/dclong/cearn/tree/master/lambda)
for illustrative examples for the following discussions.

1. When capture variables,
   you can define new variables in the `[]` of a lambda expression.
   For example,
   if a lambda function need the sum of two double variable `x` and `y`,
   you can use `[s=x+y]` to capture the sum of
   these two variables (by value) instead of capture both of them.

1. Currently the `const` keyword is not in the grammar for captures,
   so that if you cannot capture an object by const reference directly.
   A way to walk around this is to first make a const reference of that object,
   and then capture the const reference by reference.

1. When an object is captured by value,
   it cannot be mutated by the lambda function.
   If you want the lambda function to be able to mutate the capture value,
   you should use the keyword `mutable`, e.g.,

   ```
    [x]()mutable{...};
   ```

1. To capture a member variable `data` in a class,
   you have to capture `this` pointer,
   i.e.,
   you have to use either

   ```
    [this](...){...};
   ```

or

```
    [d=this->data](...){...};
```

Notice that the ways are different.
In the way,
when you use `data`,
it is actually `this->data`.
This means that `data` is always accessed via `this` pointer,
so you can consider it as capture by reference.
The second way is capture by value.
Surely you make it capture by reference by adding `&` before `d`.
This is the preferred over the first way of capturing `this`
if you just want to capture `data` not other member variables.
