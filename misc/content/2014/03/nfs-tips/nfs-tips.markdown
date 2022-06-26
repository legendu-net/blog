Status: published
Author: Ben Chuanlong Du
Date: 2014-03-10 16:03:04
Slug: nfs-tips
Title: Tips on NFS
Category: Internet
Tags: Linux, internet, web, NFS, file system, tips
Modified: 2021-01-10 16:03:04

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 

1. Make sure nfs service is not blocked. 
    Check iptables and "/etc/hosts.allow".

2. Make sure nfs service is running on the server.

    sudo service nfs-kernel-server start

2. You can choose the version of nfs using the option `-o nfsvers=n`
    while mounting directories.
    It seems to me on Debian you have to use `-o nfsvers=3` (based on a previous experience).
        mount -t nfs -o nfsvers=3 192.168.0.8:/home/dclong/downloads mnt/nfsshare
    Generally speaking, you do not have to choose a specific version manually.
    I tried on Ubuntu (server) and Linux Mint (client) and it works well with the default version (4). 

3. You can choose to change the ownership of a shared file/directory to `nobody/nogroup`
    to make it easier to access files,
    but this is not required 
    and you will probably only have read access unless the option `no_root_squash`
    is specified in the server settings 
    or your user name is the name on the client as on the server.

4. You can use wildcard in the `/etc/exports` settings. 
    For example,

        :::bash
        /nfs 192.168.*.*(ro,sync)

    shares /nfs with all local network devices with ready-only access.
    more examples

        :::bash
        *(ro,sync) all ips
        *.iastate.edu(ro,sync) all iastate.edu ips

5. You can use net mask in the `/etc/exports` settings.
    for example,

        :::bash
        /nfs 192.168.1.0/24(ro,sync)

    shares `/nfs` with local ip address 192.168.1.1 to 192.168.1.254. 
    It is equivalent to 

        :::bash
        /nfs 192.168.1.*(ro,sync)

## /etc/exports

Below is an example of `/etc/exports`.
    :::text
    # /etc/exports: the access control list for filesystems which may be exported
    #       to NFS clients.  See exports(5).
    #
    # Example for NFSv2 and NFSv3:
    # /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
    #
    # Example for NFSv4:
    # /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
    # /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
    #

    /wwwroot        *(rw,sync,fsid=0,crossmnt,no_subtree_check)

## Mount NFS

    :::bash
    #mount on Linux
    sudo mount -t nfs4 -o proto=tcp,port=2049 10.148.179.93:/ /wwwroot

    :::bash 
    # mount on macOS
    sudo mount -t nfs -o vers=4,resvport 10.148.179.93:/ mnt

## References

http://cworld.wikidot.com/mac-os-x-automount-resvport-option