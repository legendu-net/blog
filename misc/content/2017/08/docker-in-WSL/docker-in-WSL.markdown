Status: published
Date: 2017-08-10 09:05:45
Author: Ben Chuanlong Du
Slug: docker-in-WSL2
Title: Docker in WSL 2
Category: Software
Tags: software, Docker, WSL, WSL 2, Windows, Bash, BashOnWindows, Bash on Windows
Modified: 2021-08-15 16:52:00

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**
## Tips and Traps

1. Docker in WSL 2 works great.

## Install Docker in WSL 2 

1. Install WSL 2 following instructions in 
    [Tips on WSL 2](http://www.legendu.net/misc/blog/wsl-tips/)
    .

2. Install `docker.io` in WSL 2. 

        :::bash
        sudo apt-get install docker.io

2. Install Docker desktop for Windows.

3. Set Docker to use WSL 2 based engine. 

    1. Open Docker desktop settings.
    2. Check the checkbox "Use the WSL 2 based engine" in the general tab.
    3. Click "Apply & Restart".

    ![docker-wsl2-engine](https://docs.docker.com/docker-for-windows/images/wsl2-enable.png)

For more details,
please refer to
[Docker Desktop WSL 2 backend](https://docs.docker.com/docker-for-windows/wsl/)
.

## Related Articles 

[Running Docker containers on Bash on Windows](https://blog.jayway.com/2017/04/19/running-docker-on-bash-on-windows/)

## References

- [Tips on WSL 2](http://www.legendu.net/misc/blog/wsl-tips/)

- https://towardsdatascience.com/dual-boot-is-dead-windows-and-linux-are-now-one-27555902a128
