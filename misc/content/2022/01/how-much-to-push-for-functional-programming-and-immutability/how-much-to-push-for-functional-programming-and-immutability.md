Status: published
Date: 2022-01-19 14:02:09
Modified: 2022-01-19 14:02:09
Author: Benjamin Du
Slug: how-much-to-push-for-functional-programming-and-immutability
Title: How Much to Push for Functional Programming and Immutability
Category: Computer Science
Tags: Computer Science, programming, functional programming, imperative programming, immutable, mutable, Rust

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Most new programming languages 
(such as Rust, Go, Kotlin, Scala, etc.)
support functional programming style
and have clear distinguishment on mutable vs immutable variables.
So,
is functional programming superior to imperative programming?
What are advantages and disadvantages of them?

1. Functional programming makes it really easy to deal with data in standard ways
    compared to imperative programming.
    However, 
    it might be significantly harder implement certain algorithm in pure functional programming style.
    (It is not a very accurate analog, 
    but I kind of feel that functional programming vs imperative programming
    is a little bit like SQL vs programming languages.
    SQL makes it really easy to process data in standard ways
    but certain data operations are significantly harder to handle in SQL.)

2. Functional programming (or more fundalemntally, immutability) reduces bugs in code
    compared to imperative programming,
    especially in multi-threading or distributed applications. 
    However, 
    functional programming style code
    (especially if not carefully written)
    is usually less performant compared to imperative programming code,
    especially when an algorithm has to mutate large data. 

3. It is suggested that you go with functional programming style 
    and default to use immutable variables/methods (especially in Rust)
    even if you develop a single thread application. 
    If there's a performance hurt due to functional programming,
    you can then optimize the critical part of code 
    (potentially using imperative style) 
    to improve performance.
