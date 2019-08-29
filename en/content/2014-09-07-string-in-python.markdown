Status: published
Date: 2019-08-29 00:38:10
Author: Ben Chuanlong Du
Slug: string-in-python
Title: String in Python
Category: Programming
Tags: programming, Python, string, str, character

1. `\` needs to be escaped (i.e., use `\\`) in triple quotes.


2. There are a few ways to write a long string in Python.
    The first way is of course to have the long string on the the same line,
    which can be ugly.

        long_string = 'This is a very looooooooooooooooooooooooooooooooooooooooooooooooooooooong string.'

    The second way is to use `+` to concatenate multiple string,
    which is not recommended.

        long_string = 'This is a very' +
            'loooooooooooooooooooooooooooooooooooong string.'

    The third way is to use triple quotes.
    However,
    whites spaces are kept literally in a triple-qutoe string,
    which might not be what you want.

        long_string = '''This is a very
            loooooooooooooooooooooooooooooooooooooong string.
            '''

    The fourth way is to use parentheses which avoids the side effect of white spaces.

        long _string = (
            'This is a very'
            'looooooooooooooooooooooooooooooooooooong string.'
            )

    The last way is to use `\` to break a string into multiple lines
    if you don't like the parentheses way.

        long_string = 'This is a very' \
            'looooooooooooooooooooooooooooooooooong string.'

2. Since the `str` class is immutable in Python,
    no method of the `str` class is in-place.
    Instead,
    all methods of the `str` class returns a new copy of string.

3. The method `str.capitalize` capitalizes the first letter of a string.
    The method `str.title` capitalizes each word.

4. The method `str.replace` replaces an old string with a new string.

5. There is no method named `contains` in the `str` class.
    You can either use the `in` keyword (preferred)
    or `str.find` to perform substring match.

        " " in "a b"
        # or
        'a b'.find(' ')

## String Prefix

1. f, r, b

2. Notice that prefixes `f` and `r` can be used together 
  and only these prefixes can be used together.
