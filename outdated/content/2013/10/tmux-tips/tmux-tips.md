Status: published
Author: Ben Chuanlong Du
Date: 2013-10-22 15:04:34
Title: Tips on tmux
Slug: tmux-tips
Category: Software
Tags: tips, tmux, software, remote, screen, terminal
Modified: 2022-01-22 10:57:00

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

Zellij is a better alternative.

1. ctrl + b ?: help

## Split Window

1. ctrl + b ": splitwindow (split top/bottom)

2. ctrl + b %: splitwindow -h (split left/right) 

## Scroll in tmux

1. ctrl + b z: zoom/maximize

2. ctrl + b + o: switch to the next panel

3. Ctrl-b then [ then you can use your normal navigation keys to scroll around (eg. Up Arrow or PgDn). 
    Press q to quit scroll mode.
    Alternatively you can press Ctrl-b PgUp to go directly into copy mode 
    and scroll one page up (which is what it sounds like you will want most of the time)
    You can also scroll up/down line by line using Shift-k 
    and Shift-j (if you're already in scroll mode).

## References

https://gist.github.com/MohamedAlaa/2961058

https://gist.github.com/andreyvit/2921703

