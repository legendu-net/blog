---
title: Start RStudio Server after Upgrading
created: '2016-12-10T02:09:11-08:00'
date: '2026-08-11T22:39:32-07:00'
authors:
  - bendu
label: start-rstudio-server-after-upgrading
license: CC-BY-4.0
tags:
  - software
  - IDE
  - RStudio
---

It is quite often that the RStudio server cannot be start after upgrading.
This is due to running R session in the background.
A simple solution is to just restart the host machine.
However, it is very risky to start servers (especially remote shared ones).
An alternative way is to find the R session in the background,
kill it and then start the RStudio server.
The following instruction assumes that
the port 8787 (default) is used by RStudio server.

1. Find processes that listen to the port 8787.

   ```
    sudo fuser 8787/tcp
   ```

1. Kill all processes that listen to the port 8787.

   ```
    sudo fuser -k 8787/tcp
   ```

   Or you can also use the command `kill` to terminate processes.

1. Start RStudio server.

   ```
    sudo rstudio-server start
   ```
