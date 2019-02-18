Status: published
Date: 2019-02-18 19:53:47
Author: Ben Chuanlong Du
Slug: java-interfaces-for-python
Title: Java Interfaces for Python
Category: Programming
Tags: programming, Python, Java, interface, pyjnius, jpype, py4j

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

pyjnius looks like a great one. 

jpype is perhaps the most used one

py4j is too complicated to use

## [pyjnius](https://github.com/kivy/pyjnius)

### Installation

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
