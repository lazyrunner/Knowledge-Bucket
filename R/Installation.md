# Installation of R and R-studio server 

### Author : Sudeshna Bora 

---

## INSTALLATION 

### Step 1 : 

Install [CRAN and other packages](https://cran.rstudio.com/bin/linux/ubuntu/)

### Step 2 : 

Install [R](rstudio.com/products/rstudio/download-server/debian-ubuntu/) 

---

## Important rstudio-server commands

### Starting server
```
sudo rstudio-server start
```
Then navigate to the server:

```
http://<server-ip>:8787
```
### Listing server 

```
sudo rstudio-server active-sessions
```
A session starts when the workspace is present in the browser.

### Stopping a server 

```
sudo rstudio-server stop
```
### Restarting a server

```
sudo rstudio-server restart
```
---





