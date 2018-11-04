# JupyterHub Configuration

Next, we'll create a ```jupyterhub_config.py``` file and modify it to include our cookie secret and proxy auth token. 

[TOC]

## Create jupyterhub_config.py

We'll create the JupyterHub config file in the ```/etc/jupyterhub``` directory. After the directory is created, we need to modify the directory permissions. Then ```cd``` into it create the config file with ```jupyterhub --generate-config```. Make sure you are in the ```(jupyterhubenv)``` virtual environment when you run the command.  

```
$ cd /etc
$ mkdir jupyterhub
$ sudo chown -R root:peter jupyterhub/
$ sudo chmod -R g+rwx jupyterhub/
$ cd jupyterhub
$ conda activate jupyterhubenv
(jupyterhubenv)$ jupyterhub --generate-config
```

## Modify jupyterhub_config.py

Now we'll modify the ```jupyterhub_config.py``` file to allow local spawners and include our user ```peter``` as an admin user:

```
$ nano jupyterhub_config.py
```

There will be a lot of commented out text in the ```jupyterhub_config.py``` file. At the top of the file, add the following:

```python
# /etc/jupyterhub/jupyterhub_config.py

import os
c = get_config()
c.JupyterHub.log_level = 10
c.Spawner.cmd = '/home/peter/miniconda3/envs/jupyterhubenv/bin/jupyterhub-singleuser'

# Cookie Secret Files
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'
c.ConfigurableHTTPProxy.auth_token = '/srv/jupyterhub/proxy_auth_token'

c.Authenticator.whitelist = {'peter'}
c.Authenticator.admin_users = {'peter'}

```

<br>

## Restart nginx and start jupyterhub, see if we can login

Now we'll restart Nginx and start JupyterHub. Not that this time when we start JupyterHub we don't need to use the ```--no-ssl``` flag. This is because we have SSL running on nginx. 

If it seems like Nginx isn't working, try ```$ sudo systemctl status nginx``` and see if nginx really started. If it didn't, try the command ```nginx -t```. This command prints out any error messages if nginx failed to start. I had to trouble shoot Nginx many a lot before I got Nginx and JupyterHub working together.

```text
$ sudo systemctl stop nginx
$ sudo systemctl start nginx
$ sudo systemctl status nginx
# [ctrl-c] to exit
```

Once Nginx is running, restart JupyterHub without the ```--no-ssl``` flag. Make sure the ```(jupyterhubenv)``` virtual environment is active before running the ```jupyterhub``` command.

```text
$ cd /etc/jupyterhub
$ conda activate jupyterhubenv
(jupyterhubenv)$ jupyterhub
```

Log in to JupyterHub with the non-root sudo username (```peter```) and password (same user that's running the PuTTY session). 

Now we can browse to our domain and see JupyterHub running in its full SSL glory.

<br>

## Create an new user, restart JupyterHub and Login.

OK, it's all well and good that we can log in. But the purpose of setting up JupyterHub is for multiple students to be able to log on an run Python code. To test if multiple students can run Python code on JupyterHub at the same time, we need to create another user on the server.

If JupyterHub is still running, stop it with [Ctrl] + [c].  Let's create a new user and see if we can log in as her.

```text
$ sudo adduser kendra
```

Go through the prompts and remember the UNIX password. Now we'll modify ```jupyterhub_conf.py``` to include our new user ```kendra``` and add ```peter``` (our non-root sudo user) as an administrator:

```text

...

c.Authenticator.whitelist = {'peter','kendra'}
c.Authenticator.admin_users = {'peter'}

```

Restart JupyterHub and try and login as ```kendra```

```
(jupyterhubenv)$ jupyterhub
```
