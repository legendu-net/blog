---
title: Add an Entry into the Right-click Menu in Windows
created: '2014-12-03T19:30:50-08:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: add-an-entry-into-the-right-click-menu-in-windows
license: CC-BY-4.0
tags:
  - Windows
  - right-click menu
  - registry
  - regedit
---

To add an entry into the right-click menu in Windows,
edit the registry following the steps below.

0. Open the registry.
   You can search for `regedit` in Windows Start menu and run it.

1. Navigate to the key
   `HKEY_CLASSES_ROOT\Directory\Background\shell`
   in the registry.

1. Create another key with any name (e.g., rstudio) under
   `HKEY_CLASSES_ROOT\Directory\Background\shell`.

1. Set a value (e.g., Rstudio) for the newly created key (rstudio)
   in the right-side pane of the registry.
   This value (Rstudio) shows up in the right-click menu whenever you right click.

1. Create another key named `command` under the newly created key (rstudio).

1. Set the value of the newly created key `command`
   to be the full path of the application
   (e.g., `C:\Program Files\RStudio\bin\rstudio.exe`)
   that you want to launch.
