---
title: Tips on Vimperator
created: '2013-10-22T14:55:48-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: tips-on-vimperator
license: CC-BY-4.0
tags:
  - tips
  - software
  - Vimperator
  - Firefox
  - Vim
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Use Vimium instead.

## Confliction with Some Webpages

Some web applications (e.g., Google apps, MS Apps, RStudio, etc.) have their own keybindings,
and they do not cowork with Vimperator.
Having Vimperator enabled on these web apps/pages make both fail to work.
Please refer to
[Selectively Disable Vimperator on Webpages](selectively-disable-vimperator-on-webpages)
on how to selectively disable Vimperator on some web apps/pages.

## Enable/Disable Vimperator

Press `Shift + ESC` to temporarily disables Vimperator.
Press it again or press `insert` to enable Vimperator.

### Tab Navigation

1. `gt` or `ctrl + n`: go to the next tab

1. `gT`: go to the previous tab

1. `d`: close the current tab

1. `u`: reopen last closed tab

1. `o`: open a new page in the current tab

1. `t`: open a new page in a new tab

### Page Navigation

1. `ctrl + l`: focus on the search/url bar

1. when using f/F for navigation,
   you can also use words in the link that you want to navigate to instead of numbers.
   This make things very convenient.

1. use :hardcopy to print a web page

### Zomm In/Out

1. `zi`: zoom in

1. `zo`: zoom out

1. `zz`: reset zoom

### Text Manipulation

3. `gi`: goto the textbox on the page and focus on it

1. `y`: yanks the current link to the clipboard

1. c, v

1. :bma -f=toolbar/blogs -k=...

1. use :! to run command, but how can I can run user-defined command?

1. you can define your own vimperator command to simply important jobs ...

1. or alternatively you can do: o or t and then ctrl + v and then edit on the link ... cool!!!

## Links

1. <http://sysphere.org/~anrxc/j/articles/vimperator/>

1. <http://superuser.com/questions/16286/vimperator-and-ctrlk>

1. <http://sheet.shiar.nl/vimperator>

## Questions

1. sometimes no link, but can click (button, etc.), how to emulate a mouse left/right click even in vimperator?
