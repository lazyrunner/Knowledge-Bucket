# Linux Directory Tree 

This document discusses the various directory structure of a linux operation system .

## System Configuration 

The command to find the linux distribution is ```lsb_release -a```. 

```
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.2 LTS
Release:	20.04
Codename:	focal

```

#### Author : Sudeshna Bora

---

### Root directory 

The first directory is the root directory. It is the root of the linux directory tree. 
It can accessed by ```cd /```.

Checking the contents of the root directory by ```ls```, gives us :

```
bin   cdrom  etc   lib    lib64   lost+found  mnt  proc  run   snap  sys  usr
boot  dev    home  lib32  libx32  media       opt  root  sbin  srv   tmp  var
```

It is not related to the super user account.

### Bin directory

This folder has all the binaries required for maintainance, boot up , repair etc i.e. for single user use.
If we do ```ls -l /``` for detailed listing, we find :

```
lrwxrwxrwx   1 root root     7 Feb  2 22:13 bin -> usr/bin
```
The ```bin``` folder is linked to the ```usr/bin```. 

### cdrom directory

This is a legacy folder kept for mounting devices . 

### etc directory

This directory has system wide configuration files. 

### lib and lib\<qual\> directories

The /lib directory contains those shared library images needed to boot the system and run the commands in the root filesystem, ie. by binaries in ```/bin``` and ```/sbin```.

Alternatively,  ```/usr/lib``` includes object files, libraries, and internal binaries that are not intended to be executed directly by users or shell scripts. 

However, if we look into the extended listing command ```ls -l /```, we see the ```lib``` is a link to ```/usr/lib```.

```
lrwxrwxrwx   1 root root     7 Feb  2 22:13 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Feb  2 22:13 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Feb  2 22:13 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Feb  2 22:13 libx32 -> usr/libx32

```

### lost\+found directory

On Linux, the ```fsck``` command—short for “file system check”—examines your file systems for errors. fsck may find bits of “orphaned” or corrupted files in the file system. 
If it does, fsck removes those corrupted bits of data from the file system and places them in the lost+found folder.
Each directory has its own ```lost+found``` directory.

```
(base) subora@subora-Lenovo-ideapad-330-15IKB:/$ sudo su
[sudo] password for subora: 
root@subora-Lenovo-ideapad-330-15IKB:/# cd lost+found/
root@subora-Lenovo-ideapad-330-15IKB:/lost+found# ls
```

### mnt directory

The /mnt directory and its subdirectories are intended for use as the temporary mount points for mounting storage devices,
such as CDROMs, floppy disks and USB (universal serial bus) key drives.
Mounting is the process of attaching an additional filesystem, which resides on a CDROM, hard disk drive (HDD) or other storage device, 
to the currently accessible filesystem of a computer. 

### proc directory

Good [tutorial](https://www.tecmint.com/exploring-proc-file-system-in-linux/)

 It is a Virtual File System.
 It contains system information as well as various directories representating various running processes. 
 
### run directory

It is a temporary file system which comes into the file system before ```/usr/run``` is created. 

Good [tutorial](https://www.networkworld.com/article/3403023/exploring-run-on-linux.html).

Identified as a “tmpfs” (temporary file system), we know that the files and directories in /run are not stored on disk but only in volatile memory.
They represent data kept in memory (or disk-based swap) that takes on the appearance of a mounted file system to allow it to be more accessible
and easier to manage.

### snap directory

The /snap directory is, by default, where the files and folders from installed snap packages appear on your system.

#### What are snap ? 

Snaps are cross-distribution, dependency-free, and easy to install applications packaged with all their dependencies to run on all major Linux distributions.

### sys directory 

/sys is an interface to the kernel. 
Specifically, it provides a filesystem-like view of information and configuration settings that the kernel provides, much like /proc. 
Writing to these files may or may not write to the actual device, depending on the setting you're changing. It isn't only for managing devices,
though that's a common use case.

We can use it to manage minotor brightness , mac address etc. 

Documentation [here](https://www.kernel.org/doc/Documentation/filesystems/sysfs.txt).

### 


