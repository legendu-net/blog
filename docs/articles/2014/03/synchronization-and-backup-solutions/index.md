---
title: Synchronization and Backup Solutions
created: '2014-03-04T22:11:05-08:00'
date: '2026-08-13T21:19:31-07:00'
authors:
  - bendu
label: synchronization-and-backup-solutions
license: CC-BY-4.0
tags:
  - software
  - synchronization
  - backup
  - Baidu Yun
  - Dropbox
  - TeamDrive
  - Syncthing
  - alternative
---

## Tips and Traps

1. Almost all sychronization tools have problems with symbolic links.
   Most of them just ignore symbolic links.
   This makes sense as following symbolic links can causes serious disk problems.
   If not followed then symbolic links are likely broken on other device.
   The simple suggestion is do not place symbolic links in your synchronization folders.

1. Backup (relatively) small files to Dropbox (or a similar tool),
   and Backup large non-privacy files on Baidu Yun.
   If a large file is sensitive,
   encrypt it first before uploding it to Baidu Yun.

```{list-table}
---
header-rows: 1
---
- - Service
  - Linux Support Level
  - Official Linux App Details
- - pCloud
  - Native (Full Support)
  - Provides a fully featured AppImage client with file syncing, GUI management, virtual drive mounting, and selective sync.
- - Nextcloud
  - Native (Full Support)
  - Offers full desktop sync client support for Ubuntu, Debian, Fedora, Arch, openSUSE, and AppImage formats.
- - Proton Drive
  - Limited (CLI Only)
  - Official support is limited to a Command-Line Interface (CLI) app; no official native GUI sync app for desktop Linux.
- - Google Drive
  - Web / 3rd-Party Only
  - No official Google sync client for Linux. Requires web browser usage or third-party sync apps (e.g., Insync, Rclone).
- - Microsoft OneDrive
  - Web / 3rd-Party Only
  - No official desktop client. Requires web app or open-source tools (e.g., onedrive CLI or Rclone).
- - Sync.com
  - Web Only
  - Offers no native desktop sync app for Linux; web portal access only.
```

```{list-table}
---
header-rows: 1
---
- - Name
  - Opensource/free
  - OS
  - GUI/CLI
  - Sync/Backup
  - Directly Accessible from Mainland of China
  - Comments
- - [Dropbox](https://www.dropbox.com/)
  - free for 3 devices and 2G space
  - Windows, macOS, Linux
  - GUI
  - Sync
  - No
  - 1. Best solution for small data backup
    2. every thing is in the same folder, no way to sync a folder with higher priority over others
       while you can do this with TeamDrive or BTSync
- - [Baidu Net Disk](https://pan.baidu.com/disk/home)
  - free for 2T space and limited download speed
  - Windows, macOS, Linux
  - GUI
  - Sync
  - Yes
  - Best solution for large data backup
- - [Synqion (TeamDrive)](https://synqion.com/)
  - free for 2G space
  - Windows, macOS, Linux
  - GUI
  - Sync
  - Yes
  - 1. Best solution for small data backup
    2. extremely secure, good for private, sensitive docs
    3. separated spaces which is much better than dropbox
- - [Syncthing](https://syncthing.net/)
  - free
  - Windows, macOS, Linux
  - Both
  - Sync
  - Yes
  - 1. extremely secure, good for private, sensitive docs
    2. good performance on large files but poor performance on small files
    3. Best solution for private personal backup
- - [Google Drive](https://www.google.com/drive/)
  - free for 15G space
  - Windows, macOS
  - GUI
  - Sync
  - No
  - 1. good for backing up Google products
- - [OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage)
  - free for 15G space
  - Windows, macOS
  - GUI
  - Sync
  - No
  - 1. good for backing up MS products
- - NAS / NFS
  - free
  - Windows, macOS, Linux
  - Both
  - network file system
  - Yes
  - 1. easy to use
    2. provided to employees by many companies
    3. relatively low performance
- - [Mutagen](https://mutagen.io/)
  - Opensource
  - Windows, macOS, Linux
  - CLI
  - sync
  - Yes
  - 1. fast file synchronization;
    2. network forwarding
- - [Unison](https://github.com/bcpierce00/unison)
  - Opensource
  - Windows, macOS, Linux
  - CLI
  - 2-way sync
  - Yes
  - 2-way sync, fault tolerance
- - [osync](https://github.com/deajan/osync)
  - Opensource
  - Windows, macOS, Linux
  - CLI
  - 2-way sync
  - Yes
  - 2-way sync, rsync-based, fault tolerance
- - [Rsnapshot](https://github.com/rsnapshot/rsnapshot)
  - free
  - Windows, macOS, Linux
  - CLI
  - Backup
  - Yes
  - 1. easy to use
    2. quick access
    3. copy on change which takes more disk space than incremental backup tools but it is much simpler to use and is very robust
- - [duplicity](http://www.nongnu.org/duplicity/)
  - free
  - Windows, macOS, Linux
  - CLI
  - Backup
  - Yes
  - 1. incremental backup
    2. support encryption
- - [backupPC](https://github.com/backuppc/backuppc)
  - free
  - Windows, macOS, Linux
  - ?
  - Backup
  - Yes
  - high performance, enterprise-grade system
- - [Bacula](https://www.bacula.org/)
  - Opensource
  - Windows, macOS, Linux
  - ?
  - Backup
  - Yes
  - enterprise-level computer backup system for heterogeneous networks
```

## References

- [How to synchronize files between two servers bidirectionally](http://xmodulo.com/synchronize-files-between-two-servers.html)

- [csync](https://www.csync.org/)
