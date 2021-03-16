# Tips and Tricks in Linux

This document captures all the tips , tricks and nit bits I learnt while working in linux (Ubuntu - focal flavour).

#### Author Sudeshna Bora

## Packages in Linux 

| Package Name | Command | what it does |
| ------------ | ------- | ------------ |
| build-essential | ``` sudo get update && apt-get install build-essential ``` | Get all essential tools like gcc , g++ etc | 
| default-jre |``` sudo apt install default-jre ``` | Install Java Runtime Environment |

## Commands in Linux 
| Command | Explanation |
| ------- | ----------- |
|```man <commandName> ``` | ```man``` gives us the manual for the command we want to run in terminal |
| ``` tar <options> <zipped_fileName> <destination_path> ``` | archive utility software |
|``` ln <options> <sourcePath> <destinationPath>```| Creates a symbolic link. the destination path should be present in ```$PATH``` as it can be identified as executable only then. To remove just do ```rm <destinationPathWithFile>```|
|``` wget DownloadableLink```| Non interactive network downloader|
|``` ssh host ``` |secure shell login into remote server|

