UUID: 1f692e94-c786-4ba2-be36-1e6836f6f1ac
Status: published
Date: 2017-06-11 19:39:54
Author: Ben Chuanlong Du
Slug: install-gnu-utils-using-homebrew
Title: Install GNU Utils Using HomeBrew
Category: Programming
Tags: programming

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

It is suggested that you use MacPorts (which has more packages) instead of HomeBrew.
But if you do prefer HomeBrew, 
follow the guidelines below.

PATH="/usr/local/opt/findutils/libexec/gnubin:$PATH"
MANPATH="/usr/local/opt/findutils/libexec/gnuman:$MANPATH"

# core
brew install coreutils

# key commands
brew install binutils
brew install diffutils
brew install ed --default-names
brew install findutils --with-default-names
brew install gawk
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

# OS X ships a GNU version, but too old
brew install bash
brew install emacs
brew install gdb # gdb requires further actions to make it work. See `brew info gdb`.
brew install gpatch
brew install m4
brew install make
brew install nano

# Other commands (non-GNU)
brew install file-formula
brew install git
brew install less
brew install openssh
brew install perl518 # must run "brew tap homebrew/versions" first!
brew install python
brew install rsync
brew install svn
brew install unzip
brew install vim --override-system-vi
brew install macvim --override-system-vim --custom-system-icons
brew install zsh

[Install and Use GNU Command Line Tools in Mac OSX](https://www.topbug.net/blog/2013/04/14/install-and-use-gnu-command-line-tools-in-mac-os-x/)
