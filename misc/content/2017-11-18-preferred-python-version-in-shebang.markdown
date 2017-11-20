UUID: b1d58ca9-c28e-49c8-a9c4-0ea828fe4a93
Status: published
Date: 2017-11-18 10:26:03
Author: Ben Chuanlong Du
Slug: preferred-python-version-in-shebang
Title: Preferred Python Version in Shebang
Category: Programming
Tags: programming, shell, Python, shebang, version

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**



```
#!/bin/sh
''''which python2 >/dev/null 2>&1 && exec python2 "$0" "$@" # '''
''''which python  >/dev/null 2>&1 && exec python  "$0" "$@" # '''
''''exec echo "Error: I can't find python anywhere"         # '''
```

## Reference

https://stackoverflow.com/questions/18993438/shebang-env-preferred-python-version
