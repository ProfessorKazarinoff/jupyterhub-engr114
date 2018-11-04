# Create a Cookie Secret and Proxy Auth Token

In addition to an SSL certificate, the [Jupyter Hub docs on security basics](http://jupyterhub.readthedocs.io/en/latest/getting-started/security-basics.html) specify that a cookie secret and poxy auth token be created. 

[TOC]

## Create the Cookie Secret

To create the cookie secret file:

```text
$ cd /srv
$ mkdir jupyterhub
$ cd jupyterhub
$ sudo touch jupyterhub_cookie_secret
$ sudo chown :sudo jupyterhub_cookie_secret
$ sudo chmod g+rw jupyterhub_cookie_secret
$ sudo openssl rand -hex 32 > jupyterhub_cookie_secret
$ ls
jupyterhub_cookie_secret
$ sudo chmod 600 jupyterhub_cookie_secret
$ ls -l
-rw------- 1 root sudo 65 Sep 14 17:41 jupyterhub_cookie_secret
```

I had trouble with the cookie secret file because I missed where the [jupyterhub docs](http://jupyterhub.readthedocs.io/en/latest/getting-started/security-basics.html#generating-and-storing-as-a-cookie-secret-file) show:

> The file must not be readable by group or other or the server won’t start. The recommended permissions for the cookie secret file are 600 (owner-only rw).

After we create the cookie secret file, we need to make note of the file's location. We'll add this location to the ```jupyterhub_config.py``` file later.

## Create Proxy Auth Token

To generate the proxy auth token, we use the same set of commands we used to create the cookie secret, except we'll point to a different file. 

```text
$ pwd
# should be in /srv/jupyterhub
$ sudo touch proxy_auth_token
$ sudo chown :sudo proxy_auth_token
$ sudo chmod g+rw proxy_auth_token
$ sudo openssl rand -hex 32 > proxy_auth_token
$ ls
jupyterhub_cookie_secret  proxy_auth_token
$ sudo chmod 600 proxy_auth_token
$ ls -l
-rw------- 1 root sudo 65 Sep 14 17:41 jupyterhub_cookie_secret
-rw------- 1 root sudo 65 Sep 14 17:47 proxy_auth_token
```

Now when we list the contents of ```~/srv/jupyterhub``` we see:

```
/srv/jupyterhub/
├── jupyterhub_cookie_secret
└── proxy_auth_token
```

## Create dhparam.pem

Let's also generate a ```dhparam.pem``` file. I'm still not exactly sure what the ```dhparam.pem``` file is, but I think it's good for security. 

First we need to ```cd``` into the ```/srv/jupyterhub``` directory. Next  ```touch``` a new file called ```dhparam.pem```. Then use ```chown``` and ```chmod``` to modify permissions. We need to be able to wirte to the file. The ```openssl dhparam``` command generates the .pem file. Finally we modify the permissions again to ```600``` (owner-only rw). Note the location of this file as we will add it to the Nginx config file.

```text
$ cd /srv/jupyterhub
$ sudo touch dhparam.pem
$ sudo chown :sudo dhparam.pem
$ sudo chmod g+rw dhparam.pem
$ sudo openssl dhparam -out /srv/jupyterhub/dhparam.pem 2048
$ sudo chmod 600 dhparam.pem
$ ls -l
-rw------- 1 root sudo 424 Sep 14 17:59 dhparam.pem
-rw------- 1 root sudo  65 Sep 14 17:41 jupyterhub_cookie_secret
-rw------- 1 root sudo  65 Sep 14 17:47 proxy_auth_token
```

We now have three files in the ```/srv/jupyterhub/``` directory. The ```jupyterhub_cookie_secret``` and ```proxy_auth_token``` will be referenced in the ```jupyterhub_config.py``` file. The ```dhparam.pem``` file will be referenced in the ```nginx.conf``` file.

```text
/srv/jupyterhub/
├── dhparam.pem
├── jupyterhub_cookie_secret
└── proxy_auth_token
```

## Next Steps

The next step is to install Nginx.

<br>