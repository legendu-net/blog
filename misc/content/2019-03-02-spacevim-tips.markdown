Status: published
Date: 2019-03-08 22:08:22
Author: Benjamin Du
Slug: spacevim-tips
Title: Spacevim Tips
Category: Software
Tags: software, SpaceVim, Vim, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
## Installation
```
curl -sLf https://spacevim.org/install.sh | bash
```

## Uninstallation
```
curl -sLf https://spacevim.org/install.sh | bash -s -- --uninstall
```

https://github.com/SpaceVim/SpaceVim/issues/84

https://github.com/SpaceVim/SpaceVim/issues/78

## Tricks & Traps

1. By default SpaceVim enables GUI colors.
    This makes SpaceVim extremely slow in terminals that does not support 24 bits true colors.
    To resolve the performance issue, 
    simplify disable GUI colors by setting `enable_guicolors = false`
    under `[options]` in your SpaceVim configure file `$HOME/.SpaceVim.d/init.toml`.


## Some Useful Key Bindings

SPC b f: format the buffer
SPC t 8: highlight characters that execeeds 80th column
SPC t f: highlight characters that execeeds the fill column

SPC [1-9]	jump to the windows with the specific number

### [Buffers and Files](https://spacevim.org/documentation/#buffers-and-files)

:bn go to the next buffer 
:bp go to the previous buffer 
:e #: go to the previous buffer 
SPC b n go to the next buffer
SPC b p go to the next buffer

## References

https://spacevim.org/documentation/
