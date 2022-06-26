Status: published
Date: 2018-10-29 08:28:14
Modified: 2021-09-26 11:05:01
Author: Ben Chuanlong Du
Slug: use-autojump-to-help-quick-navigation-in-terminal-in-linux
Title: Use Autojump to Help Quick Navigation in Terminal in Linux
Category: OS
Tags: Linux, autojump, cd, terminal, shell, navigation

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

I personally is not a big fun of 
[autojump](https://github.com/wting/autojump) 
and similar tools.
I think it makes things more complicated.

## Installation

Use the following command to install autojump on Ubuntu.
```bash
wajig install autojump
```
Place the following code in your `.bashrc` file and you are good to go.
```bash
if [[ -f /usr/share/autojump/autojump.bash ]]; then
    . /usr/share/autojump/autojump.bash
fi
```

## References

- [autojump](https://github.com/wting/autojump) 