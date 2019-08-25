Status: published
Date: 2019-08-25 21:11:08
Author: Benjamin Du
Slug: pylint-tips
Title: pylint Tips
Category: Programming
Tags: programming, Python, pylint, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


## pylint

1. Show ERROR messages only.
```
pylint -E some_script.py
```

2. Show ERROR and WARNING messages only.
```
pylint --disable=R,C some_script.py
```

## References

https://stackoverflow.com/questions/31907762/pylint-to-show-only-warnings-and-errors
