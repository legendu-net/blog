UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Comparision of Linux Emulation Solutions on Windows
Author: Ben Chuanlong Du
Date: 2014-06-13 22:21:09
Slug: comparision-of-linux-emulation-solutions-on-windows
Category: Software
Tags: Virtual Machine, Cygwin, MobaXterm, VirtualBox, Linux Emulation
Modified: 2021-09-25 13:42:57

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
1. Virtual machine based on Virtualbox, etc. is an overkill, 
    generally speaking.
    It provides complete functionalities 
    but is more CPU and memory hangry.

2. WSL 2 is the currently the best solution comes with Windows 10+.
    It is essentially a virtual machine but based on Hyper-V.

3. Cygwin, MobaXterm, etc. are outdated 
    as WSL 2 is an integrated solution in Windows 10+.
