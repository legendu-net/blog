UUID: c744cc45-eaa3-46e4-925d-a298beb815c0
Status: published
Date: 2018-04-22 17:42:23
Author: Ben Chuanlong Du
Slug: tips-for-running-docker-containers
Title: Tips for Running Docker Containers
Category: Software
Tags: software, docker, running, execute, container

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Permission

1. It is suggested that you have your user name added into the `docker` group
    so that you can run Docker commands without using `sudo`.

2. Inside a Docker container,
    files created belong to the user in the Docker container.
    If the files are created in a mounted host directory,
    then on the host these files belong to the user with the same user ID.

## Port

1. Do NOT forget to forward ports from the host to the Docker containers
    while using docker containers.
    For example,
    if you run a Flask application in a Docker,
    you have to forward a port on the host to the port 5000 in the Docker container.
    If you run multiple services in a Docker container (not recommended),
    you have to forward all needed ports into the Docker container.

## Volume

1. ALWAYS create a directory in the Docker container first
    before you mount a volume into it.
    If the directory (to mount into) in the Docker container does not exists,
    it will be created automatically by the root user
    (unless you specified a different user to run the Docker container).
    The newly created directory is owned by the root,
    which might not be as expected.

2. AVOID mounting a volume into your home directory in the Docker container.

    - You might screw up the permission of your home directory in the Docker container.

    - If you mount your home on the host into your home in the Docker container,
        you might accidentally overwrite things in your home directory on the host.

    It is recommend that you always mount a volume to `/some_dir` and then link to home if needed.

3. When you mount a volume from the host to a Docker container,
    make sure that you have the right permissions to the directory on the host,
    o.w., you might run into various issues (such as the Docker container fails to start).

## Sharing Files

Copying file between a docker container and the host.
docker cp foo.txt mycontainer:/foo.txt
docker cp mycontainer:/foo.txt foo.txt

## Misc

1. By default log in a Docker container is redirected to the standard output.
    However,
    you won't be able to see the log if you start the Docker container as a deamon (using the `-d` option).
    For debugging purposes,
    it is suggested that you use the `-it` options instead the `-d` option.
    A more general and robust way is of course to redirect log of applications to a file.

1. Multiple running instances of the same Docker image
    do not interact with each other.
    The are running isolated.

2. Amazon AWS is blocked in China (currently).
    Do NOT run Docker services on Amazon if your users are in the mainland of China.

## Issues & Solutions

### Issue/Error 1

> docker: Error response from daemon: Get https://registry-1.docker.io/v2/dclong/jupyterlab-rstudio/manifests/latest: dial tcp 50.17.62.194:443: getsockopt: connection refused

First retry starting the Docker container.
If it still does not work
then restart the Docker daemon using the command below will resolve the issue.

        service docker restart

## Issue/Error 2

> Jupyter notebook connection failed

Due to proxy!!! Connect without proxy works!!!

https://stackoverflow.com/questions/31280465/ipython-notebook-connection-failed-issue

## Issue/Error 3

> Docker Error: Returned a Non-zero Code: 137

This issue is due to out of memory error.
To fix it,
you can either add more RAM or add more swap memory.

https://samwize.com/2016/05/19/docker-error-returned-a-non-zero-code-137/
