Status: published
Date: 2016-06-26 07:30:03
Author: Ben Chuanlong Du
Slug: map-keys-in-macos
Title: Map Keys in macOS
Category: OS
Tags: Mac, Apple, macOS, mapping, keys, Seil
Modified: 2021-08-15 13:03:09

Update: As of MacOS Sierra 10.12.1,
the remapping of `Caps Lock` to `Escape` can be done natively in the Keyboard System Preferences pane.
Follow the steps below to remap Caps Lock to Escape (without relying on 3rd party software).

1. Open System Preferences and click on `Keyboard`
2. Click on `Modifier Keys...`
3. For `Caps Lock Key`, choose `Escape`
4. Click `OK`


## The Old Way of Using Seil

[Seil](https://pqrs.org/osx/karabiner/seil.html.en)
(previouly known as PCKeyboardHack) is great tool for mapping keys on Mac.
Let me illustrate how to use `Seil`.
As a heavy Vim user,
I find it is necessary to swap the `Caps Lock` key with the `Escape` key.

1. Change the behavior of Map Caps Lock Key to No Action on Mac.

    1. Open `System Preferences`
    2. Open `Keyboard`
    3. Open `Modifier Keys...`
    4. Change `Caps Lock Key` to `No Action`

2. Map the behavior of Caps Lock key to the Escape key using `Seil`.

    1. Click on `Change the caps lock key` in `Seil`
    2. Check `Change the caps lock key`
    3. Fill 53 (keycode of Escape) in the keycode text box

3. Map the behavior of the Escape key to the Caps key using `Seil`.

    1. Click on `Other keys` in `Seil`
    2. Check `Change Escape`
    3. fill 57 (keycode of the Caps Lock key) in the keycode text box.

## References

- [Map Keys in Linux](http://www.legendu.net/en/blog/map-keys-in-linux/)

- [Map Keys in Windows](http://www.legendu.net/misc/blog/map-keys-in-windows)
