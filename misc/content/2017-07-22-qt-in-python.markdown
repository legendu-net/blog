UUID: 6f158ee8-c631-40c8-aaef-b4087e84868b
Status: published
Date: 2017-10-22 12:34:04
Author: Ben Chuanlong Du
Slug: qt-in-python
Title: Use Qt in Python
Category: Programming
Tags: programming, GUI, Python, QT, PyQT

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Both PyQt (developed by Riverbank) and PySide2 (official Python bindings from Qt) are great.
They have very similar APIs.
However, 
PySide2 has a more friendly LGPL licence. 
Personally, 
I prefer PySide2.

## Installation 
```
wajig show libclang-dev cmake
pip install PySide2
```

## Git Repository

git clone git://code.qt.io/pyside/pyside-setup.git

## PyQt
```
QtCore.QCoreApplication.instance().quit 
# vs
QtGui.qApp.quit vs QtGui.QMainWindow (self.close)
```
## Tutorial

https://build-system.fman.io/python-qt-tutorial

https://wiki.qt.io/Qt_for_Python_Tutorial_HelloWorld

https://wiki.qt.io/Qt_for_Python_Tutorial_HelloQML

https://wiki.qt.io/Qt_for_Python_Tutorial_HelloQMessageBox

https://wiki.qt.io/Qt_for_Python_Tutorial_ClickableButton

https://wiki.qt.io/Qt_for_Python_Tutorial_SimpleDialog

https://wiki.qt.io/Qt_for_Python_Tutorial:_Data_Visualization_Tool

https://wiki.qt.io/Qt_for_Python_Signals_and_Slots

https://wiki.qt.io/Qt_for_Python_UsingQtProperties

https://wiki.qt.io/Qt_for_Python_DBusIntegration

https://wiki.qt.io/Qt_for_Python_UiFiles

## References


https://www.qt.io/qt-for-python

https://wiki.qt.io/Qt_for_Python/Tutorial

https://wiki.qt.io/Differences_Between_PySide_and_PyQt

http://zetcode.com/gui/pyqt4/firstprograms/

http://openbookproject.net/thinkcs/python/english3e/events.html 
