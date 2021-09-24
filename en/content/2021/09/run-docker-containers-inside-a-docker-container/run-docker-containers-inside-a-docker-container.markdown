Status: published
Date: 2021-09-13 10:55:29
Modified: 2021-09-13 10:55:29
Author: Benjamin Du
Slug: run-docker-containers-inside-a-docker-container
Title: Run Docker Containers Inside a Docker Container
Category: Computer Science
Tags: Computer Science, programming, Docker, container, socks, container in container



You can run Docker containers inside a Docker container. 
To allow this,
you have to pass the docker socks into the container 
using the option `-v /var/run/docker.sock:/var/run/docker.sock`.
For more discussions,
please refer to
[How To Run Docker in Docker Container [3 Easy Methods]](https://devopscube.com/run-docker-in-docker/#:~:text=To%20run%20docker%20inside%20docker,sock%20as%20a%20volume.&text=Just%20a%20word%20of%20caution,privileges%20over%20your%20docker%20daemon)
.
However, 
be aware of potential security issues 
as this essentially gives root access of the host system to the Docker container.

## References

- [How To Run Docker in Docker Container [3 Easy Methods]](https://devopscube.com/run-docker-in-docker/#:~:text=To%20run%20docker%20inside%20docker,sock%20as%20a%20volume.&text=Just%20a%20word%20of%20caution,privileges%20over%20your%20docker%20daemon)