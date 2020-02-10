Status: published
Date: 2020-02-09 15:14:50
Author: Benjamin Du
Slug: take-screenshot-in-python
Title: Take Screenshots in Python
Category: Programming
Tags: programming, screenshot, Python, PIL, Pillow, PyQt5

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Pillow

    :::python
    PIL.ImageGrab.grab(bbox=(10, 10, 510, 510))

You can further crop the screenshot into smaller images using the `Image.crop`.

## PyQt5

## References

https://pillow.readthedocs.io/en/stable/reference/Image.html