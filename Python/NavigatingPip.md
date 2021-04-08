# Navigating PIP 

#### Author : Sudeshna Bora 

In the previous article (about [conda](https://github.com/SudeshnaBora/Knowledge-Bucket/blob/main/Python/NavigatingConda.md)) we spoke about <b>conda</b> as a package 
and environment manager, this article discusses <b>pip</b> , an alternative of conda for package management. 

### What is pip ?

As we already know, pip is the official package manager of python. 
It usually comes packaged with a python distribution but can be installed also. 

The command to install a package is 

```
pip install [options] <package_name>
```

When we install a package , it is usually installed in the ```site-packages``` folder of the current python. 
Putting it in the site-packages makes it easy to import the package by the ```import``` command.

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

### Important pip commands

#### Installing a package

The first command we need to know is installing a package. 

```
pip install <package_name>
```
This command fetches the sdist, wheel from pypi and copies it into the site-packages. 
However, pip can be used to install packages from source tools (vcs) , local folders , requirement files etc. 

---

#### Installing a package in development mode

This requires special mention as I found a use case of it in my life.

Whenever we are installing something, the files get copied into ```site-packages```. 
Post that if we make any changes on this package (that has been installed) it won't be reflected unless you upgrade or uninstall and reinstall the new version.
This is ok for packages that are mature. 
But what about when you are developing a distribution ? 
In that case we would need to keep on repeatedly update and check. 

The easy way to do it is <b>development</b> mode or <b>-e</b> mode.
What it does is it creates a symlink of this folder (the folder of the package which we are developing) path and stores it into the python path's site-packages. 

Let us understand this with the following example. 

We have cloned this particular repository called [brian2](https://github.com/brian-team/brian2).
We would be developing this package and would also like to check it as a module. 
For this we will follow the following steps. 

##### Step 1 : Install the package from the cloned folder in development mode

```
pip install -e brian2
```
##### Step 2 : Check where the package is cloned 

This can be checked as : 

```
pip show brian2
```
This gives us a status 

```
Name: Brian2
Version: 2.1.3.1+git
Summary: A clock-driven simulator for spiking neural networks
Home-page: http://www.briansimulator.org/
Author: Marcel Stimberg, Dan Goodman, Romain Brette
Author-email: team@briansimulator.org
License: UNKNOWN
Location: /home/subora/Documents/github_repository/brian2cuda/frozen_repos/brian2
Requires: numpy, sympy, pyparsing, jinja2, py-cpuinfo, setuptools
Required-by: 
```

If we look into the ```Location``` we see that the path is ```/home/subora/Documents/github_repository/brian2cuda/frozen_repos/brian2``` which is the path of
the cloned repository. 

However , if look into ```pip show numpy``` , it gives 

```
Name: numpy
Version: 1.16.5
Summary: NumPy is the fundamental package for array computing with Python.
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email: None
License: BSD
Location: /home/subora/anaconda3/envs/b2c/lib/python2.7/site-packages
Requires: 
Required-by: tables, statsmodels, seaborn, scikit-learn, PyWavelets, patsy, pandas, numexpr, numba, mkl-random, mkl-fft, matplotlib, imageio, h5py, Bottleneck, bokeh, bkcharts, astropy, Brian2

```
the location inside ```site-packages``` where the folder is copied from pypi. 

##### Step 3 : Go into site-packages of your python distribution.

Once inside the ```site-packages``` folder, look for the package you installed ```find . | egrep Brian2.*``` .
We see that there is a file called ```Brian2.egg-link```

##### Step 4 : See the contents of <module>.egg-link
  
It has a single line 

```
/home/subora/Documents/github_repository/brian2cuda/frozen_repos/brian2

```

This is nothing but the symlink connecting this entity to the actual folder.
Thus, when we later update this folder, it will be auto updated.

---

#### Listing packages installed 

```
pip list
```
These lists all packages installed. 

#### Show all packages installed by pip

```
pip freeze [-l]
```

The ```-l``` is used to list only those packages which are present in the local environment versus the global environment.
We can export these modules into a requirements.txt file by 

```
pip freeze >requirements.txt
```

This can be later used to be installed by ```pip install``` in a fresh environment.

#### Show information about specific package

```
pip show <package_name>
```

#### Uninstalling a package

```
pip uninstall
```

