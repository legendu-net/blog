---
title: Copy Pictures from an Android Phone to a Computer
created: '2015-09-12T23:41:58-07:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: copy-pictures-from-an-android-phone-to-a-computer
license: CC-BY-4.0
tags:
  - Linux
  - scp
  - rsync
  - pictures
  - image
  - photo
  - media
  - Android
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

You have to have a SSH server installed on the Android phone.

```bash
scp -r -P port user_name@192.168.1.105:/sdcard/DCIM .
scp -r -P port user_name@192.168.1.105:/sdcard/DCIM/Camera .
scp -r -P port user_name@192.168.1.105:/sdcard/Download .
scp -r -P port user_name@192.168.1.105:/sdcard/Tencent/MicroMsg/WeChat .
scp -r -P port user_name@192.168.1.105:/sdcard/Tencent/MicroMsg/WeiXin .
```

`/sdcard/DCIM`
`/sdcard/Download`
`/sdcard/MicroMsg`

Notice that `rsync` does not work on an Android phone.
