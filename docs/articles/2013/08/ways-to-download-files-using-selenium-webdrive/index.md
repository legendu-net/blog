---
title: Ways to Download Files Using Selenium Webdrive
created: '2013-08-16T14:25:17-07:00'
date: '2026-11-15T09:18:53-08:00'
authors:
  - bendu
label: ways-to-download-files-using-selenium-webdrive
license: CC-BY-4.0
tags:
  - web
  - WebDrive
  - automation
  - Selenium
  - software
---

Selenium WebDrive cannot have no control of system Dialog,
so you have to avoid the Dialog when downloading files using WebDrive.

The first way is to enable automatic download in the browser
that you use with Seleniu WebDrive.
So when click a file link,
the file is automatically downloaded to the directory that you set.
The second (and better way) is to export the cookie of the browser,
extract the download link and then use the command `wget` or `curl` to download it.
Surely you have to use the cookie with `wget` or `curl` if authentication is required on the web.
