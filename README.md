# jupyterhub-svr

This repo contains the shared files used to create a JupyterHub server on Digital Ocean using an Nginx proxy server and SSL security. This deployment is for an Engineering Programming class (ENGR114) at Portland Community College during Winter 2019.

## Deployment Docs

Docs for this deployment of JupyterHub can be found here:

 > [https://professorkazarinoff.github.io/jupyterhub-engr114/](https://professorkazarinoff.github.io/jupyterhub-engr114/)

For another deployment of JupyterHub on Digital Ocean with Nginx proxy. See the blog posts:

> [https://pythonforundergradengineers.com/why-jupyter-hub.html](https://pythonforundergradengineers.com/why-jupyter-hub.html)

## Basic Steps

1. Get SSH public and private keys with PuTTYgen. Save SSH keys in Documents/ssh-keys
2. Create a new Digital Ocean Droplet (DO server) running Ubuntu 18.04. Include SSH key when Droplet is created
3. Log into DO server as root with PuTTY and SSH keys. Create a non-root sudo user (username: peter).
4. Log into DO server as non-root sudo user with PuTTY and SSH keys
5. Install miniconda
6. Create conda env with Python 3.6
7. Conda install packages including numpy, pandas, matplotlib, jupyter, notebook, scipy, sympy, pyserial and xlrd
8. Conda install -c conda-forge jupyterhub pint
9. Run JupyterHub (for just a minute) without SSL to see if it works. Go to the DO server IP address and start a notebook
10. Link a google domain to DO name servers. In DO DNS link domain name to DO server.
11. Create SSL keys with let's encrypt
12. Modify jupyterhub_config.py with SSL keys
13. Start nginx and browse to domain. Should see nginx splash page
14. Modify nginx config to move traffic to Jupyter Hub
15. Start nginx and jupyter hub. Should be able to go to https://domain.com and start a new notebook
16. Add authentication and user logins
17. Add custom login page
18. Celebrate!

## Steps in more detail

### Install Miniconda in /opt on the server

The URL of the latest Miniconda install for Linux will look something like:

```text
https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Download bash installer with curl

```text
$ cd /tmp
$ curl -O $ https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ sudo bash Miniconda3-latest-Linux-x86_64.sh
```

Specify following installation directory:

```text
/opt/miniconda3/
```

Deal with some permission issues. Make sure the non-root sudo= user ```peter``` has read, write, and execute permissions on the enitre ```/opt/miniconda3/``` directory.

```text
$ cd /opt
$ ls
miniconda3
$ ls -la
total 12
drwxr-xr-x  3 root root 4096 Oct 30 04:47 .
drwxr-xr-x 23 root root 4096 Oct 29 17:49 ..
drwxr-xr-x 13 root root 4096 Oct 30 04:47 miniconda3
```

Modify the read, write, execute privaleges so that the group ```root``` can read, write, and execute (```rwx```).

```text
$ sudo chmod -R g+w miniconda3/
$ ls -la
total 12
drwxr-xr-x  3 root root 4096 Oct 30 04:47 .
drwxr-xr-x 23 root root 4096 Oct 29 17:49 ..
drwxrwxr-x 13 root root 4096 Oct 30 04:47 miniconda3
```

Change the group corresponding to the miniconda3 directory from ```root``` to ```peter```.

```text
$ sudo chown -R root:peter miniconda3/
$ ls -la
total 12
drwxr-xr-x  3 root root  4096 Oct 30 04:47 .
drwxr-xr-x 23 root root  4096 Oct 29 17:49 ..
drwxrwxr-x 13 root peter 4096 Oct 30 04:47 miniconda3
```

### Conda env and packages

Create a Python 3.6 conda env, activate and install packages

```text
$ conda create -n jupyerhubenv python=3.6
$ conda activate jupyterhubenv
(jupyterhubenv)$ conda install numpy matplotlib pandas scipy sympy seaborn bokeh holoviews pyserial xlrd jupyter notebook 
(jupyterhubenv)$ conda install -c conda-forge pint altair
(jupyterhubenv)$ conda install -c conda-forge jupyterhub
```


