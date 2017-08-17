UUID: ddef30ad-b838-4b72-b213-f2e24d170654
Status: published
Date: 2017-08-17 08:29:32
Author: Ben Chuanlong Du
Slug: docker-images-for-zeppelin
Title: Docker Images for Zeppelin
Category: Software
Tags: software, docker, Zeppelin, big data, Spark 

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Official Zeppelin Docker Image

1. Pull the official Zeppelin Docker image. 

        docker pull apache/zeppelin

2. Launch the image in a container.

        docker run -d -p 8080:8080 \
            -v $PWD/logs:/logs \
            -v $PWD/notebook:/notebook \
            -e ZEPPELIN_LOG_DIR='/logs' \
            -e ZEPPELIN_NOTEBOOK_DIR='/notebook' \
            --name zeppelin \
            apache/zeppelin:0.7.2

    If you have trouble accessing localhost:8080 in the browser, Please clear browser cache.
