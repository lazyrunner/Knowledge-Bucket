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

For binaries usable before the /usr partition is mounted.

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

### usr directory

This is a misnomer. 
It was used once ```/bin``` directory was full and does not pertain to ```user``` directory. 

### boot directory

The ```/boot/``` directory holds files used in booting the operating system. 

Tutorial about the files inside [boot](https://www.linuxnix.com/linux-directory-structure-explained-boot-folder/).

### dev directory

All Linux device files are located in the ```/dev``` directory which is an integral part of the root ```(/)``` filesystem because these device files must be available to the operating system during the boot process.

### home directory

This directory has sub home directories for each user. The ```/home/<username>/``` is the homedirectory. 
It can be changed using ```/etc/passwd```. 

Each user has its own home directory. The home directory can be accessed by ```~```.

### media directory 

The /media directory contains subdirectories where removable media devices inserted into the computer are mounted.

### opt directory

This directory is for the installation of add-on application software packages.
It is a directory for installing unbundled packages (i.e. packages not part of the Operating System distribution, but provided by an independent source), 
each one in its own subdirectory.
Alternatively, ```usr/local``` is a place to install files built by the administrator, typically by using the ```make``` command .

### root directory

It is the home directory of the root user. 
To go inside this directory we have to used ```sudo su```. 

### sbin directory

For binaries usable before the ```/usr``` partition is mounted but for binaries with ```superuser (root)``` privileges required.

### srv directory 

The /srv/ directory contains site-specific data served by your system.
This directory gives users the location of data files for a particular service, such as FTP, WWW, or CVS.
Data that only pertains to a specific user should go in the /home/ directory.

### tmp directory

In Unix and Linux, the global temporary directories are /tmp and /var/tmp. Web browsers periodically write data to the tmp directory during page views and downloads. Typically, /var/tmp is for persistent files (as it may be preserved over reboots), and /tmp is for more temporary files.

### var directory 

It contains files to which the system writes data during the course of its operation.

---
