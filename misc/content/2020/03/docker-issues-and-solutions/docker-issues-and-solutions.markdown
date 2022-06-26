Status: published
Date: 2020-03-14 09:56:34
Author: Benjamin Du
Slug: docker-issues-and-solutions
Title: Docker Issues and Solutions
Category: Software
Tags: Software, Docker, issue, solution
Modified: 2022-06-02 16:53:37

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## [Multiprocessing Issues in Docker](http://www.legendu.net/misc/blog/multiprocessing-issues-in-docker/)

## Docker Out of Disk Space

[What to Do When Docker on the Mac Runs Out of Space](https://rmoff.net/post/what-to-do-when-docker-runs-out-of-space/)

## Docker fail to register layer  ... no such file or directory

1. Remove `/var/lib/docker/*`.

        :::bash
        sudo rm -rf /var/lib/docker/*

    If you have a non-standard Docker location configured,
    then rmeove that location instead.

2. Restart Docker.

        :::bash
        sudo service docker restart

## Error response from daemon: failed to start shim: exec: "docker-containerd-shim": executable file not found in $PATH: unknown.

Restart docker resolves the issue.

    :::bash
    sudo service docker restart

## Error saving credentials: error storing credentials in Ubuntu 18.04 LTS

Installing `gnupg2` and `pass` fixes the issue.

    :::bash
    wajig install gnupg2 pass

## Container exits with non-zero exit code 137

Please refer to
[The Non-Zero Exit Code 137 While Building a Docker Image](http://www.legendu.net/misc/blog/the-non-zero-exit-code-137-while-building-a-docker-image/)
for more details.

## Debuging Docker Container Exit

1. List Docker container IDs. 

        :::bash
        docker ps -a

2. Check logs of a Docker container.

        :::bash
        docker logs container_id

3. Inspect a Docker container.

        :::bash
        docker inspect container_id

If the above does not help you identify the cause of Docker container exit,
you can inspect the logs of the Docker daemon.
The StackOverflow question
[Where is the Docker daemon log?](https://stackoverflow.com/questions/30969435/where-is-the-docker-daemon-log)
has a good discussion on where/how to find Docker daemon logs.
In case you need to figure out which init system your Linux OS is using,
please refer to the post
[Check Whether a Linux Is Using Upstart Systemd or SysV](http://www.legendu.net/misc/blog/check-whether-a-linux-is-using-upstart-systemd-or-sysv)            
.

[Why Does My Docker Container Stop?](https://www.tutorialworks.com/why-containers-stop/)

## References

- https://github.com/docker/cli/issues/1136

- [The Non-Zero Exit Code 137 While Building a Docker Image](http://www.legendu.net/misc/blog/the-non-zero-exit-code-137-while-building-a-docker-image/)

- [Why Does My Docker Container Stop?](https://www.tutorialworks.com/why-containers-stop/)