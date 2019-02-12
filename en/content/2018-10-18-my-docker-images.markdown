Status: published
Date: 2019-02-12 01:28:32
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

## <a name="#usage"></a> Usage in Unix/Linux

### <a name="#prerequisites"></a> Prerequisites

You must have Docker installed.
If you are on Ubuntu,
the just use the command below to install the community edition of Docker.

```Bash
sudo apt-get install docker.io
```

If you'd rather install the enterprise edition
or if you are on other platforms,
please refer to the offical Docker doc [Install Docker](https://docs.docker.com/install/).

### <a name="#pull"></a> Pull the Docker Image

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

### <a name="#run"></a> Start a Container

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

## <a name="#jupyterhub"></a> Use the JupyterHub Server

Open your browser and and visit `your_host_ip:8000`
where `your_host_ip` is the URL/ip address of your server.
You will be asked for user name (by default your user name on the host)
and password (by default your user name on the host and might want to change it for security reasons).
You can of course change your user password later
using the command `passwd` in the container.  

## <a name="#add_user"></a> Add a New User to the JupyterHub Server

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

## <a name="#images"></a> List of Images & Detailed Information

- [dclong/ubuntu_b](https://hub.docker.com/r/dclong/ubuntu_b/)  
    OS: Ubuntu 18.04  
    Time Zone: US Pacific Time  
    Desktop Environment: None  
    Remote Desktop: None  
    - [dclong/python](https://hub.docker.com/r/dclong/python/)  
        Python 3.6  
        - [dclong/jupyter](https://hub.docker.com/r/dclong/jupyter/)  
             Jupyter Notebook: 5.7.0  
            - [dclong/jupyter-nodejs](https://hub.docker.com/r/dclong/jupyter-nodejs/)  
                 NodeJS: 10.15.0  
                - [dclong/jupyterlab](https://hub.docker.com/r/dclong/jupyterlab)  
                     JupyterLab: 0.35.4  
                    - [dclong/jupyterlab-js](https://hub.docker.com/r/dclong/jupyterlab-js/)
                    - [dclong/jupyterlab-ts](https://hub.docker.com/r/dclong/jupyterlab-ts/)
                    - [dclong/jupyterlab-tdodbc](https://hub.docker.com/r/dclong/jupyterlab-tdodbc/)
                    - [dclong/jupyterlab-jdk](https://hub.docker.com/r/dclong/jupyterlab-jdk/)
                        - [dclong/jupyterlab-scala](https://hub.docker.com/r/dclong/jupyterlab-scala/)
                            - [dclong/jupyterlab-spark](https://hub.docker.com/r/dclong/jupyterlab-spark/)
                        - [dclong/jupyterlab-antlr4](https://hub.docker.com/r/dclong/jupyterlab-antlr4/)
                        - [dclong/jupyterlab-py](https://hub.docker.com/r/dclong/jupyterlab-py/)
                            - [dclong/jupyterlab-beakerx](https://hub.docker.com/r/dclong/jupyterlab-beakerx/)
                                - [dclong/jupyterlab-ds](https://hub.docker.com/r/dclong/jupyterlab-ds/)
                    - [dclong/jupyterlab-rb](https://hub.docker.com/r/dclong/jupyterlab-rb/)
                        - [dclong/jupyterlab-rp](https://hub.docker.com/r/dclong/jupyterlab-rp/)
                            - [dclong/jupyterlab-rp-py](https://hub.docker.com/r/dclong/jupyterlab-rp-py/)
                            - [dclong/jupyterlab-rstudio](https://hub.docker.com/r/dclong/jupyterlab-rstudio/)
                                - [dclong/jupyterlab-rstudio-py](https://hub.docker.com/r/dclong/jupyterlab-rstudio-py/)
                    - [dclong/jupyterhub](https://hub.docker.com/r/dclong/jupyterhub/)  
                         JupyterHub: 0.9.3  
                        - [dclong/jupyterhub-julia](https://hub.docker.com/r/dclong/jupyterhub-julia/)  
                        - [dclong/jupyterhub-jdk](https://hub.docker.com/r/dclong/jupyterhub-jdk/)  
                            OpenJDK 8  
                            Maven: 3.3.9  
                            - [dclong/jupyterhub-py](https://hub.docker.com/r/dclong/jupyterhub-py/)  
                                numpy scipy pandas dask  
                                torch torchvision tensorflow keras h2o  
                                gensim nltk  
                                scikit-learn xgboost  
                                matplotlib seaborn bokeh plotly  
                                tabulate  
                                JayDeBeApi pymysql pymongo sqlalchemy  
                                pysocks requests[socks] Scrapy beautifulsoup4 wget  ansible  
                                - [dclong/jupyterhub-ai](https://hub.docker.com/r/dclong/jupyterhub-ai/)  
                                    torch torchvision tensorflow keras h2o  
                                    gensim pytext    
                                - [dclong/jupyterhub-beaker](https://hub.docker.com/r/dclong/jupyterhub-beakerx/)  
                                    SQL (based on JDBC) via BeakerX 1.1.0  
                                    Scala 2.11.12 via BeakerX 1.1.0  
                                    Java 8, Clojure, Groovy, Kotlin via BeakerX 1.1.0  
                                    - [dclong/jupyterhub-ds](https://hub.docker.com/r/dclong/jupyterhub-ds/)  
    - [dclong/python:conda3](https://hub.docker.com/r/dclong/python/)  
        - [dclong/jupyter:conda3](https://hub.docker.com/r/dclong/jupyter/)  
            - [dclong/jupyterlab:conda3](https://hub.docker.com/r/dclong/jupyterlab)  
                - [dclong/jupyterhub:conda3](https://hub.docker.com/r/dclong/jupyterhub/)  
                    - [dclong/jupyterhub-py:conda3](https://hub.docker.com/r/dclong/jupyterhub-py/)  
                        - [dclong/holoviews:conda3](https://hub.docker.com/r/dclong/holoviews/)  
                        - [dclong/jupyterhub-ds:conda3](https://hub.docker.com/r/dclong/jupyterhub-ds/)  
    - [dclong/ubuntu_cn](https://hub.docker.com/r/dclong/ubuntu_cn/)  
        - [dclong/lubuntu](https://hub.docker.com/r/dclong/lubuntu/)  
            - [dclong/lubuntu-nodejs](https://hub.docker.com/r/dclong/lubuntu-nodejs/)  
                - [dclong/lubuntu-atom](https://hub.docker.com/r/dclong/lubuntu-atom/)  
                - [dclong/lubuntu-vscode](https://hub.docker.com/r/dclong/lubuntu-vscode/)  
            - [dclong/lubuntu-py](https://hub.docker.com/r/dclong/lubuntu-py/)  
                - [dclong/lubuntu-pycharm](https://hub.docker.com/r/dclong/lubuntu-pycharm/)  
            - [dclong/lubuntu-jdk](https://hub.docker.com/r/dclong/lubuntu-jdk/)  
                - [dclong/lubuntu-scala](https://hub.docker.com/r/dclong/lubuntu-scala/)  
                    - [dclong/lubuntu-intellij](https://hub.docker.com/r/dclong/lubuntu-intellij/)  
        - [dclong/xubuntu](https://hub.docker.com/r/dclong/xubuntu/)  
            - [dclong/xubuntu-nodejs](https://hub.docker.com/r/dclong/xubuntu-nodejs/)  
                - [dclong/xubuntu-atom](https://hub.docker.com/r/dclong/xubuntu-atom/)  
                - [dclong/xubuntu-vscode](https://hub.docker.com/r/dclong/xubuntu-vscode/)  
            - [dclong/xubuntu-py](https://hub.docker.com/r/dclong/xubuntu-py/)  
                - [dclong/xubuntu-pycharm](https://hub.docker.com/r/dclong/xubuntu-pycharm/)  
            - [dclong/xubuntu-jdk](https://hub.docker.com/r/dclong/xubuntu-jdk/)  
                - [dclong/xubuntu-scala](https://hub.docker.com/r/dclong/xubuntu-scala/)  
                    - [dclong/xubuntu-intellij](https://hub.docker.com/r/dclong/xubuntu-intellij/)  

### Tag `latest`

OS: Ubuntu 18.04  
Jupyter Notebook: 5.6.0  
NodeJS: 8.11.3  
JupyterLab: 0.35.4  
JupyterHub: 0.9.3  
OpenJDK 8  
Maven: 3.3.9  
Python 3.6.6 
Scala 2.11.12 
BeakerX 1.1.0

### Tag `18.10`

OS: Ubuntu 18.10  
Jupyter Notebook: 5.6.0  
NodeJS: 8.11.3  
JupyterLab: 0.35.4  
JupyterHub: 0.9.3  
OpenJDK 8  
Maven: 3.3.9  
Python 3.6.6 
Scala 2.11.12 
BeakerX 1.1.0

## <a name="issues"></a> Known Issues 

1. The subprocess managment issue.
    This is not an issue at in most use cases.
    This Docker image launch service using a shell script
    so there won't be orphan subprocesses
    when the process of the Docker container is get killed.
    However, launching by shell script is not the best way for managing processes.
    I might switch to the [Supervisor](https://github.com/Supervisor/supervisor) for process management
    or use the base image of [pushion/ubuntu](https://github.com/phusion/baseimage-docker) in future.
