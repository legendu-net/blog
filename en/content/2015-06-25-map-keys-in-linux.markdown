UUID: 9ba8c173-8851-4beb-bda4-a68e1360a23f
Status: published
Date: 2017-03-04 13:12:16
Author: Ben Chuanlong Du
Slug: map-keys-in-linux
Title: Map Keys in Linux
Category: Linux
Tags: Linux, keyboard, mapping, swap, setxkbmap, Cinnamon, GNOME, keys

## Desktop Environment

Some desktop environment (e.g., GNOME, Cinnamon, etc.) can do this for you.
For exampel, 
you can follow the steps below to map the Caps Lock key in Cinnamon.

1. Open System Settings.
2. Select Keybord.
3. Keybord layouts 
4. Options (on the right-bottom corner) 
5. Caps Lock key behavior
6. Choose the behavior you want.

For Unity desktop, you need to install `unity-tweak-tool`. 
And if you are on GNOME desktop, you need `gnome-tweak-tool`.


## setxkbmap

Swap the Caps and the Escape keys.
```bash
setxkbmap -option -option caps:swapescape
```

Unfortunately, the key mapping partially pass to virtual machines or remote desktops,
which is the worst scenario. 
It is suggested that you turn off the mapping on the Linux host 
when you work in a VM or a remote desktop.


## More References

- <http://askubuntu.com/questions/444714/how-do-i-swap-escape-and-caps-lock-in-14-04/446725#446725>

- <http://www.fascinatingcaptain.com/howto/remap-keyboard-keys-for-ubuntu/>

- <http://askubuntu.com/questions/885045/how-to-swap-ctrl-and-alt-keys-in-ubuntu-16-04/885047>

- <http://askubuntu.com/questions/453793/remapping-caps-lock-in-14-04-trusty-tahr>

- <http://askubuntu.com/questions/444714/how-do-i-swap-escape-and-caps-lock-in-14-04/446725#446725> 
