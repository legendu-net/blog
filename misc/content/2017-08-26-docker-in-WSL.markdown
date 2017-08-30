UUID: 045df550-e675-4a90-a9f2-0081631b165d
Status: published
Date: 2017-08-26 20:47:08
Author: Ben Chuanlong Du
Slug: docker-in-WSL
Title: Docker in Wsl
Category: Software
Tags: software, Docker, WSL, Windows, Bash, BashOnWindows, Bash on Windows

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. Docker can be installed in WSL starting from the Win 10 Creator update,
however, 
there are still all kinds of issues running Docker in WSL.


## Use Docker on Windows in WSL

1. Install Docker on Windows

To install the Docker engine on Windows, just go to docker.com and download the appropriate distribution. Also, make sure hardware virtualization is enabled and Hyper-V is installed, lest the engine won’t start.
Shortcut: Install Windows 10 Creators Update

With Windows 10 Creators Update*, accomplishing all of this has become a lot simpler, since it allows you to run Windows executables from Bash. Just add these two lines to your .bashrc and you’re done!
PATH="$HOME/bin:$HOME/.local/bin:$PATH" PATH="$PATH:/mnt/c/Program\ Files/Docker/Docker/resources/bin"
1
2
    
    PATH="$HOME/bin:$HOME/.local/bin:$PATH"
    PATH="$PATH:/mnt/c/Program\ Files/Docker/Docker/resources/bin"

    You can now run docker --version from Bash, and you don’t even have to read the rest of this blog post :)

    *) Windows 10 Creators Update is available to Insiders since April 11, 2017, and will be released to the public on April 25, 2017.

## Related Articles 

[Running Docker containers on Bash on Windows](https://blog.jayway.com/2017/04/19/running-docker-on-bash-on-windows/)

