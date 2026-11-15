---
title: Disable Jedi in IPython
created: '2019-10-19T21:06:24-07:00'
date: '2026-11-15T09:21:22-08:00'
authors:
  - bendu
label: disable-jedi-in-ipython
license: CC-BY-4.0
tags:
  - programming
  - Python
  - Jedi
  - IPython
  - autocomplete
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

In the meantime, looks like there is a way one can disable jedi in ipython with Completer.use_jedi: https://ipython.readthedocs.io/en/stable/config/options/terminal.html

Specifically you can use ipython locate profile to find your current profile directory, and edit the ipython_config.py to add c.IPCompleter.use_jedi = False

In jupyter just run a cell with the following contents %config IPCompleter.use_jedi = False

## References

https://tutorials.technology/solved_errors/Slow-tab-completion-on-large-data-object-in-notebook.html
