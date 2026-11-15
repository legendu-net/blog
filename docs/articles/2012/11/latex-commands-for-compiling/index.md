---
title: LaTeX Commands for Compiling
created: '2012-11-13T00:03:31-08:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: latex-commands-for-compiling
license: CC-BY-4.0
tags:
  - compile
  - LaTeX
  - programming
---

1. LaTeX

   - If your LaTeX code contains only EPS figures, you can use the `latex` command (also OK to use `pdflatex`) to compile your code.
   - If you use bibtex, you have to compile your code using commands `latex`, `bibtex`, `latex` and `latex` in sequence.
   - If you use the `psfrag` package to edit EPS figures (only work for EPS figures), you have to compile your LaTeX code using commands `latex`, `dvi2ps` and `ps2pdf` in sequence.
   - To use the `tex4ht` tool to convert LaTeX to other formats, you have to use the `latex` command to compile. See [this post](<>) for more information.

1. pdflatex

   - If you use non-EPS figures in your LaTeX code, you have to use the `pdflatex` command to compile your code.
   - If you use bibtex, you have to compile your code using commands `pdflatex`, `bibtex`, `pdflatex` and `pdflatex` in sequence.
   - Generally speaking the `pdflatex` command is preferred to `latex`.

1. xelatex

   - For compiling LaTeX code containing CJK characters.

1. pdfTexify

   - A command seen in WinEdt for compiling LaTeX code repeatedly until all issues are resolved. This can be a more convenient alternative to apply commands `pdflatex`, `bibtex`, `pdflatex` and `pdflatex` when you use bibtex in your LaTeX code. Surely one can write bash functions to simplify this process in Linux easily.
