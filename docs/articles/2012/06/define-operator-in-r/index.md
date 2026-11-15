---
title: Define Operator in R
created: '2012-06-08T00:00:00-07:00'
date: '2026-11-15T09:16:47-08:00'
authors:
  - bendu
label: define-operator-in-r
license: CC-BY-4.0
tags:
  - R
  - operator
  - overloading
  - override
  - programming
---

One thing I do not like R is that operations on String in R
are not as convenient as in other programming languages such as Java, Python and Ruby.
In these 3 programming languages,
you can simply use `+` to concatenate strings while in R you have to use the function `paste`.
The inconvenience result from unable to overload functions and operators in R.
However, you can still define/override operators in R.
For example,
the following code renew the definition of `+` to concatenate two strings.

```
"+" = function(x,y){
    paste(x,y,sep="")
}
```
