Status: published
Date: 2015-06-19 10:30:15
Author: Ben Chuanlong Du
Slug: map-keys-in-linux
Title: Map Keys in Linux
Category: OS
Tags: Linux, keyboard, mapping, swap, setxkbmap, Cinnamon, GNOME, keys, Caps Lock, Escape
Modified: 2022-04-30 16:02:35

Note: For Vim users, it is appealing to make the `Caps Lock` function like `Escape`.
It is suggested that you make `Caps Lock` an additonal `Escape`
rather than swap them.
This avoid inconsistent key mapping issues when you work remotely via VNC, NoMachine, etc.

## Desktop Environment

Some desktop environment (e.g., Cinnamon, GNOME, etc.) let you define behavior of keys.

### GNOME

1. Install gnome-tweak-tool.
    You can use the following command 
    on Debian/Ubuntu based Linux distributions.

        :::bash
        wajig install gnome-tweak-tool

2. Start gnome-tweaks by running the following command.

        :::bash
        gnome-tweaks

3. Click on the "Keyboard & Mouse" button in the left panel 
    and then the "Additional Layout Options" button 
    under the Keyboard section. 
    ![gnome-tweaks-1](https://user-images.githubusercontent.com/824507/166125171-41a73a26-ec96-46bc-a72a-3ca2f771078b.png)

4. In the prompt dialog, 
    click on the triangle button next to "Caps Lock behavior"
    and then select the behavior you want for Caps Lock.
    ![gnome-tweaks-2](https://user-images.githubusercontent.com/824507/166125255-5f95211e-9c19-447e-9979-3cb01dd4ef7a.png)

5. Restart your Linux machine.

### Cinnamon

1. Open System Settings.

2. Select Keybord.

3. Keybord layouts

4. Options (on the right-bottom corner)

5. Caps Lock key behavior

6. Choose the behavior you want.

## Keyboard Configuration

Keyboard is configured by the file `/etc/default/keyboard` on Linux.
For example,
you can find the line that starts with `XKBOPTIONS`,
and add `ctrl:nocaps` to make Caps Lock an additional Control key
or `ctrl:swapcaps` to swap Caps Lock and Control.
Run the following command after updating the file `/etc/default/keyboard` to make it in effect.
```
sudo dpkg-reconfigure keyboard-configuration
```
This is the recommended way if you want to make key swaping persistent. 
Another advantage it has over GUI configuration and `setxkbmap` (see the next section)
is that the key swaping works in TTY (without X11 or Wayland).

## setxkbmap

Swap the Caps and the Escape keys.
```bash
setxkbmap -option -option caps:swapescape
```

Unfortunately,
the key mapping partially pass to virtual machines or remote desktops,
which is the worst scenario.
It is suggested that you turn off the mapping on the Linux host
when you work in a VM or a remote desktop.

## More References

- [Map Keys in macOS](http://www.legendu.net/en/blog/map-keys-in-mac/)

- [Map Keys in Windows](http://www.legendu.net/misc/blog/map-keys-in-windows)

- [How to permanently swap esc and caps lock in xfce / xubuntu?](https://unix.stackexchange.com/questions/66775/how-to-permanently-swap-esc-and-caps-lock-in-xfce-xubuntu)

- [How do I swap Escape and Caps Lock in 14.04?](http://askubuntu.com/questions/444714/how-do-i-swap-escape-and-caps-lock-in-14-04/446725#446725)
