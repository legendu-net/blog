UUID: a96776f9-5501-4c6a-9e2b-ccf0f8f1718b
Status: published
Date: 2016-07-09 19:14:22
Author: Ben Chuanlong Du
Slug: map-keys-in-mac
Title: Map Keys in Mac
Category: Apple
Tags: Mac, Apple, OS X, mapping, keys

[Seli](https://pqrs.org/osx/karabiner/seil.html.en)
(previouly known as PCKeyboardHack) is great tool for mapping keys on Mac.
Let me illustrate how to use `Seli`.
As a heavy Vim user, 
I find it is necessary to swap the `Caps Lock` key with the `Escape` key.

1. Change the behavior of Map Caps Lock Key to No Action on Mac.

    1. Open `System Preferences`
    2. Open `Keyboard`
    3. Open `Modifier Keys...`
    4. Change `Caps Lock Key` to `No Action`

2. Map the behavior of Caps Lock key to the Escape key.

    1. Click on `Change the caps lock key`
    2. Check `Change the caps lock key`
    3. Fill 53 (keycode of Escape) in the keycode text box 

3. Map the behavior of the Escape key to the Caps key.

    1. Click on `Other keys`
    2. Check `Change Escape`
    3. fill 57 (keycode of the Caps Lock key) in the keycode text box.

