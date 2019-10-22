UUID: 09253576-35e1-470f-8fd2-03dc2d659e47
Status: published
Date: 2019-10-22 00:36:20
Author: Ben Chuanlong Du
Slug: docker-on-mac
Title: Docker on Mac
Category: Software
Tags: Software, Docker, Mac

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


It is suggested that you install the offical docker app on Mac
instead of installing docker using MacPorts/Homebrew.
Docker installed using MacPorts/Homebrew might have issues to start. 

https://docs.docker.com/docker-for-mac/

https://docs.docker.com/compose/completion/

By default, Docker Desktop for Mac is set to use 2GB runtime memory, 
allocated from the total available memory on your Mac.
This might not be enough in some situations (e.g., when you run BeakerX).
You'd make set it to be a larger value.


Default file location for user settings is
`~/Library/Containers/com.docker.docker/Data/database/com.docker.driver.amd64-linux/etc/docker/daemon.json`
However,
you shouldn't edit it directly. 
Instead, 
You should go to the whale icon in the taskbar > Preferences > Daemon > Advanced.


## Advanced Settings

CPUs: By default, 
Docker Desktop for Mac is set to use half the number of processors available on the host machine. 
To increase processing power, set this to a higher number; to decrease, lower the number.

Memory: By default, 
Docker Desktop for Mac is set to use 2 GB runtime memory, 
allocated from the total available memory on your Mac. 
To increase RAM, set this to a higher number; to decrease it, lower the number.

Swap: Configure swap file size as needed. The default is 1 GB.
