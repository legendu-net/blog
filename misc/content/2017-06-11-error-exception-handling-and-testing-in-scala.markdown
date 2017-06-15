UUID: 3fac705c-dcf0-4c44-b746-55b3deb16d7a
Status: published
Date: 2017-06-11 11:51:42
Author: Ben Chuanlong Du
Slug: error-exception-handling-and-testing-in-scala
Title: Error/Exception Handling and Testing in Scala
Category: Programming
Tags: programming

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

`assert` means that your program has reached an inconsistent state.
This might be a problem with the current method/function 
(think of it a bit as e.g., HTTP 500 InternalServerError).

`require` means that the caller of the method is at fault 
and should fix its call (think of it a bit as e.g., HTTP 400 BadRequest).
Use `require` whenever you want a constraint on parameters.
Use `assert`, 
whenever you want to make sure some conditions (like invariants) are always true during execution. 
It as a way of testing.

```scala
def assert(assertion: Boolean) { 
    if (!assertion) 
        throw new java.lang.AssertionError("assertion failed") 
} 

def assume(assumption: Boolean) { 
    if (!assumption) 
        throw new java.lang.AssertionError("assumption failed") 
} 

def require(requirement: Boolean) { 
    if (!requirement) 
        throw new IllegalArgumentException("requirement failed") 
} 
```

`assert` (java.lang.AssertionError) – a predicate which needs to be proven by a static code analyser to attempt to prove. 
It is something that you expect the static checker to be able to prove at compile time.

`assume` (java.lang.AssertionError) – an axiom for a static checker. 
It is something that the static checker can rely upon.

`require` (IllegalArgumentException) – Blames the caller of the method for violating the condition. 
Used as a pre-condition. ensuring is a post-condition.
