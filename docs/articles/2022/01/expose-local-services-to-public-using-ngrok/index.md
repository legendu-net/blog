---
title: Expose Local Services to Public Using ngrok
created: '2022-01-22T14:33:10-08:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: expose-local-services-to-public-using-ngrok
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - local
  - public
  - HTTPS
  - ngrok
---

You can expose a local service to public using `ngrok`.
Follow instructions in the
[official documentation of ngrok](https://dashboard.ngrok.com/get-started/setup)
to setup `ngrok`.

1. Install ngrok.

   ```bash
   sudo snap install ngrok
   ```

1. Login to [ngrok.com](https://ngrok.com)
   to identify your ngrok token.

1. Connect your account following instructions.

   ```bash
   ngrok config add-authtoken your_token
   ```

1. Start a http tunnel forwarding to you local port.

   ```bash
   ngrok http your_choice_of_port
   ```

For example,
suppose you have launch a code-server service
in your local network using the following command.

```bash
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
```

You can expose it to public via ngrok by running the following command.

```bash
ngrok http 2020
```

## References

- [Official Documentation of ngrok](https://dashboard.ngrok.com/get-started/setup)
