# Setting up Python

## Author : Sudeshna Bora

So, you have decided to work on python.
In spite of on and off working on python , I hae never formalised the steps required to have a working environment ready quickly.
This document is an attempt to do that.
It is the first part that does the bare minimum of just installing python and adding it into $PATH.
The second part will deal with [conda]() and creating virtual environment for each projects. 

## Host system : Linux

---
### Step 1 : Install python/anaconda

We can simply install python but I would prefer to install <b>Anaconda</b>.
Anaconda is a python/R distribution which also provides jupyter notebook, spyder ide etc. 
<b>Conda</b> (python package manager) comes bundled with it , though we will be using <b>pip</b> which comes with python. 

#### Step 1.1: Get the installer from the anaconda homepage.

```
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
```
#### Step 1.2: Run the installer script

```
bash Anaconda3-2020.11-Linux-x86_64.sh
```

When you run it , you get options. Select what suits you. I basically select everything. Then add it into the $PATH. 
As mentioned earlier, when one types a command to run, the system looks for it in the directories specified by $PATH in the order specified. 

#### Step 1.3 : Activate the installation 

```
source ~/.bashrc
```
And we are done.

