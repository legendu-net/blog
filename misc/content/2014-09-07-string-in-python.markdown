UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2017-11-18 09:49:58
Author: Ben Chuanlong Du
Slug: string-in-python
Title: String in Python
Category: Programming
Tags: programming, Python, string, character

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. `\` needs to be escaped (i.e., use `\\`) in triple quotes.


2. `\` to break a line like bash, but it has undesirable effect on string,
or you can use triple quotes
```Python
"""..."""/'''...''', 
```
it also include whatever white space you type in
or use `+` to concatenate strings (but not good for large string)
use 
```Python
(
"This line contains"
"a very long string"
"for illustration purpose."
) 
```
instead.
No extra white spaces added.

2. no method of Python's string class is in place
String is immutable in Python.

3. The method `str.capitalize` capitalizes the first letter of a string.
The method `str.title` capitalizes each word.

4. The method `str.replace` replaces an old string with a new string.

5. there is no contains method in the string class, 
you can either use str.find or the `in` keyword to perform substring match.
```Python
'a b'.find(' ')
" " in "a b"
```
the `in` keyword is suggested ...

