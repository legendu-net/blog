UUID: 6ce4bb50-6e82-4313-93d4-0d5ccfb9c291
Status: published
Date: 2019-01-28 22:48:30
Author: Ben Chuanlong Du
Slug: nbconvert-tips
Title: Nbconvert Tips
Category: JupyterLab
Tags: JupyterLab, nbconvert, tips, zmq.error.ZMQError

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Converting too many notebooks at the same (multiprocessing) causes `zmq.error.ZMQError: Address already in use`.
The simple way to fix this issue is to limit the number of processes converting notebooks.
It is suggested that you keep in within 3.