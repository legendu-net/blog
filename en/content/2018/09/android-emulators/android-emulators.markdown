Status: published
Date: 2018-09-12 23:41:58
Author: Ben Chuanlong Du
Slug: android-emulators
Title: Android Emulators
Category: Software
Tags: software, Android, emulation, emulator, AnBox, VirtualBox, xDroid
Modified: 2023-02-05 18:30:10


<table style="width:100%">
  <tr>
    <th> Name </th>
    <th> Free </th>
    <th> OS </th>
    <th> Hyper-v Compat on Win</th>
    <th> ARM-only App Support </th>
    <th> Development </th>
  </tr>
  <tr>
    <td> 
    <a href="https://www.genymotion.com"> GenyMotion </a>
    <a href="#footnote1">[1]</a>
    </td>
    <td> No </td>
    <td> Windows, macOS, Linux </td>
    <td> Partial </td>
    <td> Limited </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.bluestacks.com"> BlueStacks </a>
    <a href="#footnote2">[2]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS </td>
    <td> No </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.ldplayer.net"> LDPlayer </a>
    <a href="#footnote3">[3]</a>
    </td>
    <td> Yes </td>
    <td> Windows </td>
    <td> No </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.linzhuotech.com/index.php/home/index/xdroid.html"> xDroid </a>
    <a href="#footnote1">[9]</a>
    </td>
    <td> Partial </td>
    <td> Linux </td>
    <td> NA </td>
    <td> Limited </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://waydro.id/"> Waydroid </a>
    <a href="#footnote1">[11]</a>
    </td>
    <td> Yes </td>
    <td> Linux </td>
    <td> NA </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://anbox-cloud.io/"> AnBox Cloud </a>
    <a href="#footnote4">[4]</a>
    </td>
    <td> No </td>
    <td> Windows, macOS, Linux </td>
    <td> NA </td>
    <td> ? </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://mumu.163.com"> MuMu App Player </a>
    <a href="#footnote5">[5]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS </td>
    <td> No </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://syzs.qq.com/"> 腾讯手游助手 </a>
    <a href="#footnote5">[6]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS </td>
    <td> No </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.android-x86.org"> Android-x86 + VirtualBox </a>
    <a href="#footnote6">[7]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS, Linux </td>
    <td> Yes </td>
    <td> Limited </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://developer.android.com/studio"> Android SDK + Android Studio </a>
    <a href="#footnote7">[8]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS, Linux </td>
    <td> ? </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/budtmo/docker-android"> docker-android </a>
    <a href="#footnote1">[10]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS, Linux </td>
    <td> Yes </td>
    <td> Limited </td>
    <td> Active </td>
  </tr>
</table>

[1] [GenyMotion](https://www.genymotion.com/)
is a great cross-platform choice.
However, 
a licence must be purchased to use GenyMotion.
The desktop version of GenyMotion 
can be downloaded at
<https://www.genymotion.com/fun-zone/>
.

[2] [BlueStacks](https://www.bluestacks.com/) 
is a good free Android emulator for Windows and Mac.

[3] [LDPlayer](https://www.ldplayer.net/) (also called 雷电模拟器 in Chinese) 
is a good free Android emulator for Windows only.

[4] [AnBox](https://anbox.io/)
is an open-source WINE-like Android emulator for Linux only (CANNOT be run on macOS).
ARM apps can be run on x86-based Linux OS with Android 11+ images.
For more details,
please refer to
[Run ARM apps on the Android Emulator](https://android-developers.googleblog.com/2020/03/run-arm-apps-on-android-emulator.html)
.

[5] [MuMu App Player](https://mumu.163.com/)
is an Android emulator develop by the Chinese company Wangyi for Windows and macOS.
An English version is also availabe at https://mumu.163.com/global/download/en/.
Tribal Pioneer works on MuMu App Player on macOS!!!

[7] [Android X86](https://www.android-x86.org/)
is a project to port Android Open Source Project to x86 platform.
It works across operating systems (Windows, macOS and Linux).
Android X86 supports provides ISO and RPM files
rather than an out-of-the-box application.
You have to install an ISO or RPM file to you device 
which will add an Android operating system to your device.
You can of course install it into a virutal environemnt (e.g., using VirtualBox)
which is essentially what other out-of-the-box applications does.

[8] Android SDK and Android Studio works together to emulate software found on Android 
using the resources of your PC. 
Android developers mostly use Android SDK tools for testing and development purposes, 
but it'll work for casual use and play as well.

[9] xDroid is an Android emulator 
(seems to be a commerical software based on AnBox) 
for Linux only.
The x86_64 version is free for personal use.

[10] Docker-Android is a docker image 
built to be used for everything 
related to mobile website testing and Android project.

[11] Waydroid is a container-based approach to boot a full Android system on a regular GNU/Linux system like Ubuntu.
It is a successor of AnBox.

## References 

- [Run ARM apps on the Android Emulator](https://android-developers.googleblog.com/2020/03/run-arm-apps-on-android-emulator.html)

- [安卓虚拟键盘_干货分享：推荐几款性能不错的安卓模拟器](https://blog.csdn.net/weixin_39991222/article/details/109897655?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control)

- [Android Emulators @ GameTechWiki](https://emulation.gametechwiki.com/index.php/Android_emulators)

- [Tips on Virtualbox](http://www.legendu.net/misc/blog/virtualbox-tip)

- [x86 Virtualization in Browser](https://copy.sh/v86/)
