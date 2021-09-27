Status: published
Date: 2019-03-27 02:26:33
Author: Benjamin Du
Slug: instal-the-latest-version-of-python-in-ubuntu
Title: Instal the Latest Version of Python in Ubuntu
Category: OS
Tags: OS, Linux, Ubuntu, Python 3, installation, PPA
Modified: 2021-09-26 16:27:42

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

There are a few ways to install a newer version of Python on Ubuntu. 
If you want to completely overwrite the system version of Python,
it is suggested that you install Python with a Python PPA. 
Otherwise, 
it is suggested that you install Python using pyenvs
instead of using Anaconda Python or Linuxbrew
as pyenvs allows you to manage multiple versions of Python easily.

## Through PPA

```Bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
```

## pyenvs

## Anaconda Python 

## Linuxbrew 

1. Install Linux brew. 

2. `brew install python3`

## References

https://websiteforstudents.com/installing-the-latest-python-3-7-on-ubuntu-16-04-18-04/

http://ubuntuhandbook.org/index.php/2019/02/install-python-3-7-ubuntu-18-04/

https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa

