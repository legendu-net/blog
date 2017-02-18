UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2014-12-16 20:04:38
Slug: tips-windows
Author: Ben Chuanlong Du
Title: Tips for Windows Operating System
Category: Windows
Tags: tips, anti-virus, Windows, Dropbox, OS

<img src="http://dclong.github.io/media/windows/windows.png" height="200" width="240" align="right"/>

## Tricky Problem

1. When Dropbox is working on files, they might become unaccessible
temporarily. If you believe a problem is result from Dropbox, you
can try your operation again. If it still does not work, then quit
Dropbox and redo your operations.

## Tips

To add an entry into the right-click menu in Windows, 
edit the registry following the steps below.

1. Navigate to the key
`HKEY_CLASSES_ROOT\Directory\Background\shell`
in the registry.

2. Create another key with any name (e.g., rstudio) under 
`HKEY_CLASSES_ROOT\Directory\Background\shell`. 

3. Set a value (e.g., Rstudio) for the newly created key (rstudio)
in the right-side pane of the registry.
This value (Rstudio) shows up in the right-click menu whenever you right click.

4. Create another key named `command` under the newly created key (rstudio).

5. Set the value of the newly created key `command` 
to be the full path of the application
(e.g., `C:\Program Files\RStudio\bin\rstudio.exe`)
that you want to launch.


2. Though you can also use `/` as the delimiter for paths in Windows
system sometimes, you can only use `\` as the delimiter
for paths when you use DOS command, because `/` has been already
used for other meanings in DOS command.

3. `?` stand for a single character in DOS command, 
and `??` stand for one or two characters.

4. By default Windows 7 updates automatically unless you turn the auto
update off. This can be annoying if you do some long time computing
in Windows, because the auto-updating might force the computer to
reboot when the computing is still running. A way to solve this
problem is to turn off the auto-updating before you do computing in
Windows. However it is a convenient way, because you have to turn on
the auto-updating after the computing is done. A better way is to
lock your computer, in this way the auto-updating will be halt and
won't screw up your running program. What's more, this can also
prevent your privacy from other people. (Actually I have to check
whether it is because of lock or it is just because of the computer is
too busy.)

5. KIS under Setting/Firewall/Settings/Networks, 
edited my WiFi network from Public to Local Network

## VBScript

1. An VBScript is accesible anywhere if it is placed into a searchable path 
(a path included in the path environment). 

## Win XP

1. Disable the "Open file" Warning

开始 --> 运行 --> gpedit.msc--> 用户配置 --> 管理模板 --> windows组件 --> 附件管理器--> 右击 “中等危险文件类型的包含列表” --> 属性 --> 选 “已启用”

在 “中等危险文件类型的包含列表”里输入所要关闭警告的扩展名如.exe;.bat;.reg;.vbs 再点击确定。多个之间用分号隔开。

2. Win XP sometimes plays annoying sounds.
Turn off the firewall solves the problem.

