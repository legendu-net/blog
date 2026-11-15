---
title: Find Out Proxy in Use
created: '2014-05-27T21:31:02-07:00'
date: '2026-11-15T09:20:09-08:00'
authors:
  - bendu
label: find-out-proxy-in-use
license: CC-BY-4.0
tags:
  - web
  - internet
  - proxy
---

1. Using a Web Service.

   1. Open <http://wpad/wpad.dat>.

   1. Figure the proxy out from the contents it returns.

1. Use the command `netstat`.
   This is a universal way and is especially helpful
   when <http://wpad/wpad.dat> is not available.

   1. Inspect the output of `netstat -an | egrep "EST|Proto"` ("EST" is short for "ESTABLISHED")
      in a Linux-like environment.
      You can use Cygwin if you are on Windows.
      Note that `netstat` comes with Windows not Cygwin.
      If you cannot use it in Cygwin,
      it is probably due to a misconfigured path environment variable.
      You can of course run the `netstat -an` command in the command prompt in Windows
      but you do not have a convenient command like `grep`.

   1. Go to a fresh site that you have not recently visited.

   1. Run the `netstat -an | grep "EST"` command again
      and look for the new connection.
      It might look like the following.
      In this example,
      your proxy's IP is 192.168.1.88 and it is listening on port 8080.
      A proxy server typically listens to the 8080 port.

      ```
       TCP 192.168.1.1:1989 192.168.1.88:8080 ESTABLISHED
      ```

The second method only shows the proxy currently in use.
If more than one proxy is configured in your environment,
and you want to know all of them,
you have to repeat the procedure above periodically to get the full list.
Note that working in a Linux virtual machine on your office laptop with Windows OS
can possibly help you circumvent the proxy issue.
