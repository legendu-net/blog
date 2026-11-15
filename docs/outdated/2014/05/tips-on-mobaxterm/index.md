---
title: Tips on MobaXterm
created: '2014-05-22T15:40:46-07:00'
date: '2026-11-15T09:28:26-08:00'
authors:
  - bendu
label: tips-on-mobaxterm
license: CC-BY-4.0
tags:
  - software
  - MobaXterm
  - tips
  - Linux
  - virtualization
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

\*\*
Things under legendu.net/outdated are outdated technologies
that the author does not plan to update any more.
Please look for better alternatives.
\*\*

1. MobaXterm uses a temporary folder as the home directory by default
   and all data in the temporary home directory will be lost next time you run MobaXterm,
   so it is a good practice to set up a permanent folder
   as your home directory before you use MobaXterm.
   It is suggested that you use the `My Documents` as the home directory for MobaXterm.

1. Commands in MobaXterm (based on BusyBox) have limited functionalities
   compared to the same commands in Linux/Unix.
   You probably need to modified you bash code in Linux/Unix
   in order to run in MobaXterm.

1. Vim in MobaXterm is compiled without python support,
   so vim plugins (e.g., UltiSnips) requiring python might not work
   even if you can install python as a plugin in MobaXterm.

1. It is strange that rename is available on MobaXterm but you get no help doc for it.
   There is no way for you to know it unless you accidentally tried rename on MobaXterm.

1. You can copy Cygwin exe files to MobaXterm to extend its functionalities.
   You can also use other existing programs in Windows, e.g., R.
   However,
   interactive programs (e.g., R) might not well as an error might cause the program to exit.

1. MobaXterm automatically adjust case which is convenient on Windows.

## Tools Not Available

1. at, cron

## Available

1. shutdown, rename (limit functionalities, different from rename in Linux), ssh

1. MobaXterm rename is indeed available, though no documentation available
