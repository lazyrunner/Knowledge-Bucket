# Tips and Tricks in Linux

This document captures all the tips , tricks and nit bits I learnt while working in linux (Ubuntu - focal flavour).

#### Author Sudeshna Bora

## Packages in Linux 

| Package Name | Command | what it does |
| ------------ | ------- | ------------ |
| build-essential | ``` sudo get update && apt-get install build-essential ``` | Get all essential tools like gcc , g++ etc | 
| default-jre |``` sudo apt install default-jre ``` | Install Java Runtime Environment |
| gridengine-client| ``` sudo apt install gridengine-client ``` | Installs Distributed resource management |

## General Commands in Linux 
| Command | Explanation |
| ------- | ----------- |
|```man <commandName> ``` | ```man``` gives us the manual for the command we want to run in terminal |
| ``` tar <options> <zipped_fileName> <destination_path> ``` | archive utility software |
|``` ln <options> <sourcePath> <destinationPath>```| Creates a symbolic link. the destination path should be present in ```$PATH``` as it can be identified as executable only then. To remove just do ```rm <destinationPathWithFile>```|
|``` wget DownloadableLink```| Non interactive network downloader|
|``` ssh host ``` |secure shell login into remote server|
|``` tree ``` | lists the directory structure |
|``` ls -l``` | Detailed listing of contents of a directory with permission|
|``` ls -a ```| Lists all files |
|``` wc -l [filename]```| Number of lines in the file | 
|``` find . -name "pattern*" -printf '.' \| wc -m``` | Number of files in this folder matching a pattern |
|``` ps aux \| grep <whatever you want>```| Find the port id of running service|
|```kill <pid>```| Kills the process with this pid|
|```history``` or ```Ctrl r```| Get the history list of commands|
|```chmod -R permissions directoryName```| Gives permissions to all file inside a directory. More [information](https://github.com/SudeshnaBora/Knowledge-Bucket/blob/main/Linux/ListingAndPermission.md#GivingPermission)|
|```ssh -L local port:server port remote_server_details``` | Forwards local port to remote port (-L is local, -R is remote). Eg : ```ssh -o ServerAliveInterval=60 -NfL localhost:8889:localhost:8889 sprekeler_cluster```| 
|```sshfs <username>@<host_name>:<path> <local directory path>``` | Mounts remote folder to local folder |
|```nohup <command> &> <logfile_name> &```| Run a program in background and log output in a logfile . ```nohup``` means ```no hang up```, it prevents the process from receiving the   ```SIGNAL HANGUP``` signal , which terminates the process, and continues running the program even after the shell terminates. ```&>``` logs the output in the given output file.  ```&``` means to run the process asynchronously |
|```dpkg --print-architecture```| Prints the architecture of the os. ```dpkg``` is debian package manager, that handles ```.deb``` file. |
|```xrandr```| Gives us information about the various screens/port available in our os. This is used to to set the size, orientation and/or reflection of the outputs for a screen. |
|```command 1> <file_name> 2>&1```| Redirects standard output (file descriptor #1) and standard error (file descriptor #2) to <file_name>. ```&1``` references |

## DRM commands in linux

| Command | Explanation |
| ------- | ----------- |
| ```qsub``` | Submits a batch job for execution in compute node.  |
| ```qlogin``` |  Qlogin is similar to qsh in that it submits an interactive job to the queuing  system.  It does  not open an xterm(1) window on the X display, but uses the current terminal for user I/O. Example ```qlogin -l cuda=1 -binding linear:3```|
| ```qstat``` | used to request the status of jobs, queues, or a batch  server. |
| ```qdel``` |  A  batch  job  is  deleted by sending a request to the batch server that manages the batch job. |



