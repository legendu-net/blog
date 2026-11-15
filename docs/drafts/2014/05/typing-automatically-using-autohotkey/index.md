---
title: Typing Automatically Using AutoHotkey
created: '2014-05-22T13:34:48-07:00'
date: '2026-11-15T09:16:41-08:00'
authors:
  - bendu
label: typing-automatically-using-autohotkey
license: CC-BY-4.0
tags:
  - tips
  - software
  - AutoHotkey
  - automation
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. it is suggested that you put things into

   ```AutoHotkey
   #IfWinActive window_condition
   ...
   #IfWinActive
   ```

## Include

3. You can use `#include file_path` to include a AutoHotKey scripts
   (as if the content of the included file appears exactly there).

   use #include path_to_dir to change the working directory for subsequent #includes
   and then use #include with relative path
   this makes things much more conveninet

## Syntax

2. Lines that start with a semicolon are comments and thus not executed.

1. Commands in AutoHotkey are case-insensitive.

1. `!` is a special character in AutoHotkey and is cannot be used directly in hotstrings.
   Use `{!}` to represent a literal `!`.
   {{} literal {
   {}} literal }

1. Leading/trailing spaces in hotstring definitions are ignored.
   To use literal leading/trailing spaces in a hotstring definition,
   use \{Space} instead.
   Actually you always use \{Space} to replace literal spaces.

1. \{+} literal plus

1. You cannot put `;comment` after a command in a line, instead, you have to start a new line
   \`\`\`%\`\`: literal % or you can use continuation mode () or use SendRaw ...

1. take another look at the ignoring case functionality!!!

1. ``````is a special character in AutoHotkey.
    if you want to use AutoHotkey to automatically type in password for in,
    you cannot use ````` in the password.

   ``````

## General Tips

1. Do not define too many hotstrings that you even do not remember to use.
   Generally speaking,
   only whole (long) sentences and extremely frequently used short phrases are useful.

1. When sending a key, you can specify the number of repeated time instead of doing it manually.
   For example,
   instead of `send {Left}{Left}{Left}`, you can use `send {Left 3}`.

1. You can use `GroupAdd` to define window groups
   (to be used by `IfWinActive` or `#IfWinActive`.

1. `#IfWinActive` (without anything following) matches any window.

1. Symbolic links (made in Cygwin/MobaXterm) and shortcuts (created in Windows) of scripts cannot be used for AutoHotkey.
   However, hard links (made in Cygwin/Mobaxterm) work well.

1. Order of hotstring and hotkeys matters.
   For example,
   if you have both `/u` and `u` defined in AutoHotkey,
   you have to put `/u` before `u`.
   Otherwise, `u` will be triggered when you type in `/u`.
   Generally speaking, if you have two hotstrings/hotkeys `A` and `B` defined and `B` is a substring of `A`,
   you need to put the definition of `A` before `B`.

1. AutoHotkey ignores the case of triggers by default,
   which makes hotstrings to adjust cases according to cases of triggers.
   For example,
   if you define `:O:mma:mathematica`,
   then `MMA` is expanded to `MATHEMATICA`, `Mma` is expanded to `Mathematica`
   and `mma` is expanded to `mathematica`.

## `ahk_class` of Windows

0. You can use `AU3_Spy.exe` to get the `ahk_class` information of a window.

1. IMWindowClass: Microsoft Lync Office Communicator

1. MozillaWindowClass: Firefox

1. MozillaUIWindowClass: Thunderbird

1. IEFrame: IE Explorer

1. rctrl_renwnd32: Outlook

1. Chrome_WidgetWin_1: Chrome

1. PuTTY: putty

1. mintty: mintty

## Useful Options/Functions/Commands

1. `SetTitleMatchMode` sets the matching behavior of the WinTitle parameter in commands such as WinWait.

1. `IfWinActive`/`IfWinNotActive`

## Questions

1. How to reuse path?
   and is it possible to use windows environment variables in AutoHotkey scripts?

1. is it possible to specify a different script location?

1. can ahk be used with regular expression?

1. is it possible to let AutoHotkey popup a list of values to choose from like AutoKey does?
   This makes things more convenient many times ...

## References

- [AutoHotkey @ GitHub](https://github.com/Lexikos/AutoHotkey_L)
