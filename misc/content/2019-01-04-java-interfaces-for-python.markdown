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

## [jpype-project/jpype](https://github.com/jpype-project/jpype)

The most used one currently.

[StartJVM and other upgrading issues with 0.7.0](https://github.com/jpype-project/jpype/issues/498)

## [pyjnius](https://github.com/kivy/pyjnius)

pyjnius looks like a great one. 

### Installation

```bash
pip install Cython
pip install pyjnius
```

### Example with Imported Jar

```
import os
os.environ['CLASSPATH'] = "/path/to/your.jar"
from jnius import autoclass
YourClass = autoclass(path.to.YourClass)
yourObj = YourClass()
```

## py4j 

Too complicated to use ...

## References

https://web.archive.org/web/20170729052824/http://baojie.org/blog/2014/06/16/call-java-from-python/
