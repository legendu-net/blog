---
title: An IO Bug in R
created: '2012-08-15T21:22:47-07:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: an-io-bug-in-r
license: CC-BY-4.0
tags:
  - warning
  - IO
  - programming
  - R
  - bug
---

<img src="/media/computer/bug.jpg" height="200" width="240" align="right"/>

I encountered an input/output bug in R in Linux system.
The symptom is that input and output are not displayed in the terminal
and the warning message
"An unusual circumstance has arisen in the nesting of readline input.
Please report using bug.report()" is shown.
I found that though input and output are not displayed, you can still
interact with the underlying R session.
A safe way is to save the R workspace, quit the R session, open a new
R session and load in the saved workspace. To save the R workspace,
just type in `save.image('ws_name')` in the console, where `ws_name`
is the name of the workspace. Notice that you will not see anything
happen on the console, so you have to make sure that you do not make
any mistake typing in the command. To quit the R session after saving
the workspace, you can type in 'q('no')' in the console.
Similarly, you won't see anything in the console, so make sure you do not
make any mistake. Now can open a new R session, and then load in the saved
workspace.
