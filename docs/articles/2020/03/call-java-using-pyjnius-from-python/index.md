---
title: Call Java Using PyJNIus from Python
created: '2020-03-25T20:15:13-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: call-java-using-pyjnius-from-python
license: CC-BY-4.0
tags:
  - computer science
  - Python
  - PyJNIus
  - Java
  - JVM
---

PyJNIus is a simple-to-use Java interface for Python.
However,
[JPype](https://github.com/jpype-project/jpype)
is a better alternative.

### Installation

```bash
pip install Cython
pip install pyjnius
```

### Example with Imported Jar

```
import os
os.environ["CLASSPATH"] = "/path/to/your.jar"
from jnius import autoclass
YourClass = autoclass(path.to.YourClass)
yourObj = YourClass()
```

Note: Avoid using the same name for an instance varialbe and a method in the same class.
Even though Java is able to distinguish between them
PyJNIus is not able to.
A method will be hide by the instance variable with the same name
if you use the Jar via PyJNIus in Python.
Generally speaking,
it is a bad idea to have the same for an instance variable and a method
as it might confuse other programming languages (e.g., Kotlin) and frameworks too.

## References

- [Java Interfaces for Python](java-interfaces-for-python)

- [PyJNIus](https://github.com/kivy/pyjnius)
