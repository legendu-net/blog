UUID: 1cc3477a-802e-4ae0-b210-71acc759bf88
Status: published
Date: 2016-07-09 19:02:28
Author: Ben Chuanlong Du
Slug: install-software-on-mac
Title: Install Software on Mac
Category: Mac OS X
Tags: Mac OS X, Apple, installing software, Homebrew, Remote Desktop

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Homebrew

1. You might encounter link problems when you use the `brew` command to install packages on Mac.
A quick and dirty way to solve the problem is to link the executable file into `$HOME/bin`.
This will not solve all problems, of course.

2. Do not install python using brew as you will end up with 2 copies of python

3. better to use MacVim instead of Vim. 
```bash
brew install macvim
```
The command for MacVim is `mvim`. 
For convenience, 
you can link it to `$HOME/bin/vim`.

4. No readlink on Mac.  Use `greadlink` instead.
You have install the package `coreutils` in order to use `greadlink`.
```sh
brew install coreutils
```

## Remote (Windows) Desktop

The best free one is Microsoft Remote Desktop. 
However, it is available in the US App Repository but not the China App Repository. 
Make sure that you have a US Apple ID if you want to install Remote (Windows) Desktop.
