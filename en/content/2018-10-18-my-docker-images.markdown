Status: published
Date: 2019-03-22 01:54:54
Author: Ben Chuanlong Du
Slug: my-docker-images
Title: My Docker Images
Category: Software
Tags: software, Docker, Docker image, Ubuntu, JupyterLab, Lubuntu, dclong

## Tips

1. The `dclong/jupyterlab` Docker image is well maintained (which is the base image of `dclong/jupyterhub`), 
    however many of the `dclong/jupyterlab-*` Docker images are not maintained any more.
    Please use the corresponding `dclong/jupyterhub-*`  Docker images instead.

2. There is an issue with the `dclong/xubuntu*` Docker images due to Xfce on Ubuntu 18.04.
    It is suggested that you use the corresponding `dclong/lubuntu*` Docker images instead,
    which are based on LXQt.

## Usage

### Install Docker

You must have Docker installed.
If you are on Ubuntu,
the just use the command below to install the community edition of Docker.

```Bash
sudo apt-get install docker.io
```

If you'd rather install the enterprise edition
or if you are on other platforms,
please refer to the offical Docker doc [Install Docker](https://docs.docker.com/install/).

### Pull the Docker Image

Taking `dclong/jupyterhub-ds` as an example,
you can pull it using the command below.

```Bash
docker pull dclong/jupyterhub-ds
```

For people in mainland of China,
please refer to the post
[Speedup Docker Pulling and Pushing](http://www.legendu.net/en/blog/speedup-docker-pulling-and-pushing/)
on ways to speed up pushing/pulling of Docker images.
If you don't bother,
then just use the command below.

```Bash
docker pull registry.docker-cn.com/dclong/jupyterhub-ds
```

### Start a Container

Below are some Docker command arguments explained.
These are for properly handling file permissions in the Docker container and on the host.
Keep the default if you don't know what are the best to use.
`DOCKER_PASSWORD` is probably the only argument you want to and should change.

- `DOCKER_USER`: The user to be created (dynamically) in the container.
    By default, the name of the current user on the host is used.
- `DOCKER_USER_ID`: The ID of the user to be created in the container.
    By default, the ID of the current user on the host is used.
- `DOCKER_PASSWORD`: The password of the user to be created.
    By default, it's the same as the user name.
    You'd better change it for security reasons.
    Of course, users can always change it later using the command `passwd`.
- `DOCKER_GROUP_ID`: The group of the user to be created.
    By default, it's the group ID of the current user on the host.
- `DOCKER_ADMIN_USER` (`dclong/jupyterhub-*` only): The admin of the JupyterLab server.
    By default, it's the user to be created in the container.
- `USER_MEM_LIMIT` (`dclong/jupyterhub-*` only): The memory limit that each user can use.
    Note that this optional is not in effect now.

The root directory of JupyterLab/Jupyter notebooks is `/workdir` in the container.
You can mount directory on the host to it as you wish.
Below are illustration using the Docker image `dclong/jupyterhub-ds`.

The following command starts a container 
and mounts the current working directory and `/home` on the host machine 
to `/workdir` and `/home_host` in the container respectively.

```
docker run -d \
    --name jupyterhub-ds \
    --log-opt max-size=50m \
    -p 8000:8000 \
    -p 5006:5006 \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_PASSWORD=`id -un` \
    -e DOCKER_GROUP_ID=`id -g` \
    -e DOCKER_ADMIN_USER=`id -un` \
    -v `pwd`:/workdir \
    -v `dirname $HOME`:/home_host \
    dclong/jupyterhub-ds
```

The following command (only works on Linux) does the same as the above one 
except that it limits the use of CPU and memory.

```
docker run -d \
    --name jupyterhub-ds \
    --log-opt max-size=50m \
    --memory=$(($(head -n 1 /proc/meminfo | awk '{print $2}') * 4 / 5))k \
    --cpus=$((`nproc` - 1)) \
    -p 8000:8000 \
    -p 5006:5006 \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_PASSWORD=`id -un` \
    -e DOCKER_GROUP_ID=`id -g` \
    -e DOCKER_ADMIN_USER=`id -un` \
    -v `pwd`:/workdir \
    -v `dirname $HOME`:/home_host \
    dclong/jupyterhub-ds
```

## Use the JupyterHub Server

Open your browser and and visit `your_host_ip:8000`
where `your_host_ip` is the URL/ip address of your server.
You will be asked for user name (by default your user name on the host)
and password (by default your user name on the host and might want to change it for security reasons).
You can of course change your user password later
using the command `passwd` in the container.  

## Add a New User to the JupyterHub Server

By default,
any user in the Docker container can visit the JupyterHub server.
So if you want to grant access to a new user,
just create an account for him in the Docker container.
You can of course use the well know commands `useradd`, `adduser`, etc. to achive it.
To make things easier for you,
there are some shell scripts in the directory `/scripts/` to create usres for you.

- `/scripts/create_user.sh`: Create a new user. It's the base script for creating users.
- `/scripts/create_user_group.sh`: Create a new user with the given (existing) group.
- `/scripts/create_user_nogroup.sh`: Create a new user with group name `nogroup`.
- `/scripts/create_user_docker.sh`: Create a new user with group name `docker`.

You can use the option `-h` to print help doc for these commands.
For example, `/scripts/create_user_nogroup.sh -h` prints the below help doc.

```Bash
Create a new user with the group name "nogroup".
Syntax: create_user_nogroup user user_id [password]
Arguments:
user: user name
user_id: user id
password: Optional password of the user. If not provided, then the user name is used as the password.
```

Now suppose you want to create a new user `dclong` with user ID `2000` and group name `nogroup`,
you can use the following command.

```Bash
sudo /scripts/create_user_nogroup.sh dclong 2000
```

Since we didn't specify a password for the user,
the default password (same as the user name) is used.


## Remote Connect to Desktop in the Container

Download the NoMachine client from <https://www.nomachine.com/download>, 
install the client, 
create a new connection to your public ip, port 4000, NX protocol, 
use a user on the host OS and the corresponding password for authentication. 

## List of Images and Detailed Information

- [dclong/gitpod](https://hub.docker.com/r/dclong/gitpod/)

- [dclong/deepin_b](https://hub.docker.com/r/dclong/deepin_b/)  

    - [dclong/deepin_cn](https://hub.docker.com/r/dclong/deepin_cn/)  

        - [dclong/deepin](https://hub.docker.com/r/dclong/deepin/)  

- [dclong/ubuntu_b](https://hub.docker.com/r/dclong/ubuntu_b/)  

    > OS: Ubuntu 18.04  
    > Time Zone: US Pacific Time  
    > Desktop Environment: None  
    > Remote Desktop: None  

    - [dclong/proxychains](https://hub.docker.com/r/dclong/proxychains/)  

    - [dclong/linuxbrew](https://hub.docker.com/r/dclong/linuxbrew/)  

    - [dclong/blog](https://hub.docker.com/r/dclong/blog/)  

    - [dclong/samba](https://hub.docker.com/r/dclong/samba/)  

    - [dclong/pdftk](https://hub.docker.com/r/dclong/pdftk/)  

    - [dclong/nfs](https://hub.docker.com/r/dclong/nfs/)  

    - [dclong/nodejs](https://hub.docker.com/r/dclong/nodejs/)  

        - [dclong/typescript](https://hub.docker.com/r/dclong/typescript/)  

    - [dclong/jdk](https://hub.docker.com/r/dclong/jdk/)  

        - [dclong/scala](https://hub.docker.com/r/dclong/scala/)  

            - [dclong/hadoop](https://hub.docker.com/r/dclong/hadoop/)  

              - [dclong/hive](https://hub.docker.com/r/dclong/hive/)  

                  - [dclong/spark](https://hub.docker.com/r/dclong/spark/)  

                  - [dclong/zeppelin](https://hub.docker.com/r/dclong/zeppelin/)  

        - [dclong/h2o](https://hub.docker.com/r/dclong/h2o/)  

    - [dclong/r-base](https://hub.docker.com/r/dclong/r-base/)  

        - [dclong/r-pop](https://hub.docker.com/r/dclong/r-pop/)  

            - [dclong/rstudio](https://hub.docker.com/r/dclong/rstudio/)  

    - [dclong/qt5](https://hub.docker.com/r/dclong/qt5/)  

    - [dclong/conda](https://hub.docker.com/r/dclong/conda/)  

        - [dclong/conda-build](https://hub.docker.com/r/dclong/conda-build/)  

        - [dclong/conda-yarn](https://hub.docker.com/r/dclong/conda-yarn/)  

    - [dclong/tdodbc](https://hub.docker.com/r/dclong/tdodbc/)  

        - [dclong/tdodbc-py](https://hub.docker.com/r/dclong/tdodbc-py/)  

    - [dclong/python](https://hub.docker.com/r/dclong/python/)  

        > Python 3.6  

        - [dclong/theia](https://hub.docker.com/r/dclong/theia/)  

        - [dclong/wdb](https://hub.docker.com/r/dclong/wdb/)  

        - [dclong/python-jdk](https://hub.docker.com/r/dclong/python-jdk/)  

        - [dclong/python-nodejs](https://hub.docker.com/r/dclong/python-nodejs/)  

        - [dclong/mlflow](https://hub.docker.com/r/dclong/mlflow/)  

        - [dclong/flask](https://hub.docker.com/r/dclong/flask/)  

        - [dclong/dryscrape](https://hub.docker.com/r/dclong/dryscrape/)  

        - [dclong/jupyter](https://hub.docker.com/r/dclong/jupyter/)  

             > Jupyter Notebook: 5.7.0  

            - [dclong/jupyter-nodejs](https://hub.docker.com/r/dclong/jupyter-nodejs/)  

                 > NodeJS: 10.15.0  

                - [dclong/jupyterlab](https://hub.docker.com/r/dclong/jupyterlab)  

                     > JupyterLab: 0.35.4  

                    - [dclong/jupyterhub](https://hub.docker.com/r/dclong/jupyterhub/)  

                         > JupyterHub: 0.9.3  

                        - [dclong/jupyterhub-ts](https://hub.docker.com/r/dclong/jupyterhub-ts/)  

                        - [dclong/jupyterhub-julia](https://hub.docker.com/r/dclong/jupyterhub-julia/)  

                        - [dclong/jupyterhub-jdk](https://hub.docker.com/r/dclong/jupyterhub-jdk/)  

                            > OpenJDK 8  
                            > Maven: 3.3.9  

                            - [dclong/jupyterhub-py](https://hub.docker.com/r/dclong/jupyterhub-py/)  

                                > numpy scipy pandas dask  
                                > torch torchvision tensorflow keras h2o  
                                > gensim nltk  
                                > scikit-learn xgboost  
                                > matplotlib seaborn bokeh plotly  
                                > tabulate  
                                > JayDeBeApi pymysql pymongo sqlalchemy  
                                > pysocks requests[socks] Scrapy beautifulsoup4 wget  ansible  

                                - [dclong/holoviews](https://hub.docker.com/r/dclong/holoviews/)  

                                - [dclong/jupyterhub-ai](https://hub.docker.com/r/dclong/jupyterhub-ai/)  

                                    > torch torchvision tensorflow keras h2o  
                                    > gensim pytext    

                                - [dclong/jupyterhub-beaker](https://hub.docker.com/r/dclong/jupyterhub-beakerx/)  

                                    > SQL (based on JDBC) via BeakerX 1.1.0  
                                    > Scala 2.11.12 via BeakerX 1.1.0  
                                    > Java 8, Clojure, Groovy, Kotlin via BeakerX 1.1.0  

                                    - [dclong/jupyterhub-ds](https://hub.docker.com/r/dclong/jupyterhub-ds/)  

    - [dclong/ubuntu_cn](https://hub.docker.com/r/dclong/ubuntu_cn/)  

        - [dclong/lubuntu](https://hub.docker.com/r/dclong/lubuntu/)  

            - [dclong/lubuntu-nodejs](https://hub.docker.com/r/dclong/lubuntu-nodejs/)  

                - [dclong/lubuntu-vscode](https://hub.docker.com/r/dclong/lubuntu-vscode/)  

            - [dclong/lubuntu-py](https://hub.docker.com/r/dclong/lubuntu-py/)  

                - [dclong/lubuntu-pycharm](https://hub.docker.com/r/dclong/lubuntu-pycharm/)  

            - [dclong/lubuntu-jdk](https://hub.docker.com/r/dclong/lubuntu-jdk/)  

                - [dclong/lubuntu-scala](https://hub.docker.com/r/dclong/lubuntu-scala/)  
                    - [dclong/lubuntu-intellij](https://hub.docker.com/r/dclong/lubuntu-intellij/)  

        - [dclong/xubuntu](https://hub.docker.com/r/dclong/xubuntu/)  
            - [dclong/xubuntu-nodejs](https://hub.docker.com/r/dclong/xubuntu-nodejs/)  
                - [dclong/xubuntu-vscode](https://hub.docker.com/r/dclong/xubuntu-vscode/)  
            - [dclong/xubuntu-py](https://hub.docker.com/r/dclong/xubuntu-py/)  
                - [dclong/xubuntu-pycharm](https://hub.docker.com/r/dclong/xubuntu-pycharm/)  
            - [dclong/xubuntu-jdk](https://hub.docker.com/r/dclong/xubuntu-jdk/)  
                - [dclong/xubuntu-scala](https://hub.docker.com/r/dclong/xubuntu-scala/)  
                    - [dclong/xubuntu-intellij](https://hub.docker.com/r/dclong/xubuntu-intellij/)  

## Known Issues 

1. The subprocess managment issue.
    This is not an issue at in most use cases.
    This Docker image launch service using a shell script
    so there won't be orphan subprocesses
    when the process of the Docker container is get killed.
    However, launching by shell script is not the best way for managing processes.
    I might switch to the [Supervisor](https://github.com/Supervisor/supervisor) for process management
    or use the base image of [pushion/ubuntu](https://github.com/phusion/baseimage-docker) in future.
