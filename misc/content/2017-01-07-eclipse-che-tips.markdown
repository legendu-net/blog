UUID: 238e6a1a-0b18-457c-98ad-1a7fbdc0c6d5
Status: published
Date: 2017-03-05 21:30:21
Author: Ben Chuanlong Du
Slug: eclipse-che-tips
Title: Eclipse Che Tips
Category: Software
Tags: software, cloud IDE, Eclipse Che, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Even thought some features that I like (e.g., vim bindings, Scala support) 
are not complete,
it is usable and cool!

1. need to run project via customized command
for Maven project, use the maven plugin `exe-maven-plugin` to help run the application.

http://hmkcode.com/how-to-run-execute-java-main-class-using-maven-command/

## Eclipse Che in Docker

The simplest way to luanch Eclipse Che is via the Eclipse Che launcher image.
```bash
# pull the latest Eclipse Che launcher image
docker pull eclipse/che-launcher

# or if you'd rather run a specific version
docker pull eclipse/che-launcher[:tag]
```
```bash
# run the latest docker image
docker run --rm -t -v /var/run/docker.sock:/var/run/docker.sock eclipse/che-launcher start

# or if you'd rather run a specific version
docker run --rm -t -v /var/run/docker.sock:/var/run/docker.sock eclipse/che-launcher[:tag] start
```
Please refer to 
<https://eclipse-che.readme.io/docs/usage-docker>
for more details.

If you'd like to have more control over the Eclipse Che server, 
you can launch it directly.
Please refer to 
[Docker Installation](https://eclipse.org/che/docs/setup/docker/index.html)
for more details.

