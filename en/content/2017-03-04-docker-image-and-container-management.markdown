UUID: ded4fb17-43c4-46e1-bafd-1d47789bedc9
Status: published
Date: 2017-06-11 19:26:27
Author: Ben Chuanlong Du
Slug: docker-image-and-container-management
Title: Docker Image and Container Management
Category: Software
Tags: software, Docker, image, container, management, remove

1. Remove all existing containers (not images).

        docker rm $(docker ps -aq)
        # or you can use pipe
        docker ps -aq | xargs docker rm

2. Remove exited containers.

        docker ps -aqf status=exited


2. Remove images without names.

        docker images | awk '{ if ($1 == "<none>") print $3 }' | xargs docker rmi


3. Remove images without versions.

        docker images | awk '{ if ($2 == "<none>") print $3 }' | xargs docker rmi


3. Remove images without names or versions.

        docker images | awk '{ if ($1 == "<none>" || $2 == "<none>") print $3 }' | xargs docker rmi


4. Use the `-f` (force remove image/container) option with caution.

5. Get the container ID inside the docker container. 

    cat /proc/self/cgroup | grep -o  -e "docker-.*.scope" | head -n 1 | sed "s/docker-\(.*\).scope/\\1/"

    Or you can use the following command.
    Though, this way will not work in two cases. 
        1. if hostname is explicitly specified with --hostname flag. 
        2. when using --net=host mode.

        echo $HOSTNAME
