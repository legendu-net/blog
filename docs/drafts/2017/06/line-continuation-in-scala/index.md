---
title: Line Continuation in Scala
created: '2017-06-22T13:35:34-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: line-continuation-in-scala
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - line continuation
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Scala does not have a line continuation character.
It infers a semicolon always when:

1. an expression can end

1. The following (not whitespace) line begins not with a token that can start a statement

1. There are no unclosed ( or \[ found before

Thus,
to "delay" semicolon inference one can place a method call
or the dot at the end of the line
or place the dot at the beginning of the following line:

```scala
ConditionParser.
    parseSingleCondition("field=*value1*").
    description must equalTo("field should contain value1")

a +
b +
c
```

```scala
List(1,2,3)
    .map(_+1)
```

Wrap it in parentheses.
Note that wrap in curly braces doesn't work.
