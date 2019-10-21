Status: published
Date: 2019-10-21 18:15:23
Author: Benjamin Du
Slug: argparse-tips
Title: argparse Tips
Category: Programming
Tags: programming, Python, argparse

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. The argument `aliases` does not take a geneartor as input.
  Generally speaking, 
  you should be carefule about using a generator as a generator is essentially an iterator 
  which is invalidated once iterated.
  Use a list instead if you have to iterator a collection multiple times.

2. It seems that the default value for an argument must be specified
    in the first occurrence of the corresponding `add_argument` function.

3. It seems that default value must be specified in the first occurrence.

4. You can check whether an option is defined for a command or not using `'some_option' in args`
  where `args` is a Namespace object returned by `argparse.parse_args`.
  So that you can use `args.level if 'level' in args else 'INFO'` 
  to get the value for the option `args.level` with the fallback value `INFO`.
  You can also convert a Namespace object to a dictionary using the function `vars`,
  so an even easier way of get the value of an option with a fallback value is use `vars(args).get('level', 'INFO')`.


## Optional Positional Arguments

By design, 
positional arguments are always required (which is different from options).
However, 
you can leverage the `nargs` option to achive optional positional arguments.
Basically, 
you use `nargs=*` to let argparse knwo that the positonal argument takes 0 or more inputs.

Below is an example ...
