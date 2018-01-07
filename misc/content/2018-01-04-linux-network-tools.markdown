UUID: 20d79b02-800d-4c0f-8885-d01be3bb28f2
Status: published
Date: 2018-01-04 02:49:23
Author: Ben Chuanlong Du
Slug: linux-network-tools
Title: Linux Network Tools
Category: Programming
Tags: programming

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Network Admin  
1. arp-scan
2. ping
3. netstat
4. ip addr

        ip addr show dev eth0
        ip addr show dev eth0 | grep -i --color=auto inet | cut -d / -f 1 | cut -d ' ' -f 6

5. nslookup

        nslookup ip_address


## Remote Tools

1. OpenSSH, keychain (keyring for OpenSSH)
0. Teamviewer
5. NoMachine, FreeNX
2. VNC
3. SSHFS
4. Remmina
6. YuuGuu (Web Conference)
7. LogMeIn (Windows and Mac only)

## VPN
0. ExpressVPN
1. PrivateInternetAccess
2. LogMeIn Hamachi 

## Downloading Tools

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

## Anonymous Tools
1. VPN
2. Proxy
3. Anomos
4. Tor

