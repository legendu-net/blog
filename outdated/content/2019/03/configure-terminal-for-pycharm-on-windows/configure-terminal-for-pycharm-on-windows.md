Status: published
Date: 2019-03-05 01:48:55
Modified: 2021-09-26 16:51:18
Author: Benjamin Du
Slug: configure-terminal-for-pycharm
Title: Configure Terminal for PyCharm on Windows
Category: Computer Science
Tags: programming

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

I personally think it is better to develop in WSL 2 on Windows!

## Ubuntu Shell

1. Install Ubuntu Shell on Windows 10 if it hasn't been installed.

2. File -> Settings -> Tools -> Terminal 

3. Replace the Shell path with `C:\Windows\System32\bash.exe`.


Unfortunately the Python virtual environment created in Ubuntu shell cannot be used by PyCharm
as PyCharm (or more precisely, the Windows File System) does not recognize Linux symbolic links.
