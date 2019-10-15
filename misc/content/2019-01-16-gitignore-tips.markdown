Status: published
Date: 2019-10-15 21:44:27
Author: Ben Chuanlong Du
Slug: gitignore-tips
Title: Gitignore Examples
Category: Programming
Tags: programming, Git, .gitignore

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Online Tools

- [gitignore.io](https://www.gitignore.io/)

- [github/gitignore](https://github.com/github/gitignore)

## Gitignore Example for Python
```
__pycache__/
.ipynb_checkpoints/
venv/
target/
dist/
.coverage
.mypy
.mypy_cache
*.crc
*.egg-info/
```

## Gitignore Example for Java
```
# Java 
*.class

## BlueJ files
*.ctxt

## Mobile Tools for Java (J2ME)
.mtj.tmp/

## Package Files
*.jar
*.war
*.ear

# Gradle 
.gradle
/build/
/out/

## Ignore Gradle GUI config
gradle-app.setting

## Avoid ignoring Gradle wrapper jar file (.jar files are usually ignored)
!gradle-wrapper.jar

## Cache of project
.gradletasknamecache

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*

# Mac
.DS_Store

# IDE
.idea/

# Misc
core
*.log
deprecated

```
