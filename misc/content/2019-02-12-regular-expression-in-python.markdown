Status: published
Date: 2019-02-12 19:53:02
Author: Benjamin Du
Slug: regular-expression-in-python
Title: Regular Expression in Python
Category: Programming
Tags: programming, Python, regex, regular expression

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


[Online Regular Expression Tester](https://regex101.com/)


1. (?i) case-insensitive matching

2. `re.match` matches the regular expression pattern from the beginning of the string
    while `re.search` matches the regular expression pattern anywhere in the string.
    Generally speaking `re.search` is preferred over `re.match`
    as it is more flexible.

3. Passing `re.DOTALL` to the argument `flag` makes the dot (`.`) matches anything
    including a newline (by default the dot does not matches a newline).
