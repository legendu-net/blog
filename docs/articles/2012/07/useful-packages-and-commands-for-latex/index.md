---
title: Useful Packages and Commands for LaTeX
created: '2012-07-29T11:37:43-07:00'
date: '2026-08-11T22:19:14-07:00'
authors:
  - bendu
label: useful-packages-and-commands-for-latex
license: CC-BY-4.0
tags:
  - color
  - programming
  - list
  - LaTeX
  - package
  - bibliography
  - enumerate
  - formula
  - math
  - graphics
---

<img src="/media/latex/latex.gif" height="200" width="240" align="right"/>

## Math Packages

1. \\usepackage\{amssymb}
   - popular math fonts
1. \\usepackage\{dsfont}
   - `\mathds` font
1. \\usepackage\{bm} % bold math symbols
   - bold math symbols
1. \\usepackage\{amsmath}
   - math formulas.
1. \\usepackage\{amsthm}
   - theorem environments
   - proof enviroment

## List Packages

1. \\usepackage\{enumerate}
   - universal list

## Graphics Packages

1. \\usepackage\{ifpdf}
   - allow including figures without extensions and select the right type of figures according to the compiler used
1. \\usepackage\{graphicx}
   - for including pictures
   - the graphics driver is selected automatically if none is specified (via arguments of the package)
1. \\usepackage\{psfrag}
   - for editing eps figures in Latex (e.g., replacing text)
   - need to compile using command `latex`, `dvips` and `ps2pdf` in sequence
1. \\usepackage\{epsfig}
   - for including eps figures

## Bibliography

1. \\usepackage\{natbib}
   - for citing refernce
   - compatible with bibtex
   - compile using `pdflatex/latex`, `bibtex`, `pdflatex/latex`, `pdflatex/latex`, `pdflatex/latex` in sequence
   - some Latex IDE (e.g., WinEdt) has a single button/command (PDFTexify) for simplifying the compiling process

## Color

1. \\usepackage[usenames,dvipsnames]\{color}
   - using color by name

## Mutiple Files

1. You can use command `\input` or `\include` to include Latex source files.
   Generally speaking,
   `\input` is preferred over `\include`.
1. \\usepackage\{subfiles}
   For more information, please refer to [wiki book](http://en.wikibooks.org/wiki/LaTeX/General_Guidelines).

## Chinese Packages

1. \\usepackage\{xeCJK}
   - no need if use ctexart, ctexbook and so on
1. \\usepackage\{fontspec}
   - choose font theme
1. \\setCJKmainfont{Adobe Song Std}
   - use adobe fonts as the main font
