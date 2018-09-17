UUID: 2a10dee5-5230-4889-b81f-130b020576ef
Status: published
Date: 2017-08-26 21:10:22
Author: Ben Chuanlong Du
Slug: configure-ssh-to-use-a-proxy-server
Title: Configure SSH to Use a Proxy Server
Category: Linux
Tags: Linux, SSH, proxy server

Suppose you have a production server that you want to visit via SSH,
however, 
it is not accessible directly. 
Instead,
you have to visit it from a bastion/proxy server.
You can configure SSH to use the bastion/proxy server when visiting the production server. 
```
Host <production_server>
ProxyCommand ssh <proxy_server> -W %h:%p

Host *

SendEnv LANG LC_*
HashKnownHosts yes
GSSAPIAuthentication yes
GSSAPIDelegateCredentials no
# make connection alive
ServerAliveInterval 90
ServerAliveCountMax 3
```

1. Wildcard and NOT operator are supported.

        Host *.xxx.xxx.com !*.exclude.com
        ProxyCommand ssh proxy_server_address -W %h:%p   
        Host *
