---
title: Tips on Firefox
created: '2013-10-11T01:05:59-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: tips-on-firefox
license: CC-BY-4.0
tags:
  - software
  - tips
  - Firefox
  - web browser
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. In Debian, Iceweasel sometimes fail to wrap Chienes page well.
   To solve the problem, you can just remove the .mozilla directory under you home directory.
   The cons is that this might remove some add-ons you installed,
   so you have to reinstall them.
   This trick works for any application in Linux.

1. A Simple Way to Export all tab URLs (Without Using Extensions)

   a. Go to Tools > Options.

   b. Look for the button `Use Current Pages` in the Startup section in the `General` tab.

   c. Click the button `Use Current Pages`,
   which will copy URLs of pages (delimited by pipes) to the textbox on the home page.

   d. Copy the text to get all the URLs.

1. The keyboard shortcut to simulate clicking on the `Use Current Pages` button
   is `Alt + T + O + C` (tested in Firefox 14).

1. Firefox is very slow sometimes. Removing .Mozilla and restart helps.
   Of course, you lose old profile.

## Shortcut

1. alt + f: pop up the File menu
1. alt + e: pop up the Edit menu
1. alt + v: pop up the View menu
1. alt + s: pop up the History menu
1. alt + b: pop up the Bookmark menu
1. Alt + T: Pop up the Tool menu.
1. alt + h: pop up the Help menu

The Firefox Reader Mode keyboard shortcut is currently bound to Cmd+Alt+R on macOS, and Alt+R on Windows and Linux.

## References

- [Install Firefox in Debian](install-firefox-in-debian)

- [Useful Firefox Add-ons](install-firefox-in-debian)

- [Resolve the DNS Contamination Issue in Firefox](resolve-the-dns-contamination-issue-in-firefox)

- [Use External Downloader for Firefox](use-external-downloader-for-firefox)

- [Vim Keybindings in Firefox Using Tridactyl](vim-keybindings-in-firefox-using-tridactyl)
