UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2015-06-09 01:27:32
Slug: baidu-cloud-tips
Title: Baidu Yun Tips
Category: Internet
Tags: internet, web, Baidu Yun, cloud, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
0. Baidu cloud is a good backup solution but not a good synchronization solution.
Do not try to synchronize your devices via Baidu cloud.

1. you can apply for multiple accounts so that you have multiple 2TBs

1. `bypy -v upload` 

2. There is a unofficial client for Baidu Cloud 
at <https://github.com/LiuLang/bcloud>.
This client support fast upload (comparing hash before uploading).
However, it is not compatible with Baidu's official client. 
Suppose a file is uploaded using this unoffical client,
the offical client won't use fast upload if you upload it again.
So the suggestion is to stick with one of them.
