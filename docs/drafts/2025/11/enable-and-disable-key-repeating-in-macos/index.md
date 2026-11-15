---
title: Enable and Disable Key Repeating in macOS
created: '2025-11-27T01:05:39-08:00'
date: '2026-11-15T09:28:21-08:00'
authors:
  - bendu
label: enable-and-disable-key-repeating-in-macos
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - macOS
  - Apple
  - keyboard
  - key
  - repeating
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Run the following command in terminal and then **restart your Mac** to enable key repeating by pressing and holding.

   ```bash
   defaults write -g ApplePressAndHoldEnabled -bool false
   ```

1. Run the following command in terminal and then **restart your Mac** to disable key repeating by pressing and holding.

   ```bash
   defaults write -g ApplePressAndHoldEnabled -bool true
   ```

For more details please refer to
[How to Enable Key Repeating in macOS](https://www.howtogeek.com/267463/how-to-enable-key-repeating-in-macos/)
.
