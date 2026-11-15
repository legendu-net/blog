---
title: Install Firefox and Thunderbird Automatically on Debian
created: '2014-10-22T13:20:50-07:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: install-firefox-and-thunderbird-automatically-on-debian
license: CC-BY-4.0
tags:
  - software
  - installation
  - Thunderbird
  - Firefox
  - todo
  - Debian
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

```
#!/usr/bin/env bash

# download latest thunderbird
path=ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/latest/linux-$(uname -m)/en-US/
dir=$(mktemp -d)
echo "Temporary directory \"$dir\" is created."
cd $dir
echo "Downloading thunderbird into \"$dir\" ..."
wget -r --no-parent -e robots=off http://$path
path=$(ls $path/thunderbird-*)
filename=$(basename $path)
cp $path $filename
# decompress thunderbird installation files
echo "Decompressing thunderbird installation file ..."
if [ "$filename" == *.tar.bz2 ]; then
    option=-jxvf
elif [ "$filename" == *.tar.gz ]; then
    option=-zxvf
else
    echo "Unrecognized installation file!"
    return 1
fi
tar $option $filename
# copy to /opt
echo "Copying thunderbird to /opt ..."
sudo rm -rf /opt/thunderbird
sudo cp -r thunderbird /opt/
# uninstall icedove
if [ "$(sudo apt list | grep -i icedove)" != "" ]; then
    # sudo apt purge -y icedove
    echo "Please uninstall icedove."
fi
```
