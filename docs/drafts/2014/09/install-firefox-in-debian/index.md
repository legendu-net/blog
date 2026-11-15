---
title: Install Firefox in Debian
created: '2014-09-13T22:21:27-07:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: install-firefox-in-debian
license: CC-BY-4.0
tags:
  - Linux
  - Firefox
  - Debian
  - web browser
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

you have to update your script based on the DE being used.
but first check whether a desktop file created in GNOME can be used in Xfce or not.

```
# download latest firefox
path=ftp.mozilla.org/pub/mozilla.org/firefox/releases/latest/linux-$(uname -m)/en-US/
dir=$(mktemp -d)
echo "Temporary directory \"$dir\" is created."
cd $dir
echo "Downloading firefox into \"$dir\" ..."
wget -r --no-parent -e robots=off http://$path
path=$(ls $path/firefox-*)
filename=$(basename $path)
cp $path $filename
# decompress firefox installation files
echo "Decompressing firefox installation file ..."
if [[ "$filename" == *.tar.bz2 ]]; then
    option=-jxvf
elif [[ "$extension" == *.tar.gz ]]; then
    option=-zxvf
else
    echo "Unrecognized installation file!"
    return 1
fi
tar $option $filename
# copy to /opt
echo "Copying firefox files to /opt ..."
sudo rm -rf /opt/firefox
sudo cp -r firefox /opt/
# install flashplugin-nonfree to make firefox more usable
echo "Installing flashplugin-nonfree ..."
sudo apt install -y flashplugin-nonfree
# uninstall iceweasel
if [ "$(sudo apt list | grep -i iceweasel)" != "" ]; then 
    # sudo apt purge -y iceweasel
    echo "Please uninstall iceweasel manually!"
fi
```
