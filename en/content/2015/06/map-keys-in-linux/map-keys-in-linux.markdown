Status: published
Date: 2015-06-19 10:30:15
Author: Ben Chuanlong Du
Slug: map-keys-in-linux
Title: Map Keys in Linux
Category: OS
Tags: Linux, keyboard, mapping, swap, setxkbmap, Cinnamon, GNOME, keys
Modified: 2021-10-11 10:29:36

Note: For Vim users, it is appealing to make the `Caps Lock` function like `Escape`.
It is suggested that you make `Caps Lock` an additonal `Escape`
rather than swap them.
This avoid inconsistent key mapping issues when you work remotely via VNC, NoMachine, etc.

## Desktop Environment

Some desktop environment (e.g., Cinnamon, GNOME, etc.) let you define behavior of keys.

### GNOME

[How to use Caps Lock key as ESC on ubuntu 18](https://dev.to/yuyabu/how-to-use-caps-lock-key-as-esc-on-ubuntu-18-1g7l)


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
