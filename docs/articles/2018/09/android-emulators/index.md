---
title: Android Emulators
created: '2018-09-12T23:41:58-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: android-emulators
license: CC-BY-4.0
tags:
  - software
  - Android
  - emulation
  - emulator
  - AnBox
  - VirtualBox
  - xDroid
---

```{list-table} Android Emulators
---
widths: auto
header-rows: 1
---
- - Name
  - Free
  - OS
  - Hyper-v Compat on Win
  - ARM-only App Support
  - Development
- - [GenyMotion](https://www.genymotion.com)[^genymotion]
  - Limited
  - Windows, macOS, Linux
  - Partial
  - Limited
  - Active
- - [BlueStacks](https://www.bluestacks.com)[^bluestack]
  - Yes
  - Windows, macOS (M chip)
  - No
  - Yes
  - Active
- - [LDPlayer](https://www.ldplayer.net)[^ldplayer]
  - Yes
  - Windows
  - No
  - Yes
  - Active
- - [xDroid](https://www.linzhuotech.com/index.php/home/index/xdroid.html)[^xdroid]
  - Limited
  - Linux
  - NA
  - Limited
  - Slow
- - [MuMu App Player](https://mumu.163.com)[^mumu]
  - Yes
  - macOS (M chip)
  - No
  - Yes
  - Active
- - [腾讯手游助手](https://syzs.qq.com)
  - Yes
  - Windows
  - No
  - Yes
  - Active
- - [Waydroid](https://waydro.id)[^waydroid]
  - Yes
  - Linux
  - NA
  - Yes
  - Slow
- - [AnBox Cloud](https://anbox-cloud.io)[^anbox-cloud]
  - Limited
  - Ubuntu
  - NA
  - ?
  - Active
- - [Smartphone Simulator (Chrome extension)](https://www.webmobilefirst.com/en/)[^smartphone-simulator]
  - Limited
  - Windows, macOS, Linux
  - NA
  - ?
  - Active
- - [Android-x86 + VM](https://www.android-x86.org)[^android-x86]
  - Yes 
  - Windows, macOS, Linux 
  - Yes 
  - Limited 
  - Inactive 
- - [Android SDK + Android Studio](https://developer.android.com/studio)[^android-sdk]
  - Yes 
  - Windows, macOS, Linux 
  - ? 
  - Yes 
  - Active 
- - [docker-android](https://github.com/budtmo/docker-android)[^docker-android]
  - Yes 
  - Windows, macOS, Linux 
  - Yes 
  - Limited 
  - Active 
```

## References

- [Waydroid | Android in a Linux container](https://waydro.id/)

- [Setting up Android-x86 with Virt-Manager - ROllerozxa](https://voxelmanip.se/2022/07/12/setting-up-android-x86-with-virt-manager/)

- [Run ARM apps on the Android Emulator](https://android-developers.googleblog.com/2020/03/run-arm-apps-on-android-emulator.html)

- [安卓虚拟键盘_干货分享：推荐几款性能不错的安卓模拟器](https://blog.csdn.net/weixin_39991222/article/details/109897655?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control)

- [Android Emulators @ GameTechWiki](https://emulation.gametechwiki.com/index.php/Android_emulators)

- [Tips on Virtualbox](tips-on-virtualbox)

- [x86 Virtualization in Browser](https://copy.sh/v86/)

- [Run ARM apps on the Android Emulator](https://android-developers.googleblog.com/2020/03/run-arm-apps-on-android-emulator.html)

- [HQarroum/docker-android @ GitHub](https://github.com/HQarroum/docker-android)

- [Shmayro/dockerify-android @ GitHub](https://github.com/Shmayro/dockerify-android)

- [remote-android/redroid-doc @ GitHub](https://github.com/remote-android/redroid-doc)

- [budtmo/docker-android @ GitHub](https://github.com/budtmo/docker-android)

[^genymotion]: [GenyMotion](https://www.genymotion.com/) works well.

[^bluestack]: [BlueStacks](https://www.bluestacks.com/) works well.

[^ldplayer]: [LDPlayer](https://www.ldplayer.net/) is also called 雷电模拟器 in Chinese. It works well.

[^xdroid]: [xDroid](https://www.linzhuotech.com/index.php/home/index/xdroid.html)
    can run but has various issues.

[^mumu]: [MuMu App Player](https://mumu.163.com/) works well. Specially, Tribal Pioneer works on MuMu App Player on macOS.

[^waydroid]: [Waydroid] is a container-based approach to boot a full Android system on Linux.
    It is a successor of AnBox.

[^anbox-cloud]: [AnBox Cloud](https://anbox-cloud.io/) is developed by Canonical and works on Ubuntu only.

[^smartphone-simulator]: [Smartphone Simulator (Chrome extension)](https://www.webmobilefirst.com/en/) is a Chrome extension.

[^android-x86]: [Android X86](https://www.android-x86.org/)
    provides ISO images and RPM files for Fedora Linux distributions.
    ISO images can be used with VM tools (such as KVM, VirtualBox, VMware, etc)
    just like you can other operating systems in virtual machines.
    It's currently inactive and ISO images are outdated.

[^android-sdk]: [Android SDK and Android Studio][android-studio] works together to emulate software found on Android
    using the resources of your PC.
    Android developers mostly use Android SDK tools for testing and development purposes,
    but it'll work for casual use and play as well.

[^docker-android]: [Docker-Android] is a docker image
    built to be used for everything
    related to mobile website testing and Android project.

[android-studio]: https://developer.android.com/studio
[docker-android]: https://github.com/budtmo/docker-android
[waydroid]: https://waydro.id
