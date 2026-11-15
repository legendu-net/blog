---
title: Selectively Disable Vimperator on Webpages
created: '2017-03-04T13:28:47-08:00'
date: '2026-11-15T09:28:48-08:00'
authors:
  - bendu
label: selectively-disable-vimperator-on-webpages
license: CC-BY-4.0
tags:
  - software
  - Vimperator
  - Vim
  - Firefox
  - browser
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**
You can press `shift + esc` to disable Vimperator on pages and `insert` to enable it again.
This is not good solution as often times you wan to disable Vimperator on a few pages
but still have it enabled on other pages.
You can achieve this by configuring the `~/.vimperatorrc` file.
Below is an example of disabling Vimperator on Google main, calendar, reader and tasks.

```
autocmd LocationChange .*                             js modes.passAllKeys = false
autocmd LocationChange mail\\.google\\.com            js modes.passAllKeys = true
autocmd LocationChange www\\.google\\.com/calendar    js modes.passAllKeys = true
autocmd LocationChange www\\.google\\.com/reader      js modes.passAllKeys = true
autocmd LocationChange mail\\.google\\.com/tasks      js modes.passAllKeys = false
```

Instead of using `autocmd`,
you can also use `ignorekeys`.
Below is an example of disabling Vimperator on Yahoo and Google mail.

```
ignorekeys add mail.yahoo.com
ignorekeys add mail.google.com
```

## Reference

1. [Disable Vimperator Temporarily](http://stackoverflow.com/questions/14271624/disable-vimperator-temporarily)
