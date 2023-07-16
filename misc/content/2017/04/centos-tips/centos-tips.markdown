Status: published
Date: 2017-04-22 14:59:57
Author: Ben Chuanlong Du
Title: The CentOS Linux Distribution
Slug: centos-tips
Category: OS
Tags: Linux, CentOS, tips
Modified: 2020-05-22 14:59:57

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. The `wheel` group is the `sudo` group.
    So to grant a user the sudo previlege,
    just add it to the `wheel` group.

        :::bash
        gpasswd -a user_name wheel

## EPEL

    :::bash
    sudo yum -y install epel

## IUS Release

    :::bash
    sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
