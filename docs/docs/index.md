# Welcome to the ENGR114 JupyterHub Deployment Docs

<br>

This documentation serves as a record of the JupyterHub Deployment for ENGR114 Winter 2019. 

<br>

The GitHub repo for the deployment can be found here: 

 > [https://github.com/ProfessorKazarinoff/jupyterhub-engr114](https://github.com/ProfessorKazarinoff/jupyterhub-engr114)

<br>

Click the menu items on the left to view the deployment steps.

Or start [Here](setup.md) and click the arrows at the bottom of each page.

[![Next Setup Arrow](images/next_setup.png)](setup.md)

<br>

## What is JupyterHub?

JupyterHub is a server-hosted distributed Jupyter notebook deplpyment. JupyterHub allows different users to log into a server and write Python code within a web browswer without any installation. Anywhere you have an internet connection, you can bring up a JupyterHub webpage and write/run Python code. The Jupyter notebook interface that JupyterHub provides is the same Jupyter Notebook interface you run locally. Because JupyterHub runs in a web browser, it even works on tablets and phones.

## Why JupyterHub?

Why **Jupyter Hub**? I am teaching an engineering programming course this winter. In previous quarters, I've taught MATLAB for the programming class. But this winter, I want to try teaching **Python** and cover the same concepts and learning outcomes.

If we use **Python** in the class this winter, I would like to spend the class time coding and solving problems. I don't want to spend time during class downloading Python, creating virtual environments, troubleshooting installs, dealing with system vs. non-system versions of Python, installing packages, dealing with folder structure, explaining the difference between conda and pip, teaching command-line commands, going over Python on Windows compared to Python on MacOSX... The solution is to use JupyterHub

A [series of blog posts](https://pythonforundergradengineers.com/why-jupyter-hub.html) documents my first JupyterHub deployment in Summer 2018. This documentation builds upon that previous experience.


## Main Steps

* Install PuTTY, generate SSH keys
* Create server
* Install JupyterHub and Python packages
* Acquire and link domain name to server
* Acquire SSL cert
* Create Cookie Secret, Proxy Auth Token, and dhparam.pem
* Install and configure Nginx
* Configure JupyterHub
* GitHub Authentication
* Google Authentication
* Set JupyterLab as default interface
* Create custom login page
* Pull assignments down from GitHub for each user
