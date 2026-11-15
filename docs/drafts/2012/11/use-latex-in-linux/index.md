---
title: Use LaTeX in Linux
created: '2012-11-10T07:49:45-08:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: use-latex-in-linux
license: CC-BY-4.0
tags:
  - LaTeX
  - TeX Live
  - Linux
  - software
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. `Texlive` is the most popular package for LaTeX in Linux.

1. When installing texlive in linux,
   you'd better install the full version to avoid missing packages.
   For example, in Debian you can do this using the following command.

   ```
    sudo apt install texlive-full
   ```

```bash
# minimum LaTex
sudo apt install texlive texinfo
# Chinese support
sudo apt install texlive texinfo texlive-xetex texlive-lang-cjk
# GUI
sudo apt install texstudio dvipng
# full LaTex and GUI
sudo apt install texlive-full texstudio dvipng
```
