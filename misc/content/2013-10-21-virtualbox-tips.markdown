UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Some Tips About Virtualbox
Date: 2016-07-09 22:39:06
Slug: virtualbox-tips
Category: Software
Tags: tips, virtualbox, virtualization

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
1. use command line to export guest machines (see vbvm.export.sh),
not recommended, directly copy everything is easier,
especially for windows machines

6. Check if you set a UUID for virtualbox, whether re-activation is still needed for MS word.
Another thing is too see whether VM can access usb.

7. The activation has to do with the uuid change when creating the guest. 
Windows sees this as a changed motherboard and that is enough to trigger activation.
However, 
instead of exporting and importing which does trigger this 
you can (since version 4.x of VirtualBox) simply copy the entire guests folder out 
to a saved location, 
then copy it back into the new install 
and place it back in the VirtualBox VMs folder and dbl click the `*.vbox` file. 
Since this does not re-install anything it does not require re-activation.

8. Word 2010 require reactivation on Virtualbox even if you COPY The entire virtual machine 
Word 2007 not sure, probably will work


9. If you install a backported linux image, 
the usually version of Virtualbox might not work. 
You can try the backported version of Virtualbox which will probably work.

1. The "Shared Clipboard" functionality relies on the VirtualBox Guest Additions to work.

2. you probably need to restart after if you encounter problems in virtualbox and are required to install dkms to solve it ...

## Settings

1. You'd better check "Enable PAE/NX" under the "Processor" tab in the "System" settings group
when you use a Linux guest machine on a Windows host.
This is because a Linux machine usually support Physical Address Extension (PAE),
and if PAE is not enable in VirtualBox, 
the Linux guest machine might fail to start.

## Error Messages

1. VirtualBox Version 4.3.10
     mount: wrong fs type, bad option, bad superblock on UbuntuShared,
            missing codepage or helper program, or other error
            (for several filesystems (e.g. nfs, cifs) you might
            need a /sbin/mount.<type> helper program)
            In some cases useful info is found in syslog - try
            dmesg | tail  or so
This is probably because of a bad symbolic link.
Adding a symblic link might solve the problem.

```bash
sudo ln -s /opt/VBoxGuestAdditions-4.3.10/lib/VBoxGuestAdditions /usr/lib/VBoxGuestAdditions
```

## Speedup Virtualbox

1. use fixed size disk

2. install guest additions

## VBOXManage

3. to create a shared folder 
```bash
VBoxManage sharedfolder add "VM name" --name "sharename" --hostpath "C:\test"
```

4. To change the UUID of a Virtual Machine disk.
```bash
VBoxManage internalcommands sethduuid WinTPC.vdi 
```
If you change the UUID of a disk of an existing Virtual Machine, 
it probably won't work any more. 
You can simply create a new Virtual Machine using the disk.

1. Fail to install VirtualBox Guest Additions on antiX. 
Couldn't figure out what caused the problem. 
The problem is the Linux kernel. 
After installing an older version 3.2 of kernel, VirtualBox Guest Additions can be installed successfully.

2. Better to make 32 bit virtual machines as it runs OK on both 32 and 64 bit computers.

8. Virtual machine is a good way to learn new technologies, 
summary steps to learn Oracle SQL ... and big data, virtual machines ...

## VBoxAdditions

1. Sometimes the virtual machine fails to load VBoxAdditions iso image into the CD/DVD drive. 
You can manually download the image, mount it (using mount) and then install it.

## Issues

2. it seems that VirtualBox has caused the blue screen problem on the office laptop, 
avoid using it for a while to see whether the problem comes up again.
NEVER appeared. So VirtualBox caused the problem.


1. sometimes cannot run .exe from ...

This is usually a problem when running .exe files 
from a virtual box shared folder on the windows guest. 
The solution is to run the .exe using UNC paths 
ie In your Explorer (in Windows) go to \Vboxsvr\your shared folder\path\to\folder\with\exe 
and run the .exe from there.

problematic for CygwinPortable, as you cannot install to a network folder

## Multiscreen
View -> Virtual screen 1 -> use host screen 1/2

## Network

<http://www.virtualbox.org/manual/ch06.html> covers the virtualbox networking quite well.

1. To make the guest virtual machine behave like a machine in the local network,
you have to use the bridged network.
You must choose the right network device when you use bridged network. 
For example, if the host machine is using the wireless network, 
you might have to choose `wlan0` 
(different according to network settings of the host machine).



NAT - Your host will act as a router (firewall) and your hosts will be on a private subnet. 
Use this if you are not running servers on the guests.

Bridged - Your guests will get a ip address on the same subnet as your host. 
Use this if you are running servers on the guest 
and wish to connect from other computers on the LAN.

Host Only - Sort of a hybrid. As the name implies, 
with this option you can connect to the guest servers from the host only. 
Use this for "private" (host only) servers. 
I use this if I am running a test web server.

To make a long story short, 
assuming you have a router, I would use bridged networking.
