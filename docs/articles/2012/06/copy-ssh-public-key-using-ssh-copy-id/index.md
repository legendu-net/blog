---
title: Copy SSH Public Key Using ssh-copy-id
created: '2012-06-29T22:25:13-07:00'
date: '2026-11-15T09:16:39-08:00'
authors:
  - bendu
label: copy-ssh-public-key-using-ssh-copy-id
license: CC-BY-4.0
tags:
  - Linux
  - SSH
  - server
  - remote
  - port
  - ssh-copy-id
---

You can use the following command to copy your SSH public key to a Linux server.

```
:::bash
ssh-copy-id -i ~/.ssh/id_rsa.pub host_machine
```

However,
if a Linux server runs the SSH daemon on a non default port (default is 22),
you have to specify the port with option `-p port`.
In addition,
the host machine and the port options must be in quotes
(either single or double quotes),
otherwise,
you will get an error message.
Suppose sshd runs on port 323 on `host_machine`,
the following command copies the ssh public key to it.

```
:::bash
ssh-copy-id -i ~/.ssh/id_rsa.pub "host_machine -p 323"
```

You can of course SSH into the server
and add your SSH public key(s) into the `~/.ssh/authorized_keys` file manually.
