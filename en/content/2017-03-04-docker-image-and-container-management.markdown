UUID: ded4fb17-43c4-46e1-bafd-1d47789bedc9
Status: published
Date: 2017-10-22 12:21:19
Author: Ben Chuanlong Du
Slug: docker-image-and-container-management
Title: Manage Docker Images and Containers 
Category: Software
Tags: software, Docker, image, container, management, remove

## Remove Containers

Note that running containers will NOT be removed by default.
This is what users want generally speaking. 
You can use the option `-f` to force removing running containers,
but use it with caution and at your own risk.

1. Remove all existing containers (not images).

        docker rm $(docker ps -aq)
        # or you can use pipe
        docker ps -aq | xargs docker rm

2. Remove exited containers.

        docker ps -aqf status=exited


## Remove Images

Note that images required by running containers will NOT be removed by default.
This is what users want generally speaking. 
You can use the option `-f` to force removing images,
but use it with caution and at your own risk.

1. Remove images without names (with the help of `awk`).

        docker images | awk '{ if ($1 == "<none>") print $3 }' | xargs docker rmi


2. Remove images without versions (with the help of `awk`).

        docker images | awk '{ if ($2 == "<none>") print $3 }' | xargs docker rmi


3. Remove images without names or versions (with the help of `awk`).

        docker images | awk '{ if ($1 == "<none>" || $2 == "<none>") print $3 }' | xargs docker rmi

4. Remove all images belong to the eclipse organization with the help of `sed` and `q`. 

        docker images sed 's/ \+/\t/g' q -tH "select [image id] from - where repository like 'eclipse/%'" xargs docker rmi 

## Get Container ID Inside Container

You can get the container ID inside the docker container 
by running the following command.

    cat /proc/self/cgroup | grep -o  -e "docker-.*.scope" | head -n 1 | sed "s/docker-\(.*\).scope/\\1/"

Or another simpler way is to run

    echo $HOSTNAME

But it will not work in the following two cases. 

1. if hostname is explicitly specified with `--hostname` flag. 

2. when using `--net=host` mode.


## Import/Export Docker Container/Images

[Moving Docker Containers and Images Around](https://blog.giantswarm.io/moving-docker-container-images-around/)

1. Save a docker image to a tar.gz file.

        docker save image | gzip > image.tar.gz


2. Load a docker image from tar file.

        docker load < image.tar


## Kill a Process in a Container

```sh
docker exec container_name kill process_name
```
## List Mounted Volumes 

<https://stackoverflow.com/questions/30642844/how-to-list-docker-mounted-volumes-from-within-the-container>
