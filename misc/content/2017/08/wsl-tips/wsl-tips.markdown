Status: published
Date: 2017-08-26 23:23:44
Author: Ben Chuanlong Du
Slug: wsl-tips
Title: Tips on WSL 2
Category: OS
Tags: Linux, WSL, WSL 2, Windows, BashOnWindows, Bash on Windows, tips
Modified: 2021-09-09 12:45:13

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation & Update 

Run the following command in an command window with administrator privileges to install WSL 2.

    :::shell
    wsl --install

Run the following command to check the version of WSL.

    :::shell
    wsl -l -v

Run the following command in a PowerShell to check build information of WSL 2.

    :::PowerShell
    (gcm wsl).Version

Run the following command to update WSL 2.

    :::shell
    wsl --update

For more details,
please refer to
[Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
.

## General Tips

1. You can shutdown WSL using the command `wsl --shutdown`.

## GUI for WSL 

1. [cmder](http://cmder.net/) is a good alternative UI for WSL (and also PowerShell and CMD).

2. The opensource software Windows Terminal from software is the best terminal emulator for Windows.
    Please refer to posts 
    [My WSL2 and Windows Terminal setup](https://garrytrinder.github.io/2020/12/my-wsl2-windows-terminal-setup)
    and
    [Getting started with Windows New Terminal + WSL (Windows Subsystem for Linux)](https://medium.com/@bhavsec/getting-started-with-windows-new-terminal-and-wsl-6b8fbd10ce17)
    on how to set it up for WSL.

## Enable SSH into WSL

[THE EASY WAY how to SSH into Bash and WSL2 on Windows 10 from an external machine](https://www.hanselman.com/blog/the-easy-way-how-to-ssh-into-bash-and-wsl2-on-windows-10-from-an-external-machine)

## Access Linux Filesystems from Windows 

https://blogs.msdn.microsoft.com/commandline/2016/11/17/do-not-change-linux-files-using-windows-apps-and-tools/

With the 1903 update, users can access Linux Filesystem from Windows directly.


## General Tips

2. All windows disks are mounted under `/mnt`. 
    You can visit all Windows files/directories that do not require admin privilige in WSL. 
    However, 
    if you want to visit files/directories that require admin privilige, 
    you have to run WSL with admin and visit these files/directories using sudo in WSL.

3. You'd better use files names that work both in Windows and Linux, 
  otherwise, weird behavior might happen. 

4. Shift + Right Click -> "Open CMD here ..."

5. Starting with Win 10 Creator Update, Ubuntu 16.04 is available. if you installed old Ubuntu bash,
    you need to first uninstall it and then reinstall again to get Ubuntu 16.04.
    Upgrade to Ubuntu 16.04
    https://www.howtogeek.com/278152/how-to-update-the-windows-bash-shell/



## Copy and Paste

Another solution would be to enable "QuickEdit Mode" and then you can paste by right-clicking in the terminal.

To enable QuickEdit Mode, right-click on the toolbar (or simply click on the icon in the upper left corner), select Properties, and in the the Options tab, click the checkbox next to QuickEdit Mode.

With this mode enabled, you can also copy text in the terminal by clicking and dragging. Once a selection is made, you can press Enter or right-click to copy.



## Daemon/Service

You cannot run daemon/services in WSL currently. However, it might be supported in future.

## Samba Remote File System

cannot mount samba in WSL currently.
samba requires kernelspace while WSL only implements a userspace.


## References

- [Docker not running on Ubuntu WSL - Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running? [closed]](https://stackoverflow.com/questions/61592709/docker-not-running-on-ubuntu-wsl-cannot-connect-to-the-docker-daemon-at-unix)

- [Docker in WSL](http://www.legendu.net/misc/blog/docker-in-WSL)

- https://towardsdatascience.com/dual-boot-is-dead-windows-and-linux-are-now-one-27555902a128

- [WSL 2 Filesystem](http://www.legendu.net/misc/blog/wsl-2-filesystem)