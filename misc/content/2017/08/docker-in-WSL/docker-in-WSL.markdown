Status: published
Date: 2017-08-10 09:05:45
Author: Ben Chuanlong Du
Slug: docker-in-WSL2
Title: Docker in WSL 2
Category: Software
Tags: software, Docker, WSL, WSL 2, Windows, Bash, BashOnWindows, Bash on Windows
Modified: 2021-08-20 05:14:02

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**
## Tips and Traps

1. Docker on WSL 2 works great.
    However,
    the performance of IO is extremely bad if it involves the Windows filesystem 
    (and this is also true for IO in WSL 2 as Docker on WSL 2 share the same kernel as WSL 2)
    .
    It is suggested that you work with the WSL 2 filesystem (instead of the Windows filesystem)
    if IO performance is critical to your use case. 
    For more details,
    please refer to
    [How to Boost Docker with WSL2](https://towardsdatascience.com/how-to-improve-docker-performance-with-wsl2-3a54402ab0f2)
    .

2. Docker containers launched from a WSL (e.g., Ubuntu) shell will continue to run 
    after the WSL shell is terminated,
    as long as the Docker daemon is alive. 
    As a matter of fact,
    a WSL 2 shell is not must to start the Docker daemon (back by WSL 2) or to launch Docker containers.

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

- [How to Boost Docker with WSL2](https://towardsdatascience.com/how-to-improve-docker-performance-with-wsl2-3a54402ab0f2)

- https://towardsdatascience.com/dual-boot-is-dead-windows-and-linux-are-now-one-27555902a128
