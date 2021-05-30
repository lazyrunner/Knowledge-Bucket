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

#### Removing a virtual environment

To delete a virtual environment 

```
conda env remove --name <env_name> [--all]

```
The ```--all``` is used to delete all packages inside that environment.

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

#### Note : Usually to install something I use pip and to create environment I use conda. 



