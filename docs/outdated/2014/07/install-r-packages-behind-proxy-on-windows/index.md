---
title: Install R Packages behind Proxy on Windows
created: '2014-07-10T01:57:25-07:00'
date: '2026-08-11T22:39:37-07:00'
authors:
  - bendu
label: install-r-packages-behind-proxy-on-windows
license: CC-BY-4.0
tags:
  - programming
  - R
  - Windows
  - install package
  - proxy
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

There are 3 ways to install R packages behind a proxy on Windows.

1. Download packages and install them locally.
   This is generally speaking not recommended
   as it is a hassle to resolve dependencies.
   When the package you want to install has no (or very few) dependencies,
   you can use this way to install it.

1. Run `setInternet2(use=True)` and then install packages as usual.
   This is the recommended way to install R packages behind a proxy on Windows.

1. Select "Internet2" when you are asked to specify standard or Internet2
   during installation of R.
   If you have done this during the installation of R,
   you can install packages as usually with no need to run `setInternet2(use=True)`.

1. If you have a proxy server to use,
   you can first setup proxy environment variables
   and then install R packages.
   Proxy environment variables can be set using the following code.

   ```
   Sys.setenv(http_proxy = 'proxy_server:port')
   Sys.setenv(https_proxy = 'proxy_server:port')
   ```

   This is a more general way and is recommended if you have a proxy serve to use.

Note that working in a Linux virtual machine on your office laptop with Windows OS
can possibly help you circumvent the proxy issue.
