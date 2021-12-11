# Commands and topics for vim configuration 

The ongoing configuration file can be found [here](https://github.com/SudeshnaBora/dotfiles/blob/main/.vimrc).  

### Vim version : 8.1 (ubuntu 20.04)

---
## Vim runtimepath

These are the paths where vim looks for scripts and documentation. 
It is like ```PYTHON_PATH``` for python interpreter to identify modules. 
Command to find runtimepath

```
:set runtimepath?

runtimepath=~/.vim,~/.vim/plugged/gruvbox,~/.vim/plugged/vim-fugitive,~/.vim/
plugged/vim-man,~/.vim/plugged/ctrlp.vim,~/.vim/plugged/YouCompleteMe,~/.vim/pl
ugged/undotree,~/.vim/plugged/vim-ripgrep,~/.vim/plugged/ale,~/.vim/plugged/tab
ular,~/.vim/plugged/vim-markdown,~/.vim/plugged/markdown-preview.nvim,/var/lib/
vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim81,/usr/share/vim
/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/plugged/tabular
/after,~/.vim/plugged/vim-markdown/after,~/.vim/after
```
As can be seen, it contains path of all the plugins installed as per the .vimrc.

---
## Vim plugin manager 

There are different plugin manager. The manager I use is [vim-plug](https://github.com/junegunn/vim-plug).
All plugins are mentioned in the ```.vimrc``` between the ```vim-plug``` block :

```
call plug#begin('~/.vim/plugged')

" Plugin name
Plug 'morhetz/gruvbox'

call plug#end()
```
This block clones the repos of the plugin from github and stores it in the ```~/.vim/plugged``` folder mentioned. 
It then adds the path to the ```runtimepath``` so that it can be used by vim.

### Commands for vim-plug

Command to install plugin 

```
:PlugInstall
```
Command to uninstall plugin

```
:PlugClean
```

---

## Vim Plugin : markdown-preview 

This plugin helps in previewing markdown in real time (while typing) . 

The first step to install is mentioning it inside ```plug#begin``` and ```plug#end``` block.
**Make sure nodejs and yarn have been installed in the system**.

```
" If you have nodejs and yarn
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && yarn install'  }
```
However, only doing ```:PlugInstall``` does not install it. 
Once we have done ```:PlugInstall```, we need ```:call mkdp#util#install()``` and restart vim. 

### Command to Preview

Open the markdown file you are developing and want to preview. 

Then type 

```
:MarkdownPreview
```
This opens a browser. Post that we can see the preview as we type. 

---

