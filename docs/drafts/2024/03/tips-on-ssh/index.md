---
title: Tips on SSH
created: '2024-03-12T16:36:40-07:00'
date: '2026-06-07T16:36:36-07:00'
authors:
  - bendu
label: tips-on-ssh
license: CC-BY-4.0
tags:
  - computer science
  - SSH
  - agent
  - config
  - ssh-keygen
  - key
  - generation
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## ssh-keygen

Run the command `ssh-keygen` to interactively generate a new pair of public/private keys.
It is strongly suggested that you protect your private keys with a passphrase.
With the increasing using of AI agent/skills,
the risk of leaking keys/tokens is much higher compared to before.

## SSH agent

Follow the steps below to setup the ssh agent
if you protect your SSH private keys with a passphrase.

1. Upload your SSH public key to servers (e.g., GitHub)
   that you need to access via SSH.

1. Run the following command to terminate previously created and persisted SSH tunnels (if any).

```sh
ssh -O exit git@github.com
```

2. Run the following command (for fish).

```sh
eval (ssh-agent -c)
```

It's the best to add the following script into your config.fish.

```sh
if not set -q SSH_AUTH_SOCK
eval (ssh-agent -c) > /dev/null
end
```

3. Load the SSH private key you need into SSH agent.

```sh
ssh-add ~/.ssh/id_ed25519
```

## Tips for SSH Config

1. You can
   [configure SSH to auto add keys to SSH agent](https://github.com/legendu-net/icon-data/blob/main/ssh/client/config#L21)
   .

1. [Persist SSH connections](https://github.com/legendu-net/icon-data/blob/main/ssh/client/config#L22)
   helps.
