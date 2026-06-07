---
title: Manage Password Using gopass
created: '2026-05-25T19:31:05.793047-07:00'
date: '2026-06-06T20:17:47-07:00'
authors:
  - bendu
label: manage-password-using-gopass
license: CC-BY-4.0
tags:
  - gopass
  - password
  - management
  - token
  - key
  - age
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Fedora

```sh
sudo dnf install gopass age
```

## Initialization

It is strongly recommended that you use the `gitfs` storage.

```sh
gopass setup --crypto age --storage gitfs \
    --remote gitUrl \
    --name userName \
    --email userEmail
```

which create an age identities file at\
`~/.config/gopass/age/identities`
.
The configuration file of gopass is at
`~/.config/gopass/config`
.

## Manual Configuration for Git Sync

If you have used `fs` (not recommended) instead of `gitfs` (strongly recommended)
(`gopass setup --crypto age --storage fs`)
,
you can still manually enable Git Sync using the following configuration.
However,
files added before enabling Git Sync (e.g., `.age-recipients`) are not automatically tracked,
so you have to manually track and commit them.

```sh
gopass config user.name "Your Name"
gopass config user.email "you@example.com"
gopass git init
gopass git remote add origin git@github.com:username/my-secrets-repo.git
```

```{note}
`gopass` tracks the `master` branch of the Git repository.
```

## Configuration for Timeout

```sh
gopass config age.agent-enabled true
gopass config age.agent-timeout 900
```

## Manage Passwords

gopass insert api_keys/github

gopass show api_keys/github
