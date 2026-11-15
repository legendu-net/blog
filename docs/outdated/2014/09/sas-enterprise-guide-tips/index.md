---
title: SAS Enterprise Guide Tips
created: '2014-09-14T18:44:56-07:00'
date: '2026-11-15T09:29:16-08:00'
authors:
  - bendu
label: sas-enterprise-guide-tips
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - SAS Enterprise Guide
  - GUI
  - SEG
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

\*\*
Things under legendu.net/outdated are outdated technologies
that the author does not plan to update any more.
Please look for better alternatives.
\*\*

0. You can open multiple SAS Enterprise Guide instances.
   This allows you to work on another project if your SAS code takes a long time to run.

1. You can set the workplace layout to be "side by side" or "stacked".
   This makes things convenient as you can see both your code and the execution results at the same time.

1. "Selected Server: ..."

1. "Profile" at right bottom corner

1. CTRL +SHIFT + s WITH/WITHOUT SHIFT
   save/save as

1. select then tab or shift + tab >> \<<

1. SAS Enterprise Guide does not auto load changed code
   if it is updated in another place/editor.
   You have to close the file and reopen it to get the updated version.

1. show line number
   Menu -> Program -> Editor Options... -> General Tab -> check "Show line numbers"

## Shotcurts

Convert case
Convert selected text to upper case: Ctrl + Shift + U
Convert selected text to lower case: Ctrl + Shift + L

Quick commenting
Wrap selection (or current line) in a comment: Ctrl + /
Unwrap selection (or current line) from a comment: Ctrl + Shift + /

Hyperjump to a line
Go to line: Ctrl + G (prompts for a line number)
Be sure to turn on Show line numbers in Program->Editor Options, or you'll be navigating blind!

Jump to the "end of scope"
Move caret to matching parenthesis/brace: Ctrl + [, Ctrl + ]
Move caret to matching DO/END keyword: Alt + [, Alt + ]

There are dozens of other shortcut keys and commands available in the program editor. In SAS Enterprise Guide, you can view them all by selecting Program->Enhanced Editor Keys. From this window you can customize the keypress behaviors to your liking, and you can also combine commands and assign them to new keys. If you're a "keyboard person", then you'll want to visit this window and explore. Be sure to click "Include commands without key assignments" to see the full list of available commands.
