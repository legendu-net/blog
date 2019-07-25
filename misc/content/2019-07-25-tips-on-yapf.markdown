Status: published
Date: 2019-07-25 01:17:07
Author: Benjamin Du
Slug: tips-on-yapf
Title: Tips on Yapf
Category: Programming
Tags: programming, Python, yapf, code formatting

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

You can control the behavior of yapf via settings in the file `.style.yapf` under the root directory of your project.

```
[style]
EACH_DICT_ENTRY_ON_SEPARATE_LINE = True
ALLOW_SPLIT_BEFORE_DICT_VALUE = False
```
