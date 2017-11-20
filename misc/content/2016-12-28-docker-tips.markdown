UUID: 05e465c7-cb32-400b-9101-52043a8c6876
Status: published
Date: 2017-11-18 10:35:35
Author: Ben Chuanlong Du
Slug: docker-tips
Title: Docker Tips
Category: Software
Tags: software, docker, container, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


- [DockOne.io，最专业的Docker交流平台] (http://dockone.io/)
- [Docker在Coding WebIDE项目中的运用] (http://www.infoq.com/cn/articles/the-apply-of-docker-in-coding-webide-project)

## General Tips

1. Never mount a volume into `$HOME`!
Mount to `/user_name` instead.


## Docker Commands

```bash
service docker restart
docker run -it ubuntu:16.04
docker run -dit -p 80:80 -v /wwwroot:/usr/local/apache2/htdocs/ httpd
```

## Sharing Files

Copying file between a docker container and the host.
docker cp foo.txt mycontainer:/foo.txt 
docker cp mycontainer:/foo.txt foo.txt


## Links

[Private Docker Registry](https://docs.docker.com/registry/deploying/)

[Configure automated builds on Docker Hub](https://docs.docker.com/docker-hub/builds/)

[Configure automated builds with Bitbucket](https://docs.docker.com/docker-hub/bitbucket/)

https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/

https://coderwall.com/p/4g8znw/things-i-learned-while-writing-a-dockerfile

http://stackoverflow.com/questions/25311613/docker-mounting-volumes-on-host

http://stackoverflow.com/questions/26500270/understanding-user-file-ownership-in-docker-how-to-avoid-changing-permissions-o

https://chrisjean.com/fix-apt-get-update-the-following-signatures-couldnt-be-verified-because-the-public-key-is-not-available/

https://github.com/docker/docker/issues/22599

http://stackoverflow.com/questions/28056522/access-host-database-from-a-docker-container

https://docs.docker.com/engine/reference/commandline/tag/

https://docs.docker.com/engine/reference/commandline/push/

### Communicate with Host

http://stackoverflow.com/questions/23439126/how-to-mount-host-directory-in-docker-container

http://stackoverflow.com/questions/22907231/copying-files-from-host-to-docker-container

http://stackoverflow.com/questions/23935141/how-to-copy-docker-images-from-one-host-to-another-without-via-repository

### UI Related

1. [Running GUI Apps with Docker](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)
2. <http://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-docker-container>
2. <https://github.com/kevana/ui-for-docker>
2. <https://www.eclipse.org/community/eclipse_newsletter/2015/june/article3.php>
2. <https://hub.docker.com/r/tiokksar/eclipse/~/dockerfile/>
2. <https://hub.docker.com/r/tiokksar/eclipse/~/dockerfile/>
2. <https://medium.com/google-cloud/my-ide-in-a-container-49d4f177de#.2mhkzmp8a>
2. <https://blog.jessfraz.com/post/docker-containers-on-the-desktop/>
2. <https://store.docker.com/community/images/consol/ubuntu-xfce-vnc>

### Misc

1. <https://getcarina.com/docs/troubleshooting/stop-nonresponsive-running-container/>
2. <https://medium.com/@saturnism> 
3. <http://openhome.cc/Gossip/CodeData/DockerLayman/DockerLayman3.html>
4. <https://twitter.com/saturnism/status/645366585981538304>


1. [Docker Reference](https://docs.docker.com/engine/reference/builder/)

2. [Best practices for writing Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)

