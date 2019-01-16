UUID: bbe6ee36-67b0-44d2-8b61-f7c6b8f24bff
Status: published
Date: 2019-01-16 09:03:06
Author: Ben Chuanlong Du
Slug: gitignore-tips
Title: Gitignore Tips
Category: Programming
Tags: programming, Git, .gitignore

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Gitignore Example for Python
```
__pycache__
.mypy
.ipynb_checkpoints
```

## Gitignore Example for Java
```
### Java ###
*.class

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.ear

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*


### Gradle ###
.gradle
/build/
/out/

# Ignore Gradle GUI config
gradle-app.setting

# Avoid ignoring Gradle wrapper jar file (.jar files are usually ignored)
!gradle-wrapper.jar

# Cache of project
.gradletasknamecache

# # Work around https://youtrack.jetbrains.com/issue/IDEA-116898
# gradle/wrapper/gradle-wrapper.properties
```


## References

- [Gitignore API](https://www.gitignore.io/api)

- [Gitignore on GitHub](https://github.com/github/gitignore)

- https://medium.com/@petehouston/typical-gitignore-for-a-gradle-java-project-52cbe079a99c