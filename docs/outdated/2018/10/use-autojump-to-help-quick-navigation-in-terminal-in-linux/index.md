---
title: Use Autojump to Help Quick Navigation in Terminal in Linux
created: '2018-10-29T08:28:14-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: use-autojump-to-help-quick-navigation-in-terminal-in-linux
license: CC-BY-4.0
tags:
  - Linux
  - autojump
  - cd
  - terminal
  - shell
  - navigation
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

I personally is not a big fun of
[autojump](https://github.com/wting/autojump)
and similar tools.
I think it makes things more complicated.

## Installation

Use the following command to install autojump on Ubuntu.

```bash
sudo apt install autojump
```

Place the following code in your `.bashrc` file and you are good to go.

```bash
if [[ -f /usr/share/autojump/autojump.bash ]]; then
    . /usr/share/autojump/autojump.bash
fi
```

## References

- [autojump](https://github.com/wting/autojump)
