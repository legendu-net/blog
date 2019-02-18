Status: published
Date: 2019-01-08 06:07:17
Author: Ben Chuanlong Du
Slug: install-java8-in-mac
Title: Install Java 8 in Mac 
Category: macOS
Tags: Java, macOS, Homebrew

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Uninstall the default Java (which has a higher version than 8).

    brew cask uninstall java

Install Java 8.

    brew tap caskroom/versions
    brew cask install java8

You can verify the version of Java using the command below.

	java -version


## References

https://stackoverflow.com/questions/24342886/how-to-install-java-8-on-mac

