Status: published
Date: 2017-06-22 13:26:28
Author: Ben Chuanlong Du
Slug: install-gnu-utils-using-homebrew
Title: Install GNU Utils Using Homebrew
Category: OS
Tags: macOS, Homebrew, GNU
Modified: 2021-08-02 09:35:28


Installing GNU tools is a way to try to get Linux command experience in macOS. 
However, 
not every Linux command has an identical-experience version in macOS.
It is suggested that you use a Linux virtual machine 
if you really want to have Linux experience in macOS.
Notice that some hardwares (USB) can be accessed directly in virtual machines,
which makes Linux virtual machines even more useful.
For example, 
you can connect a flash drive into a Linux VM 
and format the flash drive in the Linux VM. 

# Configuration

Run the following command in terminal before you install any GNU utils using Homebrew.
It will ensures that the installed GNU utils get used by default.

```bash
export PATH="/usr/local/opt/findutils/libexec/gnubin:$PATH"
export MANPATH="/usr/local/opt/findutils/libexec/gnuman:$MANPATH"
```

Notice that upgrading your Mac OS will reset the 2 environment variables.
So you will have to run the above commands again after you upgrading your Mac OS.

## Popular Tools

brew install coreutils e2fsprogs dosfstools

brew --prefix e2fsprogs
/usr/local/opt/e2fsprogs/sbin/

brew --prefix dosfstools
/usr/local/opt/dosfstools/sbin/

# GNU Core Utils

```bash
brew install coreutils
```

# Key Commands

```bash
brew install binutils
brew install diffutils
brew install ed --default-names
brew install findutils --with-default-names
brew install gnu-indent --with-default-names
brew install gnu-sed --with-default-names
brew install gnu-tar --with-default-names
brew install gnu-which --with-default-names
brew install gnutls
brew install grep --with-default-names
brew install gzip
brew install screen
brew install watch
brew install wdiff --with-gettext
brew install wget
```

# OS X ships a GNU version, but too old

```bash
brew install bash
brew install emacs
brew install gdb # gdb requires further actions to make it work. See `brew info gdb`.
brew install gpatch
brew install m4
brew install make
```

# Other commands (non-GNU)

```bash
brew install file-formula
brew install git
brew install less
brew install openssh
brew install python
brew install rsync
brew install svn
brew install unzip
brew install vim --override-system-vi
brew install macvim --override-system-vim --custom-system-icons
brew install neovim --override-sytem-vim
brew install zsh
```

# References

[Install and Use GNU Command Line Tools in Mac OSX](https://www.topbug.net/blog/2013/04/14/install-and-use-gnu-command-line-tools-in-mac-os-x/)
