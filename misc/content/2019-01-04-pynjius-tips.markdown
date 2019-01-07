UUID: 19b64350-dc23-42f3-be27-521c4b1b2dbf
Status: published
Date: 2019-01-04 09:30:04
Author: Ben Chuanlong Du
Slug: pynjius-tips
Title: Pynjius Tips
Category: Programming
Tags: programming, Python, Java, pyjnius

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

https://github.com/kivy/pyjnius

## Installation
```bash
pip install Cython
pip install pyjnius
```
## Example with Imported Jar
```
import os
os.environ['CLASSPATH'] = "/path/to/your.jar"
from jnius import autoclass
YourClass = autoclass(path.to.YourClass)
yourObj = YourClass()
```

## References
https://web.archive.org/web/20170729052824/http://baojie.org/blog/2014/06/16/call-java-from-python/