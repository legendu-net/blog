Status: published
Date: 2019-11-20 17:01:14
Author: Ben Chuanlong Du
Slug: my-docker-images
Title: My Docker Images
Category: Software
Tags: software, Docker, Docker image, Ubuntu, JupyterLab, Lubuntu, dclong

## Tips

1. The `dclong/jupyterlab` Docker image is well maintained (which is the base image of `dclong/jupyterhub`), 
    however, 
    many of the `dclong/jupyterlab-*` Docker images are not maintained any more.
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


## Get Information of Running Jupyter/Lab Servers

If you are using the Jupyter/Lab server (instead of JupyterHub which is recommended),
you will be asked for a token at login.
If you have started the Docker container in interactive mode (option `-i` instead of `-d`),
the token for login is printed to the console.
Otherwise,
the tokens (and more information about the servers) can be found 
by running the following command outside the Docker container.
```bash
docker exec jupyterlab /scripts/list_jupyter.py
```
The above command tries to be smart in the sense that 
it first figures out the user that started the JupyterLab server 
and then query running Jupyter/Lab servers of that user.
An equivalently but more specifically command 
(if the Docker is launched by the current user in the host)
is as below
```bash
docker exec -u $(id -un) jupyterlab /scripts/sys/list_jupyter.py
```
If you are inside the Docker container, 
then run the following command to get the tokens (and more information about the servers).
```bash
/scripts/list_jupyter.py
```
Or equivalently if the Jupyter/Lab server is launched by the current user,
```bash
/scripts/sys/list_jupyter.py
```

To sum up, 
most of time you can rely on `/scripts/list_jupyter.py`
to find the tokens of the running Jupyter/Lab servers,
no matter you are root or the user that launches the Docker/JupyterLab server,
and no matter you are inside the Docker container or not.


## Use the JupyterHub Server

1. Open your browser and and visit `your_host_ip:8000`
  where `your_host_ip` is the URL/ip address of your server.

2. Login to the JupyterHub server 
  using your user name (by default your user name on the host machine)
  and password (by default your user name on the host machine). 

3. It is strongly suggested (for security reasons) that you change your password (using the command `passwd`)
  in the container.

4. Enjoy JupyterLab notebook!

## Add a New User to the JupyterHub Server

By default,
any user in the Docker container can visit the JupyterHub server.
So if you want to grant access to a new user,
just create an account for him in the Docker container.
You can of course use the well know commands `useradd`, `adduser`, etc. to achive it.
To make things easier for you,
there are some shell scripts in the directory `/scripts/` to create usres for you.

- `/scripts/sys/create_user.sh`: Create a new user. It's the base script for creating users.
- `/scripts/sys/create_user_group.sh`: Create a new user with the given (existing) group.
- `/scripts/sys/create_user_nogroup.sh`: Create a new user with group name `nogroup`.
- `/scripts/sys/create_user_docker.sh`: Create a new user with group name `docker`.

You can use the option `-h` to print help doc for these commands.
For example, `/scripts/sys/create_user_nogroup.sh -h` prints the below help doc.

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
sudo /scripts/sys/create_user_nogroup.sh dclong 2000
```

Since we didn't specify a password for the user,
the default password (same as the user name) is used.


## Remote Connection to Desktop in the Container

If you are running a Docker container with a desktop environment (`dclong/lubuntu*` or `dclong/xubuntu*`),
you can connect to the desktop environment in the Docker container using NoMachine.

  1. Download the NoMachine client from <https://www.nomachine.com/download>.
  2. Install the NoMachine client on your computer.
  3. Create a new connection from your computer 
    to the desktop environment in the Docker image using the NX protocol and port 4000.
    You will be asked for a user name and password.
    By default,
    the user name used to start the Docker container on the host machine 
    is used as both the user name and password in the Docker container.

## Use Spark in JupyterLab Notebook

### Spark - The BeakerX Scala Kernel

Currently [dclong/jupyterhub-ds](https://hub.docker.com/r/dclong/jupyterhub-ds/) uses the BeakerX Scala kernel.

1. Open a JupyterLab notebook with the BeakerX Scala kernel from the launcher.

2. Download Spark (say, 2.3.1) dependencies. 
```
%%classpath add mvn
org.apache.spark spark-core_2.11 2.3.1
org.apache.spark spark-sql_2.11 2.3.1
```

3. Create a SparkSession object.
```
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

val spark = SparkSession.builder()
    .master("local[2]")
    .appName("Spark Example")
    .config("spark.some.config.option", "some-value")
    .getOrCreate()

import spark.implicits._
```

4. Use Spark as usual. 
```
val df = Range(0, 10).toDF
df.show
```

### Spark - The Almond Scala Kernel

Currently [dclong/jupyterhub-almond](https://hub.docker.com/r/dclong/jupyterhub-almond/) uses the Almond Scala kernel.

1. Open a JupyterLab notebook with the Almond Scala kernel from the launcher.

2. Download Spark (say, 2.3.1) dependencies. 
```
interp.load.ivy("org.apache.spark" % "spark-core_2.11" % "2.3.1")
```

3. Create a SparkSession object.
```
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

val spark = SparkSession.builder()
    .master("local[2]")
    .appName("Spark Example")
    .config("spark.some.config.option", "some-value")
    .getOrCreate()

import spark.implicits._
```

4. Use Spark as usual. 
```
val df = Range(0, 10).toDF
df.show
```

Please refer to 
[almond-sh/examples](https://github.com/almond-sh/examples/blob/master/notebooks/spark.ipynb)
for more details.

### Spark - Apache Toree

Currently [dclong/jupyterhub-toree](https://hub.docker.com/r/dclong/jupyterhub-toree/) uses the Apache Toree Scala kernel.

The Docker image 
[dclong/jupyterhub-toree](https://github.com/dclong/docker-jupyterhub-toree)
has Spark and Apache Toree installed and configured.
Since Spark is already installed in it, 
you don't need to download and install Spark by yourself.
By default, 
a Spark Session object named `spark` is created automatically just like spark-shell.
So, you can use Spark/Scala out-of-box in a JupyterLab notebook with the `Scala - Apache Toree` kernel.

1. Open a JupyterLab notebook with the `Scala - Apache Toree` kernel from the launcher.

2. Use Spark as usual.
```
val df = Range(0, 10).toDF
df.show
```

### PySpark - pyspark and findspark

The Docker image
[dclong/jupyterhub-toree](https://github.com/dclong/docker-jupyterhub-toree)
has Spark (2.4.3) and the Python packages `pyspark` and `findspark` installed and configured.
For convenience, 
a symbolic link of the Spark home directory (`/opt/spark-2.4.3-bin-hadoop2.7`) is made to `/opt/spark`.

1. Open a JupyterLab notebook with the `Scala - Apache Toree` kernel from the launcher.

2. Find and initialize PySpark.

```
import findspark
# A symbolic link of the Spark Home is made to /opt/spark for convenience
findspark.init('/opt/spark')

import pyspark
sc = pyspark.SparkContext(appName="myAppName")
```
3. Use Spark as usual.
```
sc.textFile
```

## List of Images and Detailed Information

- [dclong/gitpod-svim](https://hub.docker.com/r/dclong/gitpod-svim/)

    - [dclong/gitpod-py3](https://hub.docker.com/r/dclong/gitpod-py3/)

- [dclong/deepin_b](https://hub.docker.com/r/dclong/deepin_b/)  

    - [dclong/deepin_cn](https://hub.docker.com/r/dclong/deepin_cn/)  

        - [dclong/deepin](https://hub.docker.com/r/dclong/deepin/)  

- [dclong/ubuntu_b](https://hub.docker.com/r/dclong/ubuntu_b/)  

    > OS: Ubuntu 18.04  
    > Time Zone: US Pacific Time  
    > Desktop Environment: None  
    > Remote Desktop: None  

    - [dclong/linuxbrew](https://hub.docker.com/r/dclong/linuxbrew/)  

    - [dclong/samba](https://hub.docker.com/r/dclong/samba/)  

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

                                - [dclong/jupyterhub-beakerx](https://hub.docker.com/r/dclong/jupyterhub-beakerx/)  

                                    > SQL (based on JDBC) via BeakerX 1.1.0  
                                    > Scala 2.11.12 via BeakerX 1.1.0  
                                    > Java 8, Clojure, Groovy, Kotlin via BeakerX 1.1.0  

                                    - [dclong/jupyterhub-ds](https://hub.docker.com/r/dclong/jupyterhub-ds/)  

    - [dclong/ubuntu_cn](https://hub.docker.com/r/dclong/ubuntu_cn/)  

        - [dclong/lubuntu](https://hub.docker.com/r/dclong/lubuntu/)  

            - [dclong/lubuntu-qt5](https://hub.docker.com/r/dclong/lubuntu-qt5/)  

                - [dclong/lubuntu-pyside2](https://hub.docker.com/r/dclong/lubuntu-pyside2/)  

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
    This is not an issue at all in most use cases.
    This Docker image launch service using a shell script
    so there won't be orphan subprocesses
    when the process of the Docker container is killed.
    However, launching by shell script is not the best way for managing processes.
    Please refer to [A Simple Init System](https://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-problem/#asimpleinitsystem)
    for more details.
    I might switch to the [Supervisor](https://github.com/Supervisor/supervisor) for process management
    or use the base image of [pushion/baseimage](https://hub.docker.com/r/phusion/baseimage/) in future.
