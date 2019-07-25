Status: published
Date: 2019-07-25 00:43:09
Author: Benjamin Du
Slug: python-logging
Title: Python Logging
Category: Programming
Tags: programming, Python, logging, loguru

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## [loguru](https://github.com/Delgan/loguru)

The best logging package for Python!

Log an exception using luguru and then throws an exception without logging redundant error messages.
```
def throw(_, error, message, *args, **kwargs):
    message = message.format(*args, **kwargs)
    logger.opt(depth=1).error(message)
    raise error(message)

logger.__class__.throw = throw

logger.throw(ValueError, "Something bad happened")
```
https://github.com/Delgan/loguru/issues/120


## [logging](https://docs.python.org/3/library/logging.html)

### Format keywords

process

levelname

message

## References

https://realpython.com/python-logging/

https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels
