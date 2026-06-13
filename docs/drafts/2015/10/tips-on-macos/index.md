---
title: Tips on macOS
created: '2015-10-23T22:14:55-07:00'
date: '2026-06-12T22:31:33-07:00'
authors:
  - bendu
label: tips-on-macos
license: CC-BY-4.0
tags:
  - macOS
  - tips
  - Apple
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Print Mac OS X operating system version information.

   ```
    :::bash
    sw_vers -productName
   ```

1. You can use Homebrew to install applications in Mac
   similar to the command `apt` in Ubuntu/Debian series of Linux distributions.
   However, you do not have to run the command brew with sudo.
   As a matter of fact,
   you should never do this.

1. You can configure macOS to hibernate on lid close
   following instructions in
   [How to configure a MacBook to hibernate when the lid is closed?](https://discussions.apple.com/thread/255421002?sortBy=rank)
   .

## Allow SSH into Mac

[Enable Remote Login to Start SSH Server in Mac OS X](http://osxdaily.com/2011/09/30/remote-login-ssh-server-mac-os-x/)

## IP Address

```
:::bash
ifconfig | grep inet
```

[How to find internal and external IP addresses on Mac OS X and macOS?](https://blog.pcrisk.com/mac/12377-how-to-find-out-your-ip-address-on-mac)

## Touchpad

1. Enable tapping (for click) by checking the checkbox `Tap to click`
   in `System preference...` > `Trackpad` > `Point & Click`.

1. Enable tapping with two fingers for right click by checking the checkboxs `Tap to click` and `Secondary click`
   in `System preference...` > `Trackpad` > `Point & Click`.

1. Tapping is automatically disable while typing on Mac.

## Useful Applications

### [CheatSheet](https://mediaatelier.com/CheatSheet/)

Just hold the ⌘-Key a bit longer to get a list of all active short cuts of the current application. It's as simple as that.

### [LICEcap](https://www.cockos.com/licecap/)

LICEcap can capture an area of your desktop and save it directly to .GIF (for viewing in web browsers, etc) or .LCF.

### [KeyCastr](https://github.com/keycastr/keycastr)

KeyCastr, an open-source keystroke visualizer.

### [Anks](https://apps.ankiweb.net/)

Anki is a program which makes remembering things easy.
Because it's a lot more efficient than traditional study methods,
you can either greatly decrease your time spent studying, or greatly increase the amount you learn.

### [Magnet](https://magnet.crowdcafe.com/)

Magnet keeps your workspace organized.

### [Alfred](https://www.alfredapp.com/)

Alfred is an award-winning app for macOS which boosts your efficiency with hotkeys, keywords, text expansion and more.
Search your Mac and the web, and be more productive with custom actions to control your Mac.

## Move and Resize Windows

https://www.spectacleapp.co/

https://github.com/eczarny/spectacle

## External Monitors

https://support.apple.com/en-us/HT202351

## References

- [Tips on Keyboard in macOS](tips-on-keyboard-in-macos)
- [How to configure a MacBook to hibernate when the lid is closed?](https://discussions.apple.com/thread/255421002?sortBy=rank)
- [Map Keys in macOS](map-keys-in-macos)
- [Install Python in macOS](install-python-in-macos)
- [Remove System Applications in macOS](misc/content/2020/03/remove-system-applications-in-mac/remove-system-applications-in-mac.markdown)
- [Change Shell in macOS](change-shell-in-mac)
- [Proxychains-Ng Issues on macOS](proxychains-ng-issues-on-mac)
- [Shortcuts in macOS](shortcuts-in-macos)
- [Add New Document to Right-Click Menu in macOS](add-new-document-to-right-click-menu-in-mac)
- [Screen Resolution in macOS](screen-resolution-in-macos)
