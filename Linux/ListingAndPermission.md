# Listing And Permission in Linux System

This article will discuss the listing permission and giving permission to files and directory in ubuntu.

## Author Sudeshna Bora 

## System Ubuntu

---

### Listing entities with permission inside a directory
<a name="listingPermission"></a>

```
ls -l

```

This gives us the list of files/directories in the current path. 
Each row of the list is in the form (example):

```
drwxr-xr-x  3 dd users   4096 Jun  10 08:01 Pictures
```

The first ```letter``` signifies what is the type of the entry. It can be directory (```d```), file (```-```) and others. 

The remaining 9 letters gives us the permision for each group. 

The number after that gives us information about the number of hard links of a file. 

The two words after that (```dd```, ```users```) tells us the <b>owner</b> and <b>group</b> of the file.

This is followed by file size (in bytes) , date of creation , Name of the file. 

---

### Understanding Permission Groups

As we mentioned above, each file has permissions associated with three groups. 
The three groups are 

1. owner (u)
2. group in which the user is part of (g)
3. others (o)
4. all (a)

---

### Understanding permissions 

There are three permissions:

1. read \[numeric 4\]
2. write \[numeric 2 \]
3. execute \[numeric 1 \]

No permission is numeric 0.

Besides this , there are other permissions also 

1. SUID \[Set user id \] . When the file will be executed by a user, the process will have the same rights as the owner of the file being executed.If set, then replaces `x` in the owner permissions to `s`, if owner has execute permissions, or to `S` otherwise.
2. SGID \[Set group id \]. Same as `SUID`, but for group. So, it will be `s` or `S` in execute place for group permissions. 
3. Stick bit . It is used to trigger process to "stick" in memory after it is finished, now this usage is obsolete. Uses `t` or `T` in the execute portion of others.
4. Execute/search only if the file is a directory or already has execute permission for some user (`X`).

|Octal Value|Text|Binary|Permission|
|---|---|---|---|
|0|---|000| no permission|
|1|--x|001| only execute (execute is 1)|
|2|-w-|010| only write (write is 2)|
|3|-wx|011| write + execute (2 +1)|
|4|r--|100| read (read is 4)|
|5|r-x|101| read + execute (4 + 1)|
|6|rw-|110| read + write (4+2)|
|7|rwx|111| read + write + execute (4+2+1)|

---

### Giving permission 
<a name="GivingPermission"></a>

In [here](#listingPermission) , we learnt how to list permission of a file/directory.

The command used to give permission is 

```
chmod options permissions directory/fileName
```

The only `option` we need to concern with is `-R` which is recursive and used to give permissions to all files under a directory or in a path. 

`chmod` stands for `change mode`.

In place of permissions we can also use `MODE`.

`MODE` is defined as 

```
[ugoa...][[+-=][perms...]...]
```

Here, `perms` is either 0 or more letters from the set `rwxXst`, or a single letter from the set `ugo` (to make it equal to either `user`,`group` or `others`).

`+-=` stands for give, remove permision or equal to the set of permissions of another group.

the `ugoa` tells us which groups permission will be changed.

Ex 

```
chmod u+x,g-x,o+r filename
```

We can also use numeric 

```
chmod 755 filename
```
gives permission 7(rwx for owner), 5(r-x for group and owner)

---

#### Note

```
chmod +x filename
```

means giving execute permission to all (can also be written as `chmod a+x filename`).

---





