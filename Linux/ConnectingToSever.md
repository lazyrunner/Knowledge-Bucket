# Automating the connection to a remote ubuntu server 

##### Author : Sudeshna Bora


<b>Goal:</b> This documentation documents the automation of connecting to a remote server from a client ubuntu machine via vpn.

<b>Software Specification:</b> <br>

The remote linux machine is Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-118-generic x86_64)<br>
The client machine is Ubuntu 20.04.2 LTS <br>
VPN used: openvpn3 <br>

## Install and Connect to openvpn3

Install openvpn3 from [source](https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux?__cf_chl_jschl_tk__=5ba086d04bb40a6e932d66d700111303d2ea9cf1-1615362411-0-AThuWJQrvtQxiIxUSuV0sLTaKqpyio0U9jD_6SpN1A874nAzJ9sDgrMfDtDydjlvakuVIIB4NxjWmWUHlHxrdhEIl8A1faLvBbTuQxeSDSFJLis6RUa8lXsMpMFal-kIxJsiXBP8gJl3NcE9qrdEFI_d8m2zfGRx4wQdgJpqB3hijGI1ivBzuESWK5NsxmSjXxtxzMXeyufVwqARPOskCGf7RJ0vJATWdQJEA3d6W2wO8cR6seM68cPsiXJ-YCpztPS8wWp3RuUmX4JPolqYTATsS1W4SQzcO9qbFzWH8g1fWd0tBxE2SNTiAVn4vxcNPhAkNsATc9zFGiK6K_05BX5-99CN4Qbg17CErnIRenN7v).
<br>
Make sure the open vpn configuration file is present in your client machine. 
<br>
<b>Command to connect to vpn:</b> <br>
  
```
openvpn2 --config [path to ovpn file] --verb 6 --daemon
```
<br>

<b> Command to list all active vpn sessions : </b>

```
openvpn3 sessions-list
```
<br>

This gives us as response with the session path. 

```
        Path: /net/openvpn/v3/sessions/7d05a17fsc2bcs4dc6sbdafs1ce614124ee0
     Created: Wed Mar 10 13:29:26 2021                  PID: 14738
       Owner: subora                                 Device: tun2
 Config name: [redacted].ovpn  (Config not available)
Session name: [redacted]
      Status: Connection, Client connected

```
<br>

We will use the session path to disconnect the session.<br>

<b>Command to disconnect the session</b>

```
openvpn3 session-manage --session-path /net/openvpn/v3/sessions/7d05a17fsc2bcs4dc6sbdafs1ce614124ee0 --disconnect
```

## SSH Connection

This section deals with connecting with the report ubuntu server. We will be using key-gen to not repeatedly feed the password while connecting. <br>
We would also then create a ssh config to keyword this connection.

<b>Command to ssh connect</b>

```
ssh [username]@[hostname/ip address]
```
This will prompt for a password. Using this password we can log into it.</br>

The next step is to use ssh key to remove the necessity to feed the password everytime. For this we will generate the key, add it into the authorised key
in the server.
<br>
<b>Command to create the authentication key</b></br>

```
ssh-keygen
```
Two keys will be created [id] and [id].pub . <br>

Move both of these keys to the <b>.ssh</b> folder.

<b>Command to transfer the private key to the remote server</b>
  
```
ssh-copy-id -i ~/.ssh/[id] [username]@[host]
```
This command transfer the private key to the remote server and adds it into the authorised keys file. This is a configuration file that stores all ssh keys that can log into this server.

Post this we can log into this server without password. 

<b>Configuring this ssh login into key</b>

So now when we want to log into the remote server we have to give [username]@[hostname] . We can convert it into a key so so that we can directly use it while sshing.

To do this we need to create a config file inside .ssh folder of our client machine. The contents of this folder is given below

```
Host [key_name]
    HostName [host ip or DNS server]
    ForwardAgent yes
    User [username]
    IdentityFile ~/.ssh/[id]
```
The identityFile is just a added here but most probably won't be required. This key specifies a file from which the user’s DSA, ECDSA or DSA authentication identity is read. 

Post this , a simple <b>ssh [key_name]</b> would be sufficient to log into the server. 

## Automating this entire process

We have now come to the last part of the document. The first two steps would be compiled together to make a single automated script. 

<b>Shell script for automation</b>

```
#!/bin/sh

echo "Starting vpn connection"
openvpn2 --config ./Downloads/BCCN-sudeshna.ovpn --verb 6 --daemon
ssh ritter_cluster
```

The first line is the shebang telling which shell or interpreter to use and to mark this script as an interpreter. 
If not given, it will just use the default shell. 

Once this is done we need to add a symbolic link to this script. Next we will discuss the symbolic link steps.

<b> Make it executable </b>

```
chmod +x [filename]
```

### Steps to create symbolic link 

<b>Find path of the shell script</b>

```
find . | egrep [filename]

or

pwd //inside the folder
```
<b>Get the folders in $PATH</b>

```
echo $PATH
```
This gives us the folders in which the terminal looks for executables. Plus when executing scripts in these folders we don't need to give full path. 

<b>Command to create symlink </b>

Symlink as the name suggests creates a symbolic link between the actual file and a key. We can circumvent this by putting the executable script in one of the $PATH folders and make it executable. 

```
ln -s [source file with path] [symbolic link]
```

<b>Command to check if symbolic link is created</b>

The above command creates the symbolic link. To check if the link is created

```
ls -l symbolic link
```

This should give us a response :

```
lrwxrwxrwx 1 linuxize users  4 Nov  2 23:03  my_link.txt -> my_file.txt
```

<b>Trouble Shooting:</b> sometimes post creating the symmlink, the command is still not recognised. In this case one of the most common issues is the symlink connection is wrong. To solve that issue we first check the symlink path , incase there is an error we remove the symlink with ``rm``.

