#  Getting Started

In this document, we will focus on installing, configuring and remote connection with github.

## Author : Sudeshna Bora

---

## Step 1 : Installing git 

Depending on the os , git can come pre installed or we may need to install
it manually. 
To check if git is installed, use :

```
git --version

```

If it gives the version, the git is already installed. 
Otherwise follow the steps as mentioned below based on your operating system-

### Ubuntu OS

```
Open Terminal (Ctrl+Alt+T)
Step 1 : sudo apt update 
Step 2 : sudo apt install git
Step 3 : git --version 
```

### MAC OS

We can install git (if not already installed) by either following the steps mentioned in an [installer](https://sourceforge.net/projects/git-osx-installer/files/) or with homebrew. 
Below we are mentioning the steps used for installing git via homebrew. 
Use these steps only if homebrew has been installed. 

```
Open terminal
Step 1: brew install git
Step 2: git --version
```

### Windows OS

Installing git in windows can be done by downloading the installer from the [source](https://git-scm.com/downloads) and following the steps once the installer is started. 

---

## Step 2: Configuring git 



For this step, successful completion of Step 1 is mandatory. 
This section only configures the basic information required to make git functioning in your system. There are other configurations that a user can do for their convenience. 

Before configuring, go to github and open a profile with a user name and a valid email address. This user name and email address will need to be stored in your local system for git to authenticate any request from your local to github. 

The configurations are stored in a number of files but the file we should be concerned about is ```.gitconfig```. 
This file is usually in the home directory but is hidden. 
The see this file , open your terminal/command prompt and type ```ls -a```.

There are two ways of configuring your username and email.

### Way 1 : Configuring user name and email

```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

### Way 2 : Configuring user name and email.

**Step 1:** Go to home directory. I do it in my terminal by ```cd ~```.

**Step 2:** Open .gitconfig using any editor. I personally use vim so I type```vim .gitconfig```.

**Step 3:** Edit .gitconfig file to add these lines

```
 [user]
     name = John Doe
     email = johndoe@example.com
```

You can choose whichever method you find feasible. I personally like the second method as it feels intuitive to me.

As the scope of this tutorial is to give a bare bone feel of github installation. You can learn more about github configurations [here](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup). 

---

## Step 3 : Checking if configuration is correct [Optional]

This is an optional step. Here, we check if the git connection and configurations are correct.

To check if the configurations are correct: 

```
git config --global --list
```
This lists all the configurations mentioned in .gitconfig file. 

---

## Step 4 : Setup communication with remote. 

This is the last step of setting up git locally. 
For us to make proper use of project development with version control (git);we would store our projects in github etc. For this, we need to connect to the remote (maybe to pull latest changes from remote project to update our local version, copy a remote project into our local for development etc). 

Currently, with our setup we can communicate with git but would be repeatedly asked for our username and password. 
Github has provided us a way to circumvent this stage. In this section, we would be discussing about that. 
The detailed steps for setting up ssh connection for git can be found [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). In this section, we would go through the steps sequentially. 

**What is ssh?**

SSh or secure shell is a network protocol that gives users a secure way to access a computer over an unsecured network. In our case, a secure way to connect our local system to www.github.com.

### Step 1 : Installing SSH [Skip if installed and running ] 

#### Windows OS 

Open windows powershell. Then type the following command :

```
Add-WindowsCapability -Online -Name OpenSSH.Client*
```

Post this ssh should be installed and ready to use. 

#### Mac OS

SSH comes pre installed in mac. However, it is not enabled. To enable it we use the following command:

```
sudo systemsetup -getremotelogin on
```
We can check the status of ssh by using the command ```sudo systemsetup -getremotelogin```.

#### Linux OS

To install ssh in linux (ubuntu) use the following commands (in terminal):

```
Step 1: sudo apt update

Step 2: sudo apt install openssh-server

```

Once the installation is done, ssh should be running automatically, to check the status 

```
sudo systemctl status ssh

```

**Troubleshooting:** In case firewall is not allowing ssh connection in ubuntu, try this command in terminal ```sudo ufw allow ssh```.

### Step 2: Check if ssh key is already created

SSH keys are stored in ```~/.ssh``` folder. So the first step is to check if the ssh folder is present. 
This can be done using 

```
ls -a ~/.ssh
```

or the listing alternative command for your os. 
In case the folder is present, it will list all the keys present. Otherwise,make a new folder ```mkdir ~/.ssh```.

Now if your .ssh folder has ssh key that you recognise was created for github, you can skip to Step 4. 

### Step 3: Create ssh key 

Use your github email id to create an ssh key : 

```
ssh-keygen -t ed25519 -C "github_email@example.com"
```

Every ssh key generation creates a private key and a public key (.pub) which are stored in your ~/.ssh folder. While creating the ssh key, you will be prompted to name the files. I suggest you give an intuitive name so as to identify the purpose of that ssh key. 

### Step 4: Add ssh key to ssh-agent

ssh-agent is a program that stores your private key. Before adding the newly generated ssh key, make sure the ssh-agent is running. 

The command to run ssh-agent for mac and linux is ```eval "$(ssh-agent -s)``` and for windows it is ```eval `ssh-agent -s``` followed by ```ssh-agent -s```.

Then add the private key (file without .pub extension) into ssh-agent :

```
ssh-add ~/.ssh/github_key

```

### Step 5: Add public ssh key in github

Copy the contents of the public ssh key file (file with .pub extension) and go to www.github.com. In github go to ```settings``` and click on ```New SSHkey``` button. 
Then, give a proper name in the ```Title``` section and copy the public key in the ```Key``` section.

Then save this new ssh key. 

---

## Final Step : Check if the ssh connection is proper

Once all of this is done, we can check the connection from our local to www.github.com is proper. 

Use this command :

```
ssh -T git@github.com
```

We should get a response acknowledging our authentication :

```
Hi SudeshnaBora! You've successfully authenticated, but GitHub does not provide shell access.
```

In this tutorial, we learnt about installing and configuring our github. In next tutorial, we will learn about a common work flow of github with an example. 




















