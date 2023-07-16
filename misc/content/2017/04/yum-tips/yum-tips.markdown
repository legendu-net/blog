Status: published
Date: 2017-04-22 15:41:55
Author: Ben Chuanlong Du
Title: Maning Packages Using Yum in CentOS
Slug: yum-tips
Category: OS
Tags: Linux, yum, rpm, RedHat, CentOS, package management
Modified: 2020-05-22 15:41:55

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

```bash
yum update

yum search vim

yum install yum-utils

yum install pkg

yum localinstall pkg

yum groupinstall development

yum install https://centos7.iuscommunity.org/ius-release.rpm

yum info unixODBC 

rpm -ivh pkg.rpm
rpm -qa
rpm -qa | grep -i odbc
```

## Proxy

[Using yum with a Proxy Server](https://docs.fedoraproject.org/en-US/Fedora_Core/3/html/Software_Management_Guide/sn-yum-proxy-server.html)

