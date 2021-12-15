Status: published
Date: 2021-12-04 20:03:49
Modified: 2021-12-13 11:52:29
Author: Benjamin Du
Slug: firenvim-brings-neovim-into-your-browser
Title: Firenvim Brings NeoVim into Your Browser
Category: Computer Science
Tags: Computer Science, Vim, NeoVim, Firenvim, browser

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [Trouble Shooting Firenvim](https://github.com/glacambre/firenvim/blob/master/TROUBLESHOOTING.md#troubleshooting-firenvim)
[Trouble Shooting Firenvim](https://github.com/glacambre/firenvim/blob/master/TROUBLESHOOTING.md#troubleshooting-firenvim)

## Font Size 

Use the following command to adjust font and its size.

    :::vim
    :set guifont=Monaco:h16

Use the following commands to adjust the frame size for editing.

    :::vim
    :set lines=80 
    :set columns=100 

## Troubleshooting

### Disable Hardware Acceleration

`:set lines=30` is very slow due to hardware acceleration in browsers.
Disabling hardware acceleration helps.
Please refer to
[How to Turn Hardware Acceleration On and Off in Chrome](https://www.howtogeek.com/412738/how-to-turn-hardware-acceleration-on-and-off-in-chrome/)
and
[Hardware acceleration and WindowBlinds causes Firefox to crash](https://support.mozilla.org/en-US/kb/hardware-acceleration-and-windowblinds-crash)
on how to disable hardware acceleration in Chrome and Firefox.

## References 

[Firenvim: Neovim inside Your Browser](https://jdhao.github.io/2020/01/01/firenvim_nvim_inside_browser/)

[firenvim](https://github.com/glacambre/firenvim)
