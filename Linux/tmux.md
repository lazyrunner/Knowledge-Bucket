# TMUX tutorial

## Author : Sudeshna Bora 

### What is TMUX?

It is a terminal multiplexer. 
It allows us to leave terminal sessions and come back to them without interrupting the running process.
It also allows us to manage a whole swarm of screens, split displays, dashboards at once.

### What is Tmux session, windows and panes ? 

There are three hierarchy in tmux namely <b>session</b> , <b>windows</b> and <b>panes</b>.
  
A Tmux session is made of a group of windows. 
Each windows can be visualised as an independent virtual machine. 
Each window can further be divided into panes. 

### tmux commands and key binding

We will mention only the important commands 

| Commands | Description |
| --- | ----------- |
| ```tmux list-commands``` | Lists all the commands |
| ```Ctrl+b``` | Binding key. |
|```Ctrl+b <arrow keys>```| To move between panes. Make sure to leave the ```Ctrl``` key before pressing <arrow Keys> otherwise it resizes the current pane|
|```Ctrl +b q``` |Gives the pane numbers|  


### Scripting a tmux workspace 

Let us create a bash script to create a tmux workspace. 
This workspace is what I use for my [Fundamental Analysis](https://github.com/SudeshnaBora/FundamentalAnalysis/tree/master/Codes/python) project and can be found [here](https://github.com/SudeshnaBora/FundamentalAnalysis/blob/master/Codes/python/setup/tmux_setup.sh).

The workspace can be visualised as 

```
_____________________________
| jupyter notebook | spyder |
|___________________________|
|          shell            |
|___________________________|

```

#### Step 1: Creating shebang

The first line of the shell script informs us what the interpretor should be. 
In this case we will be using ```bash```

```
#! /bin/bash

```

#### Step 2 : Going inside the required folder

This is very specific to this use case and is not actually needed for the ```tmux``` layout.

#### Step 3 : Creating the tmux session 

The command that we use is ```tmux new-session``` and give it a name with the short argument ```-s```.

```
session_name=FundamentalAnalysis
tmux new-session -s $session_name \; \

```
#### Step 4 : Creating jupyter notebook

For my project, I have created a virtual conda environment. To use it in our bash script we need to source [```conda.sh```](https://github.com/conda/conda/issues/7126) and then activate the virtual environment. Once that is done, we will start the jupyter notebook.

```
send-keys 'source /home/subora/anaconda3/etc/profile.d/conda.sh' C-m \; \
send-keys 'conda activate stockAnalysis' C-m \; \
send-keys 'jupyter notebook' C-m \; \

```
#### Step 5 : Create the next pane and start spyder. 

```

split-window \; \
send-keys 'source /home/subora/anaconda3/etc/profile.d/conda.sh' C-m \; \
send-keys 'conda activate stockAnalysis' C-m \; \
send-keys 'spyder' C-m \; \

```

#### Step 6 : Create the final pane and activate the conda environment there. 

```
split-window \; \
send-keys 'source /home/subora/anaconda3/etc/profile.d/conda.sh' C-m \; \
send-keys 'conda activate stockAnalysis' C-m \; \
select-layout tiled \

```

For both <b>Step 5</b> and <b>Step 6</b> we use ```split-window``` command to create a new pane. We then use ```select-layout tiled``` to evenly space 
the three panes created. There are other [layouts](https://manpages.ubuntu.com/manpages/precise/en/man1/tmux.1.html#contenttoc6) available.

---

The final bash file looks like this 

```
#! /bin/bash

# go inside the requisite folder
cd /home/subora/Documents/github_repository/FundamentalAnalysis/Codes/python/

#create a tmux session
session_name="FundamentalAnalysis"

#a new session is created which currently has only one pane
# important point , do not give commands between these lines
tmux new-session -s $session_name \; \
send-keys 'source /home/subora/anaconda3/etc/profile.d/conda.sh' C-m \; \
send-keys 'conda activate stockAnalysis' C-m \; \
send-keys 'jupyter notebook' C-m \; \
split-window \; \
send-keys 'source /home/subora/anaconda3/etc/profile.d/conda.sh' C-m \; \
send-keys 'conda activate stockAnalysis' C-m \; \
send-keys 'spyder' C-m \; \
split-window \; \
send-keys 'source /home/subora/anaconda3/etc/profile.d/conda.sh' C-m \; \
send-keys 'conda activate stockAnalysis' C-m \; \
select-layout tiled \

```

As you can notice , we cannot have any comments between ```tmux new-session``` and the remaining lines. 
This is because all of these a single chained command. 
