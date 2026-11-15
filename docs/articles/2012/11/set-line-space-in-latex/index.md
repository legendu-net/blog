---
title: Set Line Space in LaTeX
created: '2012-11-13T00:05:22-08:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: set-line-space-in-latex
license: CC-BY-4.0
tags:
  - LaTeX
  - programming
  - line
  - spacing
  - space
---

1. The `parskip` command makes a skip between paragraphs.
   The length of skip can be set using the command `\setlength`, e.g.,

   ```
    \setlength{\parskip}{15pt plus 1pt minus 1pt}
   ```

1. The command `\itemsep` sets the space between items in lists, e.g.,

   ```
    \begin{itemize}
    \itemsep = 0.8cm
    \item 
    \end{itemize}
   ```

1. The command `\doublespace` makes lines after this command double spaced.
   This is convenient to produce PDF document for review.
