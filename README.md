# programming with Python

This is part of my journey at ALX, it is the second sprint -aka semister (3 months)- in this sprint we will learn Python.


## Before starting
its important to have an isolated environment to be specific to the work related to alx because the project at ALX requires using Python3.8.5, and the version of Python in my machine is the latest version and will be the latest always; because of the programs depinding on it.


### Installing and isolating a Python release

To make this possible we can simply install the package related to the version we need usnig the package manager in our linux distro (in my case it is pacman; I use Arch btw ^_^), but I prefer to have this setup isolated from the global PATH where every thing is connected together, hence we will need it only for specific projects.

1. Get the vesion you want from [python/downloads]
```sh
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz
```

2. Unzip the tar.xz file you got
```sh
tar -xf <filename.tar.zx> -C <path/to/extarct>
```

Now have the source code of the release we downloaded at the path/to/extract we gave above Note that this directory will be of our virtual environment directories Here is how it will look like at the end:

```text
📂 ~/.venv         ~> imagine this as the root of our environments
│
├── 📁 rel         ~> releases we will install for the environs
│   ├── 📂 src     ~> the source code we downloaded and extracted
│   ├── 📂 bin     ~> these 3 are stantard for the installed binary 
│   ├── 📂 lib     ~~ you can use any names you prefere for any dir
│   └── 📂 lib64   ~~ instead for these 3 standard ones
│
├── 🇻 vert-env-1  ~> the virtual environments we will make later
├── 🇻 vert-env-2
└── 🇻 ....

```

3. Use the configure script to specify where we want to compile the source
```sh
./configure --exec-prefix=$HOME/.venv/rel/
```

4. Finally compile the soucre and make the release's executable binaries
```sh
make altinstall clean
```


### Making the virtual Python environment

Now we have the specific Python release we want, and it is isolated from the PATH directorys meaning that if I typed python in the terminal it will execute the version that is inside the PATH directorys and this is what I want; to avoid any conflict with the project specific Python and the global Python release used by any program in the system.

to make a virtual Python environmet see [python/venv]:
```sh
<path/to/python/executable> -m venv </path/to/new-virt-evn/directory>
```


For example: to make a Python3.8 vertual environment and its name is "ALX":
```sh
$HOME/.venv/rel/bin/python3.8 -m venv $HOME/.venv/ALX
```

To activate ALX we need to source a shell-script that will do the magic
```sh
source $HOME/.venv/ALX/bin/activate
```
Now the current shell session and any child proccess from it will act as if the python version we working on is 3.8.5 instead of 3.11 in additon we can use pip to install any Python library or package we want and it will be execlusve for the ALX environment

In our example to exit the ALX environment just type:
```sh
deactivate
```


[python/downloads]: https://www.python.org/downloads/
[python/venv]: https://docs.python.org/3/library/venv.html
