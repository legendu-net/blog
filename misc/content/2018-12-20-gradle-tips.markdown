UUID: 6d113de7-4f66-4e73-aba8-e0d61e53be4b
Status: published
Date: 2018-12-20 10:13:28
Author: Ben Chuanlong Du
Slug: gradle-tips
Title: Gradle Tips
Category: Programming
Tags: programming, JVM, Java, gradle, Groovy, compile, compiler, package management

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Installation 
You can use the following command to install the latest version of gradle on Ubuntu.
```
sudo add-apt-repository ppa:cwchien/gradle
sudo apt-get update
sudo apt upgrade gradle
```
You can use the following command to install Gradle on Mac.
```
brew install gradle
```

## Tricks and Traps

1. You'd better rebuild (using the `build` command) your project 
    before testing running your project or generating a fat jar (using the `shadowjar` command).
    Otherwise, 
    you might run into weird issues such as resource file not found, etc.

## References

https://askubuntu.com/questions/932083/how-do-i-upgrade-gradle
