---
title: LaTeX for Chinese
created: '2012-11-13T00:04:39-08:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: latex-for-chinese
license: CC-BY-4.0
tags:
  - LaTeX
  - Chinese
  - programming
  - TeX Live
  - XeTex
  - Linux
  - fonts
  - markup
---

1. `xetex` is the state-of-art way for dealing with Chinese type setting.
   You can install `xetex` on Debian series of Linux distributions (Debian, Ubuntu, Linux Mint, etc.)
   using the following command.

```bash
sudo apt install texlive-xetex
```

You can use command `xelatex` to compile.
The utf-8 format is preferred.

There are 2 good ways for writing Chinese doc using LaTeX (TeX Live) in Linux.
You can use either the `ctex` or `xeCJK` package.
`ctex` is based on `xeCJK` and is more convenient,
however `xeCJK` is more customizable.
The following are minimum example using `ctex` and `xeCJK` respectively.

```Tex
\documentclass{article}
\usepackage{ctex}
\begin{document}
中文 English 
\end{document}
```

```Tex
\documentclass{article}
\usepackage{xeCJK}
\begin{document}
中文 English 
\end{document}
```

Both template uses the Fandole fonts coming with Tex Live by default (without manually specification of fonts to use).
With Tex Live 2015 and above,
the configuration is done automatically and no hassle of manual configuration.
Both `ctex` and `xeCJK` need `xelatex` (see below) to compile.

```bash
xelatex test.tex
```

Required packages (`texlive`, `xelatex`, `ctex`, `xeCJK`, etc.) can be installed
on Debian sereis of Linux (Debian, Ubuntu, Linux Mint, etc.)
using the following command.

```bash
sudo apt install texlive texlive-xetex texlive-lang-cjk
```

The following command installs all LaTeX components that I personally use frequently.

```bash
sudo apt install texlive latex-beamer wiki2beamer dvipng texlive-xetex texlive-lang-cjk texstudio
```
