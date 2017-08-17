UUID: 1827a10a-70e9-4bf8-877e-aef9f672b4dd
Status: published
Date: 2017-08-17 08:44:24
Author: Ben Chuanlong Du
Slug: ansible-tips
Title: Ansible Tips
Category: Software
Tags: Software, Ansible, Python, cluster management, server management

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Ansible
https://serversforhackers.com/running-ansible-programmatically

```sh
sudo pip3 install ansible
```

`ansible.cfg` in the current directory for local configuration

```sh
proxychains ansible all \
    -i hosts \
    --user=stack \
    --private-key=~/.ssh/rsa \
    -m copy \
    -a "src=../pkg.tar.gz dest=~/"
```

```sh
proxychains ansible all \
    -i hosts \
    --user=stack \
    --private-key=~/.ssh/spot_rsa \
    -a 'Rscript -e "install.packages(\"../pkg.tar.gz\")"'
```

## Host Key Checking

Ansible 1.2.1 and later have host key checking enabled by default.

If a host is reinstalled and has a different key in ‘known_hosts’, 
this will result in an error message until corrected. 
If a host is not initially in ‘known_hosts’ this will result in prompting for confirmation of the key, 
which results in an interactive experience if using Ansible, 
from say, cron. 
You might not want this.

If you understand the implications and wish to disable this behavior, 
you can do so by editing /etc/ansible/ansible.cfg or ~/.ansible.cfg:

```text
[defaults]
host_key_checking = False
```

Alternatively this can be set by an environment variable:

```sh
export ANSIBLE_HOST_KEY_CHECKING=False
```

Also note that host key checking in paramiko mode is reasonably slow, therefore switching to ‘ssh’ is also recommended when using this feature.

