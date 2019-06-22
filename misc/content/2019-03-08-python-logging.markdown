Status: published
Date: 2019-06-22 18:47:20
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

There are at least 2 ways to include traceback information in logging. 

1. Use `logger.exception` to log error messages with traceback information.

2. Use `logger.opt(exception=True).log(...)` to include the traceback information.

## [logging](https://docs.python.org/3/library/logging.html)

### Format keywords

process

levelname

message

## References

https://realpython.com/python-logging/

https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels
