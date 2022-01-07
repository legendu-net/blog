Status: published
Date: 2022-01-01 13:47:32
Modified: 2022-01-03 18:54:21
Author: Benjamin Du
Slug: get-centos-version
Title: Get CentOS Version
Category: Computer Science
Tags: Computer Science, programming, CentOS, Linux, version

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

You can get the version of CentOS
using the following command.

    :::bash
    rpm -q centos-release

This trick can be used to get the version of the CentOS distribution on a Spark cluster.
Basically, 
you run this command in the driver or workers to print the versions 
and then parse the log of the Spark application.
