Status: published
Date: 2012-09-30 19:30:05
Author: Ben Chuanlong Du
Title: Windows Operating System
Slug: tips-windows
Category: OS
Tags: tips, anti-virus, Windows, Dropbox, OS
Modified: 2021-09-10 10:13:26

<img src="http://dclong.github.io/media/windows/windows.png" height="200" width="240" align="right"/>

## Tips and Traps

1. You can download a Windows 10 Virtual Machine at 
    [Get a Windows 10 development environment](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/) 
    !

1. [winget](https://github.com/microsoft/winget-cli)
    is the official Windows Package Manager CLI
    and
    [Chocolatey](https://chocolatey.org/) 
    is a cool community-driven software management tool for Windows.

1. When a file is being synchronized by Dropbox,
    it might be unaccessible temporarily. 
    If this happens, 
    you can simplify retry accessing it or you can quit Dropbox and try again.

2. Though you can also use `/` as the delimiter for paths in Windows system sometimes, 
    you can only use `\` as the delimiter for paths when you use DOS command, 
    because `/` has been already used for other meanings in DOS command.

3. `?` stand for a single character in DOS command, 
    and `??` stand for one or two characters.

4. A good way to manage Windows udpate is to disable Windows update for 7 days,
    update Windows and then disable Windows update for another 7 days,
    and repeat this cycle.
    This way you can keep your Windows up-to-date 
    while avoding being interrupted by Windows Auto Update too much.
    It is critical to disable Windows Auto Update/Restart (best for 7 days)
    before you run a long-running task on Windows.

## Add a Right-click Menu

To add an entry into the right-click menu in Windows, 
edit the registry following the steps below.

1. Navigate to the key `HKEY_CLASSES_ROOT\Directory\Background\shell` in the registry.

2. Create another key with any name (e.g., rstudio) under `HKEY_CLASSES_ROOT\Directory\Background\shell`. 

3. Set a value (e.g., Rstudio) for the newly created key (rstudio)
    in the right-side pane of the registry.
    This value (Rstudio) shows up in the right-click menu whenever you right click.

4. Create another key named `command` under the newly created key (rstudio).

5. Set the value of the newly created key `command` 
    to be the full path of the application
    (e.g., `C:\Program Files\RStudio\bin\rstudio.exe`)
    that you want to launch.

