---
title: Cygwin Come to Rescue Linux Fans on Windows
created: '2013-08-19T10:37:20-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: cygwin-come-to-rescue-linux-fans-on-windows
license: CC-BY-4.0
tags:
  - Linux
  - Windows
  - virtualization
  - software
  - Cygwin
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. It is suggested that you use 32 bit Cygwin as it has a better package support.

1. Some tools (e.g., terminator) are not included in the regular release of Cygwin,
   but can be installed using
   [Cygwin Ports](cygwin-ports).

1. Configuration files for many applications (e.g., bash and Vim)
   in Linux can be migrated to Cygwin directly
   and work out of the box.

1. You might get an error about "... unexpected token ..."
   if you edit your bash script in Windows and try to run it under Cygwin.
   You can fix the problem by convert DOS text file format to Unix/Linux text file format
   using the command `dos2unix`.
   You can do the opposite using the command `unix2dos`.

1. If you are running Cygwin behind a (corpate) firewall,
   you have to choose "use http proxy" when you install packages.

1. To install new packages,
   run the Cygwin installer again and select new packages that you want to install.
   Installed packages will be kept by default.
   There's a script `apt-cyg` witten by Stephen Jungels
   which gives users similar experience to `apt-get` and `apt` in Debian/Ubuntu.

1. You can use `keychain` to manager your SSH public key in Cygwin.

1. Sometimes Cygwin fails to download and install new packages
   (even there is no problem with the network and proxy).
   Restalling it can often solve the problem in this situation.

1. Use gawk instead if awk does not work in Cygwin.

1. It is best to put your configurations files in the \$HOME/archives.
   And link to the home directory in Cygwin.
   Do not put data directly in Cygwin,
   because it makes things not portable.

1. The `rename` utility on Cygwin/MobaXterm has very limited functionality.
   It mimics the `rename` command on older version (2.6) of Linux.
   The new version of `rename` (on latest version of Linux)
   is not compatible with the older version one (on Cygwin/MobaXterm).

1. By default,
   the `PATH` environment variable in Cygwin contains some Windows executable paths
   before Cygwin executable paths.
   This shelter some Linux commands from being used directly.
   For example, Windows has a `find` command which might shelter the Linux `find` command.
   If this is case, you can either use the full path to the Linux `find` command,
   or you can put it into a Cygwin executable path before Windows executable paths.
   Sometimes, this causes seriously problems.
   For example, if you install R and its executables into the PATH environemtn variable,
   its executables shelter Cygwin's and make it not work well.
   It is suggested that you manually prepend $HOME/bin, /usr/local/bin, /usr/bin, etc.
   into $PATH in the `.bashrc` file in Cygwin.

## Recommended Packages

### Compiler Related

1. make, cmake

### Python Related

python-dateutil (via [Cygwin Ports](cygwin-ports)), python-pip (manually)

```bash
pip install python-dateutil
```

python-setuptools (contains easy_install)

However, notice that if you have Python (e.g., Anaconda Python) installed on Windows,
it might confuse yourself about which one you are using ...
Avoid installing Python on Windows if you have it installed in Cygwin
or at least be careful about the path ...

it seems to me that the best way to install Python packages on Cygwin is to use Python directly,

```bash
python setup.py --install package_name
```

#### Packages that Fail to Work

1. FuzzyWuzzy

1. NLTK

1. NumPy

### Git Related

1. git

1. git-completion (required for Git to auto complete in Cygwin)

### Editor

1. Vim

### Text Manipulation Tools

1. colordiff

## Available Tools Installed by Default

1. cd, ls, cp, mv, chmod, chown, ln

1. du, df

1. grep, sed, awk

### Availabe Tools not Installed by Default

1. terminator (available via [Cygwin Ports](cygwin-ports))

1. shutdown, halt, reboot (availabe via the `shutdown` package)

1. openssh-client, scp, rsync, keychain (keyring for ssh)

1. wget (better supported in 32 bit version of Cygwin until 1.7.35), curl, unison, w3m

1. gcc, git

1. screen (no help doc available, which is odd)

1. Vim

1. pdftk (only available on 32 bit as of Mar 6, 2015)

1. tmux

1. convert (in the ImageMagic package)

1. rename (available via the util-linux package,
   not as powerful as rename in linux but OK for simple batch rename)

1. clear (available via the ncurses package)

1. TexMacs

1. Texlive

1. dos2unix, unix2dos

## Missing Tools

1. openssh-server

1. dvipng

1. netstat (use X-NetStat as an alternative)

1. pandoc, wkhtmltopdf, pdfgrep
