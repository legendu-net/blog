---
title: Make Your Linux Server Securer
created: '2013-04-16T11:02:36-07:00'
date: '2026-11-15T09:14:47-08:00'
authors:
  - bendu
label: make-your-linux-server-securer
license: CC-BY-4.0
tags:
  - security
  - Linux
  - server
---

3. Define host access rules in `/etc/hosts.allow` and `/etc/hosts.deny`.
   Usually I only allow login to my private server from my home and work ip.
   If I have to login into my private server from some other network,
   I login to a computer at my workplace,
   login into my private server from the computer at my workplace,
   editing the access rules on my private server,
   and then login into my private server from the new network directly.

1. Disable root SSH login (edit the file `/etc/ssh/sshd_config`).
   With root SSH login disabled,
   a hacker has to guess both your login name and password,
   which is much harder than guessing the password alone.

1. Use a non-default port for the SSH server (edit the file `/etc/ssh/sshd_config`).
   With a non-default port set up,
   a hacker has to also guess the port number,
   which makes the brute-forth break-in even harder.
   You can use the command `sudo nmap -sS -O 127.0.0.1` to scan open ports.

1. Use the package `fail2ban` to automatically ban ips which attempts to break into your server by brute-forth.
