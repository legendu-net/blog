Status: published
Date: 2016-05-04 20:59:32
Modified: 2021-09-26 21:56:03
Author: Ben Chuanlong Du
Slug: things-to-do-after-installing-linux
Title: Things to Do After Installing Linux
Category: OS
Tags: Linux, OS, installation

1. Choose a fast mirror.
    If you are using Ubuntu, 
    a fast mirror will be automatically decided based on your location. 
    However, if you are using other Linux distribution (e.g., Linux Mint),
    you might have to choose a fast mirror manually.

2. Configure `vm.swapness` to be a proper value (10 or even less),
    if your Linux system has a large swap partition.
    For more details,
    please refer to
    [SwapFaq](https://help.ubuntu.com/community/SwapFaq)
    .

3. Install a good alternative package manager.
    `apt-get` is a very good package manager for Debian series Linux distributions,
    however, `wajig` is much superior choice.
        
        :::bash
        sudo apt-get install wajig

4. Upgrade the system.
        
        :::bash
        wajig update && wajig upgrade

5. Swap the `Caps Lock` key with the `Escape` key.

6. install must have software

    - aria2, uGet
    - install and configure Chrome/Firefox 
    - Sogou Pinyin
    - transimission
    - Dropbox

This list might not be the best for everyone. 
For a general list of useful software/tools for Linux, 
please check the post [Useful Tools in Linux](http://www.legendu.net/misc/blog/useful-tools-linux/).
