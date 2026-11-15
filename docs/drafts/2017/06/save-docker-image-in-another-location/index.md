---
title: Save Docker Image in Another Location
created: '2017-06-28T19:41:40-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: save-docker-image-in-another-location
license: CC-BY-4.0
tags:
  - software
  - Docker
  - location
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Docker images are saved in `/var/lib/docker`.
You can link the directory to another place to save images elsewhere.
Another way is to change the configuration file of Docker.
For example,
you can add the following into `/etc/default/docker`
to save docker images into `/mnt` (instead of the default location).

```
DOCKER_OPTS="-dns 8.8.8.8 -dns 8.8.4.4 -g /mnt"
```

1. symbolic link

1. bind mount (check
   [Specifying a default Docker storage directory by using bind mount](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/installing/docker_dir.html)
   for more details)

1. Add the options into the file `/etc/docker/daemon.json`.

   ```
    :::json
    {
        "data-root": "/new/data/root/path"
    }
   ```

Restart Docker after whichever approach you take.

```
:::bash
sudo systemctl restart docker
```

## References

https://forums.docker.com/t/how-do-i-change-the-docker-image-installation-directory/1169

https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/installing/docker_dir.html

https://stackoverflow.com/questions/19234831/where-are-docker-images-stored-on-the-host-machine
