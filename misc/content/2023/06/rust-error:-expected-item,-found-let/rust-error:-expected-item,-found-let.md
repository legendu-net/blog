Status: published
Date: 2023-06-17 11:36:33
Modified: 2023-06-17 11:36:33
Author: Benjamin Du
Slug: rust-error:-expected-item,-found-let
Title: Rust Error "error: expected item, found 'let'"
Category: Computer Science
Tags: Computer Science, programming, Rust, error, let, include, variable, static, const, module

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The error message "error: expected item, found 'let'" is commonly encountered in Rust 
when you mistakenly place a `let` statement in an invalid location. 
A `let` statement can only be used within a function 
or a code block inside a function.
It cannot be used placed directly within the body of a module, struct, trait or enum. 
Specially,
you might mistakenly use `let` to define variables directly within a module
where you really meant to define a `static` or `const` variable.
This issue become more tricky if you use macros such as `include!`
to literally include code from another file.
