Status: published
Date: 2021-09-13 22:44:33
Modified: 2021-09-13 22:44:33
Author: Benjamin Du
Slug: fix-the-CrashLoopBackOff-issue-of-pod-in-kubernetes
Title: Fix the Crashloopbackoff Issue of Pod in Kubernetes
Category: Computer Science
Tags: Computer Science, Software, tools, k8s, Kubernetes, pod, CrashLoopBackOff, container, issue, error, exception

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


Define `command` as `["/busybox/sh", "-c", "tail -f /dev/null"]`
instead of 
`["/busybox/sh", "-c", "tail", "-f", "/dev/null"]`