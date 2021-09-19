Status: published
Title: Synchronization and Backup Solutions
Author: Ben Chuanlong Du
Date: 2014-03-04 22:11:05
Slug: synchronization-and-backup-solutions
Category: Software
Tags: software, synchronization, backup, Baidu Yun, Dropbox, TeamDrive, Syncthing
Modified: 2021-09-19 12:03:07

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tips and Traps

1. Almost all sychronization tools have problems with symbolic links.
    Most of them just ignore symbolic links.
    This makes sense as following symbolic links can causes serious disk problems.
    If not followed then symbolic links are likely broken on other device.
    The simple suggestion is do not place symbolic links in your synchronization folders.

2. Backup large non-privacy files on Baidu Yun or Wei Yun.

2. Backup large privacy critial files on Mega or encrypt them first and then backup to Baidu Yun or Wei Yun.

3. Build a local home server (e.g., using NFS or SAMBA) for sharing files.

1. Among non-native sync & backup apps TeamDrive, Mega Sync, OneDrive (official client) are usable in mainland of China.

Dropbox, TeamDrive, Mega, Syncthing, Baidu Yun, Wei Yun

<table style="width:100%">
  <tr>
    <th> Name </th>
    <th> Opensource/free </th>
    <th> OS </th>
    <th> GUI/CLI </th>
    <th> Sync/Backup </th>
    <th> Directly Accessible from Mainland of China </th>
    <th> Comments </th>
  </tr>
  <tr>
    <td> 
    <a href="https://www.dropbox.com/"> Dropbox </a>
    </td>
    <td> free for 3 devices and 2G space  </td>
    <td> Windows, macOS, Linux </td>
    <td> GUI </td>
    <td> Sync </td>
    <td> No </td>
    <td> 
    1. Best solution for small data backup 
    2. every thing is in the same folder, no way to sync a folder with higher priority over others
        while you can do this with TeamDrive or BTSync
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://pan.baidu.com/disk/home"> Baidu Net Disk </a>
    </td>
    <td> free for 2T space and limited download speed  </td>
    <td> Windows, macOS, Linux </td>
    <td> GUI </td>
    <td> Sync </td>
    <td> Yes </td>
    <td> 
    Best solution for large data backup
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://synqion.com/"> Synqion (TeamDrive) </a>
    </td>
    <td> free for 2G space </td>
    <td> Windows, macOS, Linux </td>
    <td> GUI </td>
    <td> Sync </td>
    <td> Yes </td>
    <td> 
    1. Best solution for small data backup 
    1. extremely secure, good for private, sensitive docs
    3. separated spaces which is much better than dropbox
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://syncthing.net/"> Syncthing </a>
    </td>
    <td> free </td>
    <td> Windows, macOS, Linux </td>
    <td> Both </td>
    <td> Sync </td>
    <td> Yes </td>
    <td> 
    1. extremely secure, good for private, sensitive docs
    2. good performance on large files but poor performance on small files
    3. Best solution for private personal backup 
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.google.com/drive/"> Google Drive </a>
    </td>
    <td> free for 15G space </td>
    <td> Windows, macOS </td>
    <td> GUI </td>
    <td> Sync </td>
    <td> No </td>
    <td> 
    1. good for backing up Google products
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage"> OneDrive </a>
    </td>
    <td> free for 15G space </td>
    <td> Windows, macOS </td>
    <td> GUI </td>
    <td> Sync </td>
    <td> No </td>
    <td> 
    1. good for backing up MS products
    </td>
  </tr>
  <tr>
    <td> 
    <a> NAS / NFS </a>
    </td>
    <td> free </td>
    <td> Windows, macOS, Linux </td>
    <td> Both </td>
    <td> network file system </td>
    <td> Yes </td>
    <td> 
    1. easy to use
    2. provided to employees by many companies
    3. relatively low performance
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://mutagen.io/"> Mutagen </a>
    </td>
    <td> Opensource </td>
    <td> Windows, macOS, Linux </td>
    <td> CLI </td>
    <td> sync </td>
    <td> Yes </td>
    <td> 
    1. fast file synchronization;
    2. network forwarding 
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/bcpierce00/unison"> Unison </a>
    </td>
    <td> Opensource </td>
    <td> Windows, macOS, Linux </td>
    <td> CLI </td>
    <td> 2-way sync </td>
    <td> Yes </td>
    <td> 
    2-way sync, fault tolerance
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/deajan/osync"> osync </a>
    </td>
    <td> Opensource </td>
    <td> Windows, macOS, Linux </td>
    <td> CLI </td>
    <td> 2-way sync </td>
    <td> Yes </td>
    <td> 
    2-way sync, rsync-based, fault tolerance
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/rsnapshot/rsnapshot"> Rsnapshot </a>
    </td>
    <td> free </td>
    <td> Windows, macOS, Linux </td>
    <td> CLI </td>
    <td> Backup </td>
    <td> Yes </td>
    <td> 
    1. easy to use
    2. quick access
    3. copy on change which takes more disk space than incremental backup tools but it is much simpler to use and is very robust
    </td>
  </tr>
  <tr>
    <td> 
    <a href="http://www.nongnu.org/duplicity/"> duplicity </a>
    </td>
    <td> free </td>
    <td> Windows, macOS, Linux </td>
    <td> CLI </td>
    <td> Backup </td>
    <td> Yes </td>
    <td> 
    1. incremental backup
    2. support encryption
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/backuppc/backuppc"> backupPC </a>
    </td>
    <td> free </td>
    <td> Windows, macOS, Linux </td>
    <td> ? </td>
    <td> Backup </td>
    <td> Yes </td>
    <td> 
    high performance, enterprise-grade system
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.bacula.org/"> Bacula </a>
    </td>
    <td> Opensource </td>
    <td> Windows, macOS, Linux </td>
    <td> ? </td>
    <td> Backup </td>
    <td> Yes </td>
    <td> 
    enterprise-level computer backup system for heterogeneous networks 
    </td>
  </tr>
</table>

## References

https://alliance.seas.upenn.edu/~bcpierce/wiki/?n=Main.UnisonFAQTips

http://xmodulo.com/synchronize-files-between-two-servers.html

http://superuser.com/questions/31512/how-to-synchronize-the-home-folder-between-multiple-computers

csync: https://www.csync.org/

http://thanhsiang.org/faqing/node/192

http://fak3r.com/2009//howto-build-your-own-open-source-dropbox-clone/ 14.09.2016

