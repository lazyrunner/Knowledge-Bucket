# Navigating Conda 

#### Author : Sudeshna Bora

This is part two of setting up a python environment series. 
In the previous [document](https://github.com/SudeshnaBora/Knowledge-Bucket/blob/main/Python/SettingUp.md) , we have set up a anaconda distribution.
In this section, we will be talking about how to start working on this distribution and some other information that can be found.

### What is Conda ? 

Conda is a package manager. Python has its own default package manager called <b>pip</b>. 
Unlike pip, conda is language agnostic i.e. it can install non python packages (packages that don't have setup.py file in them). 
Conda installs packages from [anaconda cloud](https://anaconda.org/) or [anaconda repository](https://repo.anaconda.com/) whereas pip install packages from [python package index (pyPI)](https://pypi.org/).
Additionally, conda manages packages via their binaries unlike pip which uses [wheel]. 

Additionally, conda is also an environment manager to create different virtual environments. 
This cannot be done in pip. We need other packages like [virtualenv](https://virtualenv.pypa.io/en/latest/) and [venv](https://docs.python.org/3/library/venv.html).

Information about conda can be found using ```conda info``` command. This gives us 

```
     active environment : base
    active env location : /home/sudeshna/anaconda3
            shell level : 1
       user config file : /home/sudeshna/.condarc
 populated config files :
          conda version : 4.10.1
    conda-build version : 3.21.4
         python version : 3.8.8.final.0
       virtual packages : __cuda=10.1=0
                          __linux=4.15.0=0
                          __glibc=2.27=0
                          __unix=0=0
                          __archspec=1=x86_64
       base environment : /home/sudeshna/anaconda3  (writable)
      conda av data dir : /home/sudeshna/anaconda3/etc/conda
  conda av metadata url : https://repo.anaconda.com/pkgs/main
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /home/sudeshna/anaconda3/pkgs
                          /home/sudeshna/.conda/pkgs
       envs directories : /home/sudeshna/anaconda3/envs
                          /home/sudeshna/.conda/envs
               platform : linux-64
             user-agent : conda/4.10.1 requests/2.25.1 CPython/3.8.8 Linux/4.15.0-46-generic ubuntu/18.04.2 glibc/2.27
                UID:GID : 2002:2007
             netrc file : None
           offline mode : False
```

information about the current conda installed into our system. 

---

## Conda Channels

### What are conda channels ? 

We now know that ```conda``` is a package manager. However, how does the conda find the packages (which are nothing but packaged applications) to install into our system. This is where ```conda channels``` come into play. ```Conda channels``` are nothing but repositories/locations where these packages are uploaded to be used. 

If we look into the ```conda info``` above we see a key called ```channel urls``` , going into any of the urls we find a number of packages uploaded there which will inturn be downloaded and executed (installed) when we do ```conda install```.  

When we do ```conda list <package_name>```, it gives us information regarding from which channel the package was installed, the build number etc.

```
conda list _libgcc_mutex

# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main    anaconda

```
Additionally, the four urls mentioned above are from the ```default channels``` of the anaconda channels. 

Every conda installation comes with the urls for the default channel. To check how many channels are present in the installation we can use ```conda config --show channels```.

```
conda config --show channels

channels:
  - defaults
```

Furthermore, the urls of the channels can be shown as 

```
conda config --show default_channels

default_channels:
  - https://repo.anaconda.com/pkgs/main
  - https://repo.anaconda.com/pkgs/r

```

Currently, all the four urls mentioned in ```conda info``` belongs to ```defaults``` channel. 

### How many channels are there ?

We have a number of channels. The most important are ```defaults```, ```anaconda``` , ```conda-forge``` , ```bioconda``` and ```pypi```. 

### How to add new channel into our conda configuration? 

Before going to <b>how</b> , it is important to ask <b> why</b>.

As we know, a channel is nothing but a repository where the packages are uploaded. Sometimes, it may so happen that some packages are not present in the ```default``` or ```anaconda``` repository, but is present in another repository (conda-forge). For eg: ```xorg-kbproto``` is not present in the default channel but is present in ```conda-forge``` (this we can find by searching for it in [anaconda](https://anaconda.org/search?q=xorg-kbproto) or [pypi](https://pypi.org/)). 

However, a simple ```conda install xorg-kbproto``` without configuration change is not going to find the package as it is not looking in the correct place. 
We can solve this issue by either mentioning the channnel while installing 

```
conda install -c[/--channel] conda-forge xorg-kbproto
```
or by adding this channel into the conda configuration

```
conda config --add channels conda-forge

conda config --show channels

channels:
  - conda-forge
  - defaults
  
 conda info
 
      active environment : None
            shell level : 0
       user config file : C:\Users\sudes\.condarc
 populated config files : C:\Users\sudes\.condarc
          conda version : 4.10.3
    conda-build version : 3.20.5
         python version : 3.8.5.final.0
       virtual packages : __win=0=0
                          __archspec=1=x86_64
       base environment : E:\Programs\Anaconda  (writable)
      conda av data dir : E:\Programs\Anaconda\etc\conda
  conda av metadata url : None
           channel URLs : https://conda.anaconda.org/conda-forge/win-64
                          https://conda.anaconda.org/conda-forge/noarch
                          https://repo.anaconda.com/pkgs/main/win-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/win-64
                          https://repo.anaconda.com/pkgs/r/noarch
                          https://repo.anaconda.com/pkgs/msys2/win-64
                          https://repo.anaconda.com/pkgs/msys2/noarch
          package cache : E:\Programs\Anaconda\pkgs
                          C:\Users\sudes\.conda\pkgs
                          C:\Users\sudes\AppData\Local\conda\conda\pkgs
       envs directories : E:\Programs\Anaconda\envs
                          C:\Users\sudes\.conda\envs
                          C:\Users\sudes\AppData\Local\conda\conda\envs
               platform : win-64
             user-agent : conda/4.10.3 requests/2.24.0 CPython/3.8.5 Windows/10 Windows/10.0.21296
          administrator : True
             netrc file : None
           offline mode : False
           
```

Post adding the config command, we can see that new channel and new channel urls have been added.

Post this we can easily install packages available in that channel. 

---
### Important conda commands 

---

#### Creating virtual environment

The first important command of conda is to create a virtual environment. 
It is adviced that each project have its own virtual environment in order to prevent package mismatch etc. 

```
conda create -n <env_name> [python=2.7] [list of packages you want installed]

Eg:

conda create -n b2c python=2.7 anaconda
```

The above command creates a virtual environment named "b2c" with python2.7 as the python interpreter version and installs anaconda into it.

We can also create an environment using a ```environment.yml``` file. The skeleton of the file is as 

```
name: <environment name>
channels: 
  - anaconda
  - conda-forge
  - defaults
dependencies:
  - [library name]
  - pip:
    - [pip package]
prefix : [path of the virtual environment]
```
The ```name``` gives the name of the virtual environment. The ```channels``` gives the channels to look for the packages. ```dependencies``` give us the 
packages required. In case the package is available only in pip , we install it as a pip subprocess. 
Finally, ```prefix``` gives us the path of the virtual environment. However, this field is not used while creating an environment.

The command to create a virtual environment using yaml file is a bit different

```
conda env create --file environment.yml
```
A point to be noted is, all dependencies (not pip packages) are installed as executable in ```bin``` of the virtual environment and can be found using 
```which package```, whereas all pip packages installed by pip sub package are installed and found in ```site-package``` inside the python folder of the 
virtual environment. This can be found using ```pip show```.

There are other options which can be found by 

```
conda create --help
```

---

#### List virtual environment 

Most often we forget the environments we have made. 

```
conda env list
```
The above command lists all the environments we have created along with the path. 
As can be seen. the virtual environment is nothing but a folder inside the anaconda folder. 

---

#### Activate and Deactivate virtual environment

To activate and deactivate a virtual environment we will use the following commands 

```
conda activate <env_name>
```
and 

```
conda deactivate <env_name>
```

Once it is activated , the terminal command prompt will have the name of the environment.

---

#### Removing a virtual environment

To delete a virtual environment 

```
conda env remove --name <env_name> [--all]

```
The ```--all``` is used to delete all packages inside that environment.

---

#### Exporting the virtual environment 

```
conda env export -f environment.yml
```
---

#### Listing packages in a virtual environment

To list packages in an activated environment , we use

```
conda list
```

This packages can be written into a requirement.txt which can be later used to create another virtual environment using ```conda create```.
The command to write it into requirements.txt

```
conda list -e > requirements.txt
```
---

#### Installing packages

Till now we have discussed about conda environment manager. We know that conda can also install packages from its binaries without a compiler. 
The command we use to install , update and uninstall are :

```
conda install <package_name>
```

followed by 

```
conda update [package_name]
```
and finally 

```
conda uninstall <package_name>
```

---

So, we have come to the end of a simple introduction to conda. 
In another [document]() we will be discussing pip and what it does and how it does what it does. 

#### Note : Usually to install something I use pip and to create environment I use conda. However, this is not adviced. The first priority to install a package should be given to conda channels (conda-forge, anaconda) and only if not present should go into pip.



