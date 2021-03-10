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

The next step is to use ssh key to remove the necessity to feed the password everytime. 




