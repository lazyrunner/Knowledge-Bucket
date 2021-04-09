# Creating python package or module

#### Author : Sudeshna Bora

This is a work along tutorial for creating a packages and modules in python. 
These packages and modules can be latter installed by [pip](https://github.com/SudeshnaBora/Knowledge-Bucket/blob/main/Python/NavigatingPip.md) and/or [conda](https://github.com/SudeshnaBora/Knowledge-Bucket/blob/main/Python/NavigatingConda.md).

---

### What are distributions in python ? 

A versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a Release. 
The archive file is what an end-user will download from the internet and install.

<b>Distutils</b> tool is used to register the metadata of the created distribution to PyPI and upload the distributions.

#### What is sdist ? 

sDist is source distribution. The packages have the course code , any data file required and a ```setup.py``` file.
A source distribution is packaged by : 

```
python setup.py sdist
```
When installing a package (uwsgi) having only source distribution by ```pip install```. 
We see 

```
Collecting uwsgi==2.0.*
  Downloading uwsgi-2.0.18.tar.gz (801 kB)
     |████████████████████████████████| 801 kB 1.1 MB/s
Building wheels for collected packages: uwsgi
  Building wheel for uwsgi (setup.py) ... done
  Created wheel for uwsgi ... uWSGI-2.0.18-cp38-cp38-macosx_10_15_x86_64.whl
  Stored in directory: /private/var/folders/jc/8_hqsz0x1tdbp05 ...
Successfully built uwsgi
Installing collected packages: uwsgi
Successfully installed uwsgi-2.0.18
```
the logs . 
First the ```tar``` file is downloaded. 
Then a wheel is packaged and labelled.
Then it is installed from the wheel. 

#### What is wheel ?

Wheel is a built distribution. It is essentially a zip file.
It means while installing a package wheel, it need not be built (like in sDist) and can be directly installed. 
This makes it faster and smaller. It cuts off using ```setup.py``` file .

We can create wheel by 

```
python setup.py bdist_wheel
```

While installing a package with a wheel available. 
We see reduced steps 

```
Collecting chardet
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 1.5 MB/s
Installing collected packages: chardet
Successfully installed chardet-3.0.4
```

There is a nomenclature to label wheels. It is <b>{dist}-{version}(-{build})?-{python}-{abi}-{platform}.whl</b>.

If we unzip a wheel. 

```
Archive:  six-1.14.0-py2.py3-none-any.whl
  Length      Date    Time    Name
---------  ---------- -----   ----
    34074  01-15-2020 18:10   six.py
     1066  01-15-2020 18:10   six-1.14.0.dist-info/LICENSE
     1795  01-15-2020 18:10   six-1.14.0.dist-info/METADATA
      110  01-15-2020 18:10   six-1.14.0.dist-info/WHEEL
        4  01-15-2020 18:10   six-1.14.0.dist-info/top_level.txt
      435  01-15-2020 18:10   six-1.14.0.dist-info/RECORD
---------                     -------
    37484                     6 files
```

---

### Where are these distributions stored ?

These archived version are usually stored in <b>PyPI</b>. 
It is usually stored as source distributions(<b>sdist</b>) or precompiled <b>wheels</b>.

---

So now, lets get into creating a module. 

The folder structure is as follows:

```
parentFolderName
|
| -> README.md
| -> setup.py
| - moduleName 
    |
    | -> __init__.py
    | -> fileName.py    
```

So, let's understand each of these before we move onto creating it. 

The ```README.md``` file contains the information about the modules. 

The ```moduleName``` folder contains the modules with the functionality. Using ```__init__.py``` file shows that this folder is a module. 
It can be empty or not. 

```filename.py``` contains the functionality. 

Now we come to the ```setup.py``` file. 

---

### What is setup.py ?

It is a python file which is used to install packages into the system or create distribution and update into pypi.

Example of a ```setup.py``` is 

```
from setuptools import find_packages, setup

setup(
      name ='stockLibraries',
      packages = find_packages(include = ['stockLibraries']),
      version = '0.1.0',
      description = 'Fundamental Stock Analysis Libraries',
      author = 'Sudeshna Bora',
      license = 'MIT',
      install_requires = ['requests']
      )
```

We can directly use ```setup.py``` to install a package or use it n develop mode.

The command for the same is 

```
python setup.py install/develop
```

Just like ```pip install -e``` , ```develop``` creates a symlink in site-packages to the folder where the module is present. 

The command above is usually not followed. 
Inorder to install the package locally in your global python environment or virtual python environment.
We will use 

```
pip install [-e] path/to/rootFolder/
```

---

Once the setup file and everything is done. 
To install it locally, use 

```
pip install [-e] path/to/rootFolder
```

Once that is done, we can import it like any other module.

```
from packageName.fileName import functionName
```

The next step is trying to publish it in pypi.

For that, we will create a distribution file either a source distribution or a built distribution. 

This can be done by the following command

```
python setup.py sdist bdist_wheel 
```

Here, ```sdist``` is source distribution and ```bdist``` is built distribution with file type as ```wheel```.

Then to push it into either test pypi or production pypi , we use the following command.

```
twine upload --repository testpypi/pypi dist/*  
```

For creating and publishing the distribution we need the ```wheel``` and ```twine``` packages.

---
#### Note : 

Instead of using ```twine```. We can use ```python setup.py upload``` and to build we can use ```setuptools```.


---
