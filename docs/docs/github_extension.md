# GitHub Extension

Now we'll put in a "GitHub" tab into each user's JupyterLab browser that shows a "labs" and "notes" directory with pre-constructed lab assignments and notes for each JupyterHub user.

[TOC]

## Install nodejs

To install the GitHub extension for JupyterHub, first log into the server and install nodejs with conda into the ```(jupyterhubenv)``` virtual environment.

```
$ sudo systemctl stop jupyterhub
$ conda activate jupyterhubenv
(jupyterhubenv)$ conda install -c conda-forge nodejs
```

## Install GitHub extension for JupyterLub

Another conda install line to install the GitHub extension for 
JupyterLab.

```
(jupyterhubenv)$ jupyter labextension install @jupyterlab/github
```

## Restart JupyterHub and test it out

```
$ sudo systemctl start jupyterhub
$ sudo systemctl status jupyterhub
[Ctrl]-[c] to exit
```

![GitHub Extension for JupyterLab plugin tab](images/github_plugin_tab.png)

![GitHub Extension for JupyterLab repo browser](images/github_extension_repo_browser.png)

![GitHub Extension for JupyterLab notebook open](images/github_extension_notebook_open.png)

## Create notebook config file

## Aquire GitHub token

## Modify notebook config file

## pip install GitHub server extension

## Point JupyterHub to notebook config file

## Restart JupyterHub

## A way to put a default repo in?

In the notebook config file (not the jupyterhub config file):

```
c.GitHubConfig.api_url = 'https://git.myserver.com/api/v3'
```

