UUID: ded4fb17-43c4-46e1-bafd-1d47789bedc9
Status: published
Date: 2017-03-18 19:49:54
Author: Ben Chuanlong Du
Slug: docker-image-and-container-management
Title: Docker Image and Container Management
Category: Software
Tags: software, Docker, image, container, management, remove

1. Remove all existing containers (not images).
    ```bash
    docker rm $(docker ps -aq)
    # or you can use pipe
    docker ps -aq | xargs docker rm
    ```
2. Remove exited containers.
    ```bash
    docker ps -aqf status=exited
    ```

2. Remove images without names.
    ```bash
    docker images | awk '{ if ($1 == "<none>") print $3 }' | xargs docker rmi
    ```

3. Remove images without versions.
    ```bash
    docker images | awk '{ if ($2 == "<none>") print $3 }' | xargs docker rmi
    ```

3. Remove images without names or versions.
    ```bash
    docker images | awk '{ if ($1 == "<none>" || $2 == "<none>") print $3 }' | xargs docker rmi
    ```

4. Use the `-f` (force remove image/container) option with caution.


