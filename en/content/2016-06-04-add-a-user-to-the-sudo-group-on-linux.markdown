UUID: 714cb0b0-3623-478f-91a5-d67b00f92527
Status: published
Date: 2016-12-28 21:03:43
Author: Ben Chuanlong Du
Slug: add-a-user-to-the-sudo-group-on-linux
Title: Add a User to the "sudo" Group On Linux
Category: Linux
Tags: Linux, sudo, user, groups

There are at least 2 ways to add a user to the sudo group using command line.
```sh
gpasswd -a user_name sudo
```
Or you can use
```sh
usermod -aG sudo user_name
```
Similarly, you can add users to other groups using these 2 commands. 


Some desktop environment (e.g., GNome, Cinnamon, KDE, etc.) can also do this for you. 
Taking Cinnamon as an example, 
you can follow the steps below to add/remove groups for a user. 

1. Open `System Settings`.

2. Click `Users and Groups`.

3. Select the user you want modify.

3. Click on `Groups`.

4. Check/uncheck groups from the prompt list.

5. Click the OK to save the changes.
