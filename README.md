# Quantum Camp 2021
Resources for the summer camp at NYU. Summer of 2021, [ShabaniLab](https://shabanilab.com).   
The program starts on Monday June 28 and ends on Friday August 20. 

## Intro
Welcome to the 2021 summer quantum camp. In this summer camp we will be coding a lot to learn about quantum computing, visualizing the concepts, and designing and implementing quantum circuits on quantum hardware. 
There are some basic tools that we need to learn beforehand. 
Along with each week's lecture there is a code section in which we try to learn about how to implement problems in code, solve them, and plot the results. 
There are some basic tools that we need to learn beforehand.  

- `git`: a version control software to organize your code and keep track of the changes.  
- `python`: a programming language which all our code is based on.  
- `qiskit`: a python library from IBM which helps us design, implement, and analyze quantum circuits.  
- `jupyter`: a python library which allows us to organize our notes, codes, and plots in one file.  

## Setting up
The first step is the proper installation of these tools on your computer.  

### git 
To install `git`, you just need to follow the installation guide on the [git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). 
This software has only a *command line* interface. To check if the installation was successful you just need to run the following command:  
```
git --version
```
which prints out the version of the software 
```
git version 2.30.0
```
Here are some useful `git` commands. 
| command | what it does |  
| ---- | --- |
| `git log`  |  prints the log of previous commits to your code | 
| `git status` | prints the status of the current project |  
| `git add my_file` | add `my_file` to the stage (prepare for commiting changes) |
| `git commit -m 'my custom comment` | commit the changes with a comment on it | 
| `git push -u origin master` | push the changes to the remote directory | 

If you are not familiar with the command line, you may need to take a short online course to familiarize yourself. 
You will only need to know some basic commands. Here are some commands that are used often.  

| command | what it does |  
| ---- | --- |
|`cd my-folder`  |  change directory to `my-folder/` | 
| `cd -` | go back |  
| `cd ..` | go to the parent directory | 
| `pwd` | show current directory | 
| `ls` | show the contents (files and folders) of the current directory | 

#### Linux terminal on a Windows machine 
If you have a windows machine, you can install the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to have a linux terminal (unless you are already familiar and comfortable with windows terminal)


### Python 
The best way to install `python` is to first install *Anaconda*. You can do so by following the instructions on [Anaconda website](https://docs.anaconda.com/anaconda/install/index.html). 
After installing Anaconda you can easily install python using the following command 
```
conda install python 
``` 
To check if the installation was successful you just need to run the following commands:  
```
conda --version
python --version
```
which print out the versions of the softwares
```
conda 4.9.2
Python 3.8.5
```
After installing python you will need to install the following libraries `numpy`, `scipy`, and `matplotlib`. 
These libraries might be already installed if you used Anaconda to install python. If not you can always use `pip` to install them as follows
```
pip install numpy
pip install scipy
pip install matplotlib
```

### qiskit 
Next step is to install `qiskit` by following the instructions on [qiskit website](https://qiskit.org/documentation/getting_started.html). 

### jupyter
To install `jupyter` you can either use `conda`. 
```
conda install -c conda-forge notebook
```
or you can use `pip`
```
pip install notebook
```
You can refer to the [jupyter website](https://jupyter.org/install) for more instructions. 

### Coding exercises
Each week you will be provided with a coding exercise that incorporates the concepts in the lecture notes. All the coding exercises and tutorials are available in the folder `notebooks/` on the [github page](https://github.com/ShabaniLab/quantum-camp-2021). 
