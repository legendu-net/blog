---
title: Tips on Zellij Web
created: '2026-10-04T20:38:36.580759-07:00'
date: '2026-10-04T20:55:12-07:00'
authors:
  - bendu
label: tips-on-zellij-web
license: CC-BY-4.0
tags:
  - Zellij
  - terminal
  - multiplexer
  - web
  - keybinding
  - shortcut
  - Google
  - Chrome
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. You can create a token using `zellij web --create-token`
   and then start a web server for zellij using `zellij web`
   .

1. By default,
   `zellij web` uses the IPv4 address `127.0.0.1`.
   Modern browsers (Chrome, Edge, ect) might resolves `localhost` as the IPv6 address `::1`.
   If that's the case,
   visiting `localhost:8082` will results in the error code `ERR_EMPTY_RESPONSE`
   .
   It is suggested that you use `127.0.0.1` instead of `localhost`
   when visiting the web page or doing local port fowarding via SSH tunneling.

1. Use `mkcert` to create certificate for hosting HTTPS
   if you need to share sessions beyong the local network.

For more discussions,
please refer to
[The Zellij Web Client - Share Sessions in the Browser](https://zellij.dev/tutorials/web-client/)
.

## Handle Conflicts of Keybindings with Google Chrome

1. Configure different keybindings in Zellij.

1. Configure different keybindings in Google Chrome for those non-builtin keybindings.

1. Enter a tab into the fullscreen Mode (with Keyboard Lock).
   Chrome includes the Keyboard Lock API,
   which allows web applications to capture reserved system keystrokes (including Ctrl + T, Ctrl + N, and Ctrl + W),
   but only when the browser tab is in fullscreen.
   This is kind of like the lock mode of Zellij,
   which allows keystokes to be passed into applications running in Zellij terminals.

## References

- [The Zellij Web Client - Share Sessions in the Browser](https://zellij.dev/tutorials/web-client/)
