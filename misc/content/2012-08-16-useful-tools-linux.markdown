UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2017-04-17 11:37:24
Slug: useful-tools-linux
Title: Useful Tools in Linux
Category: OS
Tags: shell, remote, PDF, software, tools, terminal, application, Linux

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

<img src="http://dclong.github.io/media/linux/linux.png" height="200" width="240" align="right"/>

[IceWalkers](http://www.icewalkers.com/) is a great place 
to find software/tools for all kinds of purposes.

## Project Collaborating/Managment
1. slack

2. [trello](https://trello.com)
<http://lifehacker.com/how-to-use-trello-to-organize-your-entire-life-1683821040?utm_source=pocket&utm_medium=email&utm_campaign=pockethits>

## Server/Desktop Management

### Desktop Environment

1. Xfce
2. KDE
3. Gnome
4. Cinnamon
5. Unity

### Tiling Windows Manager

1. Xmonad
2. i3

### Software Installation/Remove/Recommendation
1. apt-get
2. wajig (my favourite Debian/Ubuntu package management command)
3. Software Center (A fancy GUI for managing packages on Ubuntu/Debian)
4. Software Management (Linux Mint)

### Terminal Tools
0. command-not-found - Suggest installation of packages in interactive bash sessions
1. terminator, terra, terminology, TermKit
1. screen, tmux
3. nohup, disown
5. nautilus-open-terminal
6. script (logging terminal activities)

### Administer
1. webmin, cloudmin, usermin
1. id, adduser, gpasswd (recommended for adding/removing groups)
2. uptime, top, netstat, ifconfig, top, iotop (input and output monitoring), atop, 
3. htop (a better alternative to top)

### Disk Maintenance
1. fdisk (manipulate disk partition tables)
2. df (report file system disk space usage)
3. badblocks
4. dd

### Resource Statistics
1. top
2. htop
3. dstat

### Security
1. fail2ban
2. Tor (on-line anonymity)

### Encryption

1. gpg 

### Time Synchronization

1. ntp (sync-debian)

### Task Scheduling
1. at
2. watch
1. crontab
2. inotify (monitoring file system changes and trigger events)
3. parallel

## Backup 

### Cloud Backup Tools
9. Network Attach Storage (NAS)
1. Storage Made Simple (SME)
#### Centralized 
0. Amazon S3 
    - AeroFS can backup to Amazon S3
    - s3cmd is a command line client for Linux
1. Dropbox
2. TeamDrive (secure, fast)
3. Bitcasa (security, infinite storage)
2. Google Drive
#### Decentralized (private, security)
2. BitTorrent Sync (BTSync)
##### Pros
    1. secure
    2. free
    3. no limit on files except the limit of your own disk
##### Cons
    1. beta version, not stable enough
    2. versioning is a little bit tricky
    3. no GUI version for Linux

5. AeroFS (can use Amazon S3 as the central repository)
3. Syncthing

### Non-cloud Backup Tools
1. FreeFileSync (a very good synchronization software written in C++, but bundled with malware now)
2. rsync (1-way synchronization)
3. rsnapshot (incremental backup)
4. duplicity (incremental backup with encryption and compression)
6. Back In Time
5. unison (2-way synchronization, not a good solution compared to cloud backup tools)
7. Bacula (comprehensive backup tool)
8. BackupPC

### File Transfer

0. infinit (fast, secure) 
1. BitTorrent
2. BiTorrent Sync

### File Cleaning

1. BleachBit

### File Hosting

1. Mega
#### Pros
    1. 50 GB free
    2. secure (encrypted before upload)
    3. 10 GB every 30 minutes free (essentially free consider currently network speed)
    4. maximum file size is only restricted by browser memory capability
    5. never expire
    6. cross-platform and command line tools available for Linux
    7. able to follow symbolic link
#### Cons
    1. one file at a time for free account

1. File Dropper 

#### Pros
    1. unlimited space 
    2. no bandwith limit 
#### Cons
    1. uploaded files will be removed if they are not downloaded even once 
    within 30 days consecutively (files belong to premium account are never removed)
    2. upload file can be at most 5 GB
    3. the cheapest plan is $1/month.
    really no free account, but rather just upload and keep link
    so not convenient for people without an premium account

    Good for people who would like to share large files and do not need uploaded files to be persistent.
    Or for backing up frequently changed files so that before an uploaded file is removed,
    another updated version is uploaded.
2. Baidu Yun
3. Tencent Weiyun

## Network 

### Remote Tools
1. OpenSSH, keychain (keyring for OpenSSH)
0. Teamviewer
5. NoMachine, FreeNX
2. VNC
3. SSHFS
4. Remmina
6. YuuGuu (Web Conference)
7. LogMeIn (Windows and Mac only)


### Network Maintenance
1. arp-scan
2. ping

### Downloading Tools

0. aria2 (high speed command line download utility)
1. uGet (a great Linux download manager, also a GUI for aria2)
1. Deluge (BitTorrent, magnet)
1. wget
2. curl
3. mechanize, Selenium, iMacros (auto download solutions)
3. transimission (A simple and clean BitTorrent GUI, allow you set upload rate to 0)
4. qBitTorrent (BitTorrent)
5. rTorrent (command line BitTorrent)
7. youtube-dl (youtube video downloader)
6. SubDownloader (download/upload subtitles of movies)

### Anonymous Tools
1. VPN
2. Proxy
3. Anomos
4. Tor

### VPN
1. PrivateInternetAccess
2. LogMeIn Hamachi 

## Compress and Uncompress
1. tar
1. dar (disk archive)
2. rar, unrar
3. 7z and 7za
4. dtrx
5. zip, unzip
6. xarchive
7. PeaZip

## Virtual Machine
1. VirtualBox
2. VMWare
3. Xen
4. KVM (requires hardware support, e.g., Intel VT-x or AMD-V)
5. QEMU-KVM (requires hardware support, e.g., Intel VT-x or AMD-V)

## Cloud
5. OpenStack

## Database Management System (DBMS)

### Relational DBMS
1. MySQL
    - MySQL Workbench 
2. SQLite (embedded database)

### Object/Document-oriented DBMS
1. MongoDB
4. CouchDB
3. OrientDB (written in Java)
2. UnQLite (embedded database, sounds like a good replace for SQLite)
3. MooDB (embedded database)
4. Kyoto Cabinet (embedded, for simple key-value data)
5. LevelDB (embedded, for simple key-value data)

## Daily Work Tools (Office Tools, etc.)

### Well Supported Printers
1. HP
2. Brother

### Pinyin Input Method
1. Sogou Pinyin
2. Google Pinyin
3. Sun Pinyin

### Web Browser
0. Tor (on-line anonymity)
1. Google Chrome
2. Firefox/Iceweasel
3. w3m (a powerful text-based web browser) 
4. lynx (another text-based web browser)

### On-line Tools

1. Doodle
2. Survata (for custom surveys)
3. Google Docs (Google Form can a simple solution to custom surveys)

### (Automated) Web Browsing
5. wget
5. curl (command line web browsing/scripting)
6. mechanize (web browsing/scripting written in python)
7. Selenium, iMacros
2. Sikuli Script (automate anything based on image recognition)

### Web Crawling
1. Scrapy (an open source web crawling and scraping tool written in Python)
2. 火车采集器
3. [80legs](http://www.80legs.com/)


### Finance
1. gnucash
2. DocumentBurst

### Password Management

#### GUI Password Manager

1. [KeePassXC](https://keepassxc.org/) (successor of KeePassX)
1. KeePassX
2. LastPass (for non-critical passwords)
3. kpcli (command line tool for keepassX)

#### Command-line Password Manager

3. pwman3
3. pass

### Data Manipulation
0. grep/sed/awk/cut/sort/uniq/comm
1. pdfgrep 

Search in pdf files for strings matching a regular expression. 
It only works on PDF files but even not text files.

2. taggrepper - search and match tags of audio files against regular expressions

3. crgrep - common resource grep

4. sgrep - tool to search a file for structured pattern

2. recoll 

Personal full text search package with a Qt GUI

1. catdoc/xls2csv/catppt

### Text Editor
1. Vim (general purpose text editor)
3. Geany (my favourite GUI text editor)
2. Gedit

### IDE

#### Cloud IDE

1. cloud9

Looks a good one for public projects. 
Need an account on cloud9 in order to create new workspace/project. 

2. Codenvy / Eclipse Che

Eclipse Che is a great cloud IDE!

#### C++

1. Vim with plugins YouCompleteMe and UltiSnips
0. KDevelop (C++)
0. Clion (Commerical IDE)
2. Qt Creator (for Qt development and general purpose C++ IDE)
1. Eclipse (for Java ,C++, Python, etc.)
3. Dev-C++

#### Java

1. Eclipse

2. IntelliJ IDEA (community edition available)

#### Python

1. Spyder (Python)

2. Wing IDE

3. PyCharm 

A great IDE for Python. 
A open source community edition is available for users.

4. Eric

3. Eclipse + PyDev (python)

#### R

1. RStudio (for R, Markdown ,C++, Latex, etc.) 

#### Markdown

1. Atom + Markdown Plugin

4. ReText (Markdown, reStructuredText)

5. Markable (on-line Markdown editor)

#### Julia

4. JuliaStudio (for Julia)

#### Latex

6. Bakoma (Great for Latex)

7. Texstudio (latex)

8. TexMacs (WYSIWYG, convert to Tex available)

9. ShareLatex (on-line collaborative editing)

10. WriteLatex (on-line collaborative editing)

#### SQL

1. Teradata Studio

2. Oracle SQL Developer

3. Toad

1. ViEmu/SQL for SQL Server

2. dbext for Vim

### MS Office Alternative

2. LibreOffice

3. [OnlyOffice](http://www.onlyoffice.com/)

3. Calligra Suite (KDE dependent)

2. AbiWord (Word)

1. gnumeric (Excel)

3. WPS Office

### Type Setting Tools

1. texlive

2. texstudio

### Dictionary

1. goldendict

1. dict

### Email Client

1. Thunderbird (called IceDove in Debian)

2. Evolution

3. Claws Mail

4. Sieve (mail filtering language)

### Contacts

1. cobook

2. plaxo contact

3. fullcontact


### PDF Tools

#### Reader/Viewer

1. evince

2. xpdf

2. okular

#### Manipulation

2. pdftk

### Scientific Reference Management

3. Zotero (open source, a very good one)

1. Mendeley (2G free, social network based, good for small usage, better to use together with Zotero)

2. ReadCube

2. JabRef (OK but not good)

### E-book library management

1. calibre 

### Symbolic Computing

1. Methmatica

2. sage

3. Maxima

### Notes Taking

<http://www.legendu.net/misc/blog/software-for-taking-notes/>

### Mind Mapping Tools

1. XMind
cross-platform, free

2. IHMC Cmap

2. [MindJet](http://www.mindjet.com/)
commerical, windows, mac

3. Mindomo
cross-platform (via Adobe Air)

4. WiseMapping

5. IHMC CmapTools

6. SimpleMind 
Windows, Mac

3. [Coggle](http://coggle.it/)

4. FreeMind

5. [LucidChart](https://www.lucidchart.com/)

6. [MindMeister](https://www.mindmeister.com/)
WebApplication, free

7. [code2flow](http://code2flow.com/)

#### Text-based Mind Mapping Tools
1. Markdown with relevant tools
MarkdownToMindMap
PopClip 
http://brettterpstra.com/2013/08/18/markdown-to-mind-map/

4. LaTex PGF/TikZ/Graphviz

5. [Mappio](http://mappio.com/)
looks pretty cook, better than Text2MindMap
but unfortunately also web-based

6. [Text2MindMap](https://www.text2mindmap.com/)
An online tool which looks pretty cool, but I'm looking for a native application ...

2. [Asciiflow](http://asciiflow.com/)

3. [ditaa](http://ditaa.sourceforge.net/)

4. PlantUML
plugin available for Eclipse
sounds great!

### Task Management

0. XMind

0. WorkFlowy

1. Todoist

2. Wunderlist

3. Taskwarrior

### [Auto Typing Tools](http://www.legendu.net/misc/blog/auto-typing-tools/)

## Programming Tools

### Compiler

1. GCC

2. Clang

### Debugging Tools

0. GDB

1. Valgrind

2. CUDA-Memcheck

### Version Control

1. git

## Multimedia Tools

### CD/DVD burning

#### GUI Tools  

1. k3b  

2. gnome baker

3. brasero

#### Command line Tools

0. xvidenc (shell script to encode DVDs to Xvid)

1. isoinfo

2. genisoimage (Debian) or mkisofs (other Linux)

3. dd or cat

### Video/Audio Player/Editing

1. vlc

2. MPlayer, SMPlayer

1. Kdenlive

2. Lightworks

3. ffmpeg

4. HandBrake

5. exiftool (command line multimedia meta data editor)

6. Exiv2 (image meta data library and tools written in C++)

7. youtube-dl (youtube video downloader)

### Audio

1. puddletag (simple, powerful audio tag editor)

1. beets (command line tool for managing music tagger and library)

2. clementine (a modern music player)

3. cmus (a very cool Command-line MUSic player)

3. mutagen (a python library for handling audio meta data)

4. festival (sound synthesis)

1. Ardour (audio editing)

2. Audacity (audo recording, editing)

### Screencast

1. comstudio (Windows only)

### Voice Control

1. Blather

2. Voxforge

3. Simon



### Image

1. ImageMagic

2. GwenView (KDE)

3. digiKam (KDE)

1. PIL (python image library)

4. exiftool

### Scan/OCR

0. VueScan

1. tesseract

2. gocr

### Chart

1. Dia Diagram Editor

2. LibreOffice Draw

### 3-D Modelling

1. blender

1. freeCAD

2. OpenSCAD

1. Google Sketchup

2. EQUINOX-3D

### Audio/Video Conference

<https://en.wikipedia.org/wiki/Comparison_of_web_conferencing_software>

2. Apache OpenMeeting

3. Jitsi

3. UberConference (free for up to 10 callers)

4. TeamViewer

1. Skype (support screen sharing)

2. iVisit, iChat, NetMeeting

3. Breeze

2. MeetingBurner (free for 10 attendees)


3. GoToMeeting (free for up to 4 people)

4. Google Voice (up to 4 people)

5. FreeConferenceCall (seems that it is free?)

6. Wiggio (?)

7. Speek (?)

8. https://www.freeconference.com/

9. join.me by LogMeIn

10. SightSpeed

11. Free conference calling

12. Dimdim

1. Tokbox

2. MyMeeting123

3. Paltalk

4. MegaMeeting

5. Fuze Meeting

6. Free Audio Conferencing

7. Easy Conference

8. Easy Conference

9. Gizmo Call

10. Totally Free Conference

11. RingCenteral

1. Onstream Meetings
http://en.wikipedia.org/wiki/Comparison_of_web_conferencing_software
http://www.d.umn.edu/~hrallis/professional/presentations/cotfsp06/indiv_tools/videoaudio.htm

## Social Tools

### Teleconference

0. Blink

1. Skype

2. Wire

2. Jitsi

3. ekiga

4. QQ (webqq, wineqq)

## Web Hosting

### Server Side Scripting Language

1. PHP

2. JSP

### Client Side Scripting Language

1. JavaScript

### Integrated Package for Web Hosting

1. XAMPP (originaly called LAMPP)

### Math Formulas in Web Pages

1. MathJax (a successor to jsMath)

## Performance Tools

## Boot Performance

1. bootchart

2. readahead-fedora

## Runtime Performance

1. preload

2. localepurge

## Other Suggestions

1. remove old kernels

2. package clean-up

## Web Tools

1. 1. JustInMind Prototyper

2. Ruby On Rails (RoR)

4. Django

3. Node.JS

4. ActiveJDBC

5. web2py

3. SAS Stored Process (Web Application) and SAS Visual Analytics

## Software Host 

1. GitHub
    - no private repository for free account

2. Bitbucket
    - unlimited private repositories for free account

3. SourceForge

## Repository Hosting Tools

1. gitolite

2. gitlab


## File Converting Tools

1. pandoc (mark-up language)

2. markdown (markdown to HTML)

2. tex4ht (convert Latex code to HTML)

2. wkhtmltopdf (html to PDF, support URL, best)

2. knitr (an R package)

3. ImageMagick (convert between types of images)

4. [HTML2Image](http://www.guangmingsoft.net/htmlsnapshot/html2image.htm)

5. [CutyCapt](http://cutycapt.sourceforge.net/)

4. pdflatex 

5. dos2unix, unix2dos

## Windows Emulation on Linux Host

Virtual machine is the recommend way to emulate Windows working environment.

1. VirtualBox, VMWare, MobaLiveCD

2. Wine, CrossOver

## Linux Emulation on Windows Host

0. VirtualBox, VMWare

1. Cygwin (Vim, git and other tools might limited functionalities)

2. MobaXterm (tools have limited functionalities)

2. MobaLiveCD (a little cool application to run Linux live CD in Windows)

## Games

- Team fortress 2

- Dungeon defenders

- Counter strike

- Bit trip runner 2

- The cave

- Heroes of newerth

- Trine 2

- Serious sam 3

- Rochard

- Botanicula

- Frozen Synapse

- Dear Esther


## Websites

1. MileWise

2. BTGuard

3. http://dedalvs.tumblr.com/post/48998678919/99-life-hacks-to-make-your-life-easier

## Translation
https://www.apertium.org/index.eng.html?dir=eng-cat#translation

## Misc

1. KeyMon: displays the mouse button or key being clicked/pressed, 
useful when you video tape your screen
