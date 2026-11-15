---
title: FTP on Linux
created: '2021-10-10T14:00:53-07:00'
date: '2026-11-15T09:21:48-08:00'
authors:
  - bendu
label: ftp-on-linux
license: CC-BY-4.0
tags:
  - computer science
  - Linux
  - FTP
  - SFTP
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation in Ubuntu

```bash
sudo apt install ftp
```

## FTP

1. Most FTP severs accepts only SFTP connections,
   which means that you have to log into those servers using `sftp` instead of `ftp`.
   The tricky part is that connecting to those servers using `ftp` might hang without meaningful error messages.
   So if you encounter issues log into a FTP server using `ftp`,
   try `sftp` instead.

   ```bash
   sftp user@server [port]
   ```

1. ftp transfer non-text use binary mode
