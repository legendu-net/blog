Status: published
Date: 2022-01-22 14:33:10
Modified: 2022-11-14 10:19:55
Author: Benjamin Du
Slug: expose-local-services-to-public-using-ngrok
Title: Expose Local Services to Public Using ngrok
Category: Computer Science
Tags: Computer Science, programming, local, public, HTTPS, ngrok

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

You can expose a local service to public using `ngrok`.
Follow instructions in the 
[official documentation of ngrok](https://dashboard.ngrok.com/get-started/setup)
to setup `ngrok`. 

1. Install ngrok.

        :::bash
        sudo snap install ngrok

2. Login to [https://ngrok.com](ngrok.com) 
    to identify your ngrok token.

3. Connect your account following instructions. 

        :::bash
        ngrok config add-authtoken your_token

4. Start a http tunnel forwarding to you local port.

        :::bash
        ngrok http your_choice_of_port

For example, 
suppose you have launch a code-server service
in your local network using the following command.

    :::bash
    docker run -d --init \
        --hostname vscode-server \
        --log-opt max-size=50m \
        --memory=$(($(head -n 1 /proc/meminfo | awk '{print $2}') * 4 / 5))k \
        --cpus=$(($(nproc) - 1)) \
        -p 2020:8080 \
        -e DOCKER_USER=$(id -un) \
        -e DOCKER_USER_ID=$(id -u) \
        -e DOCKER_PASSWORD=$(id -un) \
        -e DOCKER_GROUP_ID=$(id -g) \
        -v "$(pwd)":/workdir \
        dclong/vscode-server /scripts/sys/init.sh

You can expose it to public via ngrok by running the following command.

    :::bash
    ngrok http 2020

## References

- [Official Documentation of ngrok](https://dashboard.ngrok.com/get-started/setup)
