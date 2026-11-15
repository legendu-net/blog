---
title: Graphics in LaTeX
created: '2012-11-13T00:02:34-08:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: graphics-in-latex
license: CC-BY-4.0
tags:
  - image
  - vector
  - LaTeX
  - graphics
  - programming
---

1. Generally PDF figures are preferred for LaTeX code.

1. There are many useful commands in Linux for converting between different types of figures, e.g., `convert`, `pdf2ps`, etc. So it does not matter much which types of figures you produce. You can always convert them into other format when needed.

1. The `psfrag` package is useful for editing EPS figures.
   If you use it in your LaTeX code, you have to compile your code using commands `latex`, `dvi2ps` and `ps2pdf` in sequence.

1. Vector figures (EPS, PDF, etc) can be too big sometimes (e.g., if you do scatter plot). In this case, you'd better use non-vector pictures (e.g., png, jgp, etc).

1. To include figures in a frame in beamer, you must use the option `[fragile]` for that frame. For example
   \\begin\{frame}[fragile]
   \\begin\{figure}
   \\includegraphics\{graph1}
   \\caption\{captiontext}
   \\label\{figurelabel}
   \\end\{figure}
   \\end\{frame}
