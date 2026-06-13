---
title: Map Keys in macOS
created: '2016-06-26T07:30:03-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: map-keys-in-macos
license: CC-BY-4.0
tags:
  - macOS
  - Apple
  - mapping
  - keys
  - Seil
---

Update: As of MacOS Sierra 10.12.1,
the remapping of `Caps Lock` to `Escape` can be done natively in the Keyboard System Preferences pane.
Follow the steps below to remap Caps Lock to Escape (without relying on 3rd party software).

1. Open System Preferences and click on `Keyboard`
1. Click on `Modifier Keys...`
1. For `Caps Lock Key`, choose `Escape`
1. Click `OK`

## The Old Way of Using Seil

[Seil](https://pqrs.org/osx/karabiner/seil.html.en)
(previouly known as PCKeyboardHack) is great tool for mapping keys on Mac.
Let me illustrate how to use `Seil`.
As a heavy Vim user,
I find it is necessary to swap the `Caps Lock` key with the `Escape` key.

1. Change the behavior of Map Caps Lock Key to No Action on Mac.

   1. Open `System Preferences`
   1. Open `Keyboard`
   1. Open `Modifier Keys...`
   1. Change `Caps Lock Key` to `No Action`

1. Map the behavior of Caps Lock key to the Escape key using `Seil`.

   1. Click on `Change the caps lock key` in `Seil`
   1. Check `Change the caps lock key`
   1. Fill 53 (keycode of Escape) in the keycode text box

1. Map the behavior of the Escape key to the Caps key using `Seil`.

   1. Click on `Other keys` in `Seil`
   1. Check `Change Escape`
   1. fill 57 (keycode of the Caps Lock key) in the keycode text box.

## References

- [Map Keys in Linux](map-keys-in-linux)

- [Map Keys in Windows](map-keys-in-windows)
