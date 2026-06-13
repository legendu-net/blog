---
title: Useful Tools in Linux
created: '2012-08-17T11:42:15-07:00'
date: '2026-06-12T22:31:50-07:00'
authors:
  - bendu
label: useful-tools-in-linux
license: CC-BY-4.0
tags:
  - shell
  - remote
  - PDF
  - software
  - tools
  - terminal
  - application
  - Linux
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

<img src="/media/linux/linux.png" height="200" width="240" align="right"/>

[IceWalkers](http://www.icewalkers.com/) is a great place
to find software/tools for all kinds of purposes.

## [Project](tips-on-project-management)

## Server/Desktop Management

### [Linux Desktop Environment](desktop-environments-for-linux)

### [Linux Package Management](package-management-in-linux)

### [Administer](linux-administrator-tools)

### [Disk Maintenance](command-line-tools-for-linux-file-system)

### [Admin Tools](linux-administrator-tools)

### Security

1. fail2ban
1. Tor (on-line anonymity)

### Encryption

1. gpg

### Time Synchronization

1. ntp (sync-debian)

### [Task Scheduling](workflow-managing-tools)

## Backup

### Cloud Backup Tools

1. Network Attach Storage (NAS)

1. Storage Made Simple (SME)

#### Centralized

0. Amazon S3

   - AeroFS can backup to Amazon S3
   - s3cmd is a command line client for Linux

1. Dropbox

1. TeamDrive (secure, fast)

1. Bitcasa (security, infinite storage)

1. Google Drive

#### Decentralized (private, security)

2. BitTorrent Sync (BTSync)

##### Pros

1. secure

1. free

1. no limit on files except the limit of your own disk

##### Cons

1. beta version, not stable enough

1. versioning is a little bit tricky

1. no GUI version for Linux

1. AeroFS (can use Amazon S3 as the central repository)

1. Syncthing

### Non-cloud Backup Tools

1. rsync (1-way synchronization)

1. rsnapshot (incremental backup)

1. duplicity (incremental backup with encryption and compression)

1. borg

1. Back In Time

1. unison (2-way synchronization, not a good solution compared to cloud backup tools)

1. Bacula (comprehensive backup tool)

1. BackupPC

1. FreeFileSync (a very good synchronization software written in C++, but bundled with malware now)

### File Transfer

0. infinit (fast, secure)

1. BitTorrent

1. BiTorrent Sync

### File Cleaning

1. BleachBit

### File Hosting

1. Mega

#### Pros

1. 50 GB free

1. secure (encrypted before upload)

1. 10 GB every 30 minutes free (essentially free consider currently network speed)

1. maximum file size is only restricted by browser memory capability

1. never expire

1. cross-platform and command line tools available for Linux

1. able to follow symbolic link

#### Cons

```
1. one file at a time for free account
```

1. File Dropper

#### Pros

1. unlimited space

1. no bandwith limit

#### Cons

1. uploaded files will be removed if they are not downloaded even once
   within 30 days consecutively (files belong to premium account are never removed)

1. upload file can be at most 5 GB

1. the cheapest plan is \$1/month.
   really no free account, but rather just upload and keep link
   so not convenient for people without an premium account

   Good for people who would like to share large files and do not need uploaded files to be persistent.
   Or for backing up frequently changed files so that before an uploaded file is removed,
   another updated version is uploaded.

1. Baidu Yun

1. Tencent Weiyun

## [Network](linux-network-tools)

## [Compress and Uncompress](compress-and-decompressing-archives-in-linux)

## Virtual Machine

1. VirtualBox
1. VMWare
1. Xen
1. KVM (requires hardware support, e.g., Intel VT-x or AMD-V)
1. QEMU-KVM (requires hardware support, e.g., Intel VT-x or AMD-V)

## Database Management System (DBMS)

### Relational DBMS

1. MySQL

1. SQLite (embedded database)

### Object/Document-oriented DBMS

1. MongoDB
1. CouchDB
1. OrientDB (written in Java)
1. UnQLite (embedded database, sounds like a good replace for SQLite)
1. MooDB (embedded database)
1. Kyoto Cabinet (embedded, for simple key-value data)
1. LevelDB (embedded, for simple key-value data)

## Daily Work Tools (Office Tools, etc.)

### Pinyin Input Method

1. Sogou Pinyin
1. Google Pinyin
1. Sun Pinyin

### Web Browser

0. Tor (on-line anonymity)
1. Google Chrome
1. Firefox/Iceweasel
1. w3m (a powerful text-based web browser)
1. lynx (another text-based web browser)

### On-line Tools

1. Doodle
1. Survata (for custom surveys)
1. Google Docs (Google Form can a simple solution to custom surveys)

### Finance

1. gnucash
1. DocumentBurst

### [Password Management](password-management)

### Data Manipulation

0. grep/sed/awk/cut/sort/uniq/comm
1. pdfgrep

Search in pdf files for strings matching a regular expression.
It only works on PDF files but even not text files.

2. taggrepper - search and match tags of audio files against regular expressions

1. crgrep - common resource grep

1. sgrep - tool to search a file for structured pattern

1. recoll

Personal full text search package with a Qt GUI

1. catdoc/xls2csv/catppt

### Text Editor

1. Vim (general purpose text editor)
1. Visual Studio Code

## MS Office Alternative

2. LibreOffice

1. [OnlyOffice](http://www.onlyoffice.com/)

1. Calligra Suite (KDE dependent)

1. AbiWord (Word)

1. gnumeric (Excel)

1. WPS Office

### Publishing Tools

1. LaTex

#### [Scribus](https://www.scribus.net/magazine-production/)

Opensource Desktop Publishing

### Dictionary

1. goldendict

1. dict

### Email Client

1. Thunderbird (called IceDove in Debian)

1. Evolution

1. Claws Mail

1. Sieve (mail filtering language)

### PDF Tools

#### Reader/Viewer

1. evince

1. xpdf

1. okular

#### Manipulation

2. pdftk

### Scientific Reference Management

3. Zotero (open source, a very good one)

1. Mendeley (2G free, social network based, good for small usage, better to use together with Zotero)

1. ReadCube

1. JabRef (OK but not good)

### E-book library management

1. calibre

### Notes Taking

[Notes Taking Solutions](notes-taking-solutions)

### Task Management

0. XMind

1. WorkFlowy

1. Todoist

1. Wunderlist

1. Taskwarrior

### [Auto Typing Tools](auto-typing-tools)

## Programming Tools

### Compiler

1. GCC

1. Clang

### Debugging Tools

0. GDB

1. Valgrind

1. CUDA-Memcheck

### Version Control

1. git

## Multimedia Tools

### [OBS Studio](https://github.com/obsproject/obs-studio)

[OBS Studio](https://github.com/obsproject/obs-studio)
Free and open source software for live streaming and screen recording

### Music Player

1. [Clementine](https://www.clementine-player.org/)

### Screenshot

[Take Screenshot Using Shutter on Linux](take-screenshot-on-linux)

### CD/DVD burning

#### GUI Tools

1. k3b

1. gnome baker

1. brasero

#### Command line Tools

0. xvidenc (shell script to encode DVDs to Xvid)

1. isoinfo

1. genisoimage (Debian) or mkisofs (other Linux)

1. dd or cat

### Video/Audio Player

1. vlc

1. [IINA](https://github.com/iina/iina)

1. HandBrake

1. exiftool (command line multimedia meta data editor)

1. Exiv2 (image meta data library and tools written in C++)

### [Software for Editing Videos](software-for-editing-videos)

### [Audio Tools](audio-tools)

Please refer to
[Audio Tools](audio-tools)
for more details.

### Screencast

1. comstudio (Windows only)

### Voice Control

1. Blather

1. Voxforge

1. Simon

### Image

1. ImageMagic

1. GwenView (KDE)

1. digiKam (KDE)

1. PIL (python image library)

1. exiftool

### Scan/OCR

0. VueScan

1. tesseract

1. gocr

### [Charts](software-for-charts)

### 3-D Modelling

1. blender

1. freeCAD

1. OpenSCAD

1. Google Sketchup

1. EQUINOX-3D

## Social Tools

### Teleconference

0. Blink

1. Skype

1. Wire

1. Jitsi

1. ekiga

1. QQ (webqq, wineqq)

## Web Hosting

### Server Side Scripting Language

1. PHP

1. JSP

### Client Side Scripting Language

1. JavaScript

### Integrated Package for Web Hosting

1. XAMPP (originaly called LAMPP)

### Math Formulas in Web Pages

1. MathJax (a successor to jsMath)

## Performance Tools

## Boot Performance

1. bootchart

1. readahead-fedora

## Runtime Performance

1. preload

1. localepurge

## Other Suggestions

1. remove old kernels

1. package clean-up

## Web Tools

1. 1. JustInMind Prototyper

1. Django

1. Node.JS

1. ActiveJDBC

1. web2py

## Software Host

1. GitHub

   - no private repository for free account

1. Bitbucket

   - unlimited private repositories for free account

1. SourceForge

## Repository Hosting Tools

1. gitolite

1. gitlab

## Websites

1. MileWise

1. BTGuard

1. http://dedalvs.tumblr.com/post/48998678919/99-life-hacks-to-make-your-life-easier

## Translation

https://www.apertium.org/index.eng.html?dir=eng-cat#translation

## Misc

1. KeyMon: displays the mouse button or key being clicked/pressed,
   useful when you video tape your screen
