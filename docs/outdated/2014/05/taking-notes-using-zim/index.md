---
title: Taking Notes Using Zim
created: '2014-05-22T13:11:56-07:00'
date: '2026-11-15T09:28:22-08:00'
authors:
  - bendu
label: taking-notes-using-zim
license: CC-BY-4.0
tags:
  - software
  - tips
  - notes
  - Zim
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

\*\*
Things under legendu.net/outdated are outdated technologies
that the author does not plan to update any more.
Please look for better alternatives.
\*\*

0. best to let Zim commit (Git) automatically to avoid data loss

1. A quickly to delete a note is to delete everything (including the title) of that note.
   Actually this is the suggested way to delete a note from Zim.
   The advantage is that if there a sub note, it won't be deleted,
   but if the sub note is delete, then the note will also be deleted automatically.
   also works for linked pages ...
   a linked page won't disappear even if you remove everything in the page,
   but if the link is gone, the page will automatically be removed
   The traditional right-click then delete way ...,
   you have to worry about whether a note has sub notes or not.

1. Link file vs attach file:
   a link points to a local file/web address
   while "Attach File" make a local copy of the file in the notes directory and then link to it.
   The approach of "Attach file" is more robust while the approach of "link" is better for sharing
   if you are sure that the file/web site won't be moved.

1. uncheck "Automatically turn "CamelCase" into links ...

1. Since Zim notes are organized using files and directories,
   merging 2 independent zim notes can be as simple as copy files and directories from one to the other.
   Of course you need to take care of conflicting names.
   you can rename notes first to avoid confliction.

1. better to use full link address to avoid confusing zim
   about whether it is an external link or an internal link

## Useful Plugins

1. Sort lines
   With this plugin enabled, you can sort selected lines alphabetically.

The first time you open Zim,
you will be asked for a name and directory of the notes.
You can select a previous Zim notes directory to import it.
It is possible for you to track multiple Zim notes at the same time.
