---
title: Working with Class in C++
created: '2012-10-05T10:56:31-07:00'
date: '2026-11-15T09:17:04-08:00'
authors:
  - bendu
label: working-with-class-in-c++
license: CC-BY-4.0
tags:
  - C++
  - destructor
  - programming
  - inheritance
  - override
  - class
  - hiding
  - constructor
---

Illustrative examples for the following discussions can be found
[here](https://github.com/dclong/cearn/tree/master/class).

1. It is suggested that you also provide a default constructor
   if you ever provide a user-defined constructor when writing a C++ class.

1. If you want to allow deleting a derived class from a pointer of the base class,
   you have to make the destructor of the base class `public` and `virtual`
   even if it does nothing.
   If you want to prevent deleting a derived class from a pointer of the base class,
   make the descturctor of the base class `protected` and `virtual`.

1. If you derive a class from a base class,
   the destructor of the base class is called automatically
   so that you do not have to call it manually.

1. If a derived class `D` has a method with the name `fun`,
   then all non-virtual methods with the name `fun` (no matter what signature they have) in its
   base class `B` are `hidden` by the method `fun` in `D`.
   Suppose `d` and `b` are instances of the class `D` and `B` respectively,
   and you invoke the method `fun` through these two instances,
   then everything works OK (in the sense that the `right` method is invoked).
   However, this is different from `overriding`.
   The problem is that `hidden` does not support polymorphism.
   If you have a pointer of the base class `B` pointing to an instance of the
   derived class `D`, and you invoke the method via the pointer,
   then `fun` of the base class `B` will be called.
   To support polymophism, you have to `override` the method `fun` in the base class `B`.
   To do this, you have to mark `fun` as virtual in the base class.
   To help the compiler (and also make your code more readable),
   you can use `override` after the signature of method explicitly.
   [Here](https://github.com/dclong/cearn/tree/master/class/inheritance) is
   an example illustrating problems discussed above.

1. Overriding method must have the same return type as the overridden method.
   (not sure whether this is required in Java)

1. If you write your own version constructor for a class,
   you'd better also provide the copy/move constructor and assignment operator.

1. You'd better not use lvalue references in a class that point to an object outside the class.
   A better way is to pass the object by lvalue reference to methods that need it.
   If you ever decide to use a lvalue reference in a class that point to an object outside the class,
   you must initialize it in the initialization list of a constructor.
   This is because when you initialize a lvalue reference,
   you must point it to a valid object.

1. Generally speaking, member variables should not be declared as public,
   unless they are `static constant`.
   Also you should not declare member variables as `protected` unless
   you are sure that the derived classes want to access these member variables directly.
   If you define a protected member `m` in a base class `B`,
   a derived class `D` can access and modify (if `m` is a data member) `m` in its own class or through its own instances
   but not through other arbitrary object.
   For example, if `b` is an object of the base class `B`,
   you cannot access or modify `b.m` directly in the definition of the derived class `D`.

1. It is suggested that you provide a `to_string` method,
   rather than overriding the `<<` operator.

1. You'd better not use overloading and default parameters at the same time.
   Because this might make compiler fail to find the right version of function/method to call.
   Generally speaking, overloading is more powerful and thus prefereed.

1. Inheritance works with template class,
   i.e., you can derive class from template classes.

1. A `swap` method can make the implementation of copy and move structor unified and thus more conveneint.
   It is suggested that you make the `swap` function `public` (at least `protected`) if you provide one.

1. If a class have many variables to be initialized,
   you can think of initializing non-critical variables in the definition
   of the class and provide public method to access and modify them.
   This make it easier to implement constructors.

1. Always mark a method as `const` if it does not change the state of the object.

1. It is suggested that you initialize member variables in the constructor initializing list
   (after `:` before `{`).
   Surely you can achieve the same by assigning values to member variables in the body of constructors,
   but in this way these member variables are first initialized to default values and then assigned values,
   which is not as efficient.

## Virtuality

The following are some guidelines for virtuality from Herb Sutter.
The original article can be found [here](http://www.gotw.ca/publications/mill18.htm).

13. Prefer to make interfaces nonvirtual, using Template Method.

01. Prefer to make virtual functions private.

01. Only if derived classes need to invoke the base implementation of a virtual function, make the virtual function protected.

01. A base class destructor should be either public and virtual, or protected and nonvirtual.

A few points to add:

1. A virtual method can be overridden by a derived class even if it is private.

1. A class without a public destructor cannot be used by itself.
   It servers as a base class only.
