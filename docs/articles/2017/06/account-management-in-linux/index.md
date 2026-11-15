---
title: Account Management in Linux
created: '2017-06-22T13:30:05-07:00'
date: '2026-11-15T12:20:05-08:00'
authors:
  - bendu
label: account-management-in-linux
license: CC-BY-4.0
tags:
  - Linux
  - account management
  - group management
  - adduser
  - useradd
  - gpasswd
  - getent
---

## Create a User

Both `adduser` and `useradd` can be used to create a new user.
`adduser` is interactive while `useradd` is non-interactive.
It is suggested that you use `useradd` in batch mode
and `adduser` in non-batch mode.

```sh
useradd -o -m -u -g -d
groupadd -o -g
```

## Group

Add a user to a group.

```sh
gpasswd -a user_name group_name
```

Get information about a group.

```sh
getent group group_name
getent group group_id
```
