# /etc/jupyterhub/jupyterhub_conf.py

# Configuration file for JupyterHub to run GitHub OAuth.
# Need to get client ID and client secret from GitHub --> User Settings --> Developer Settings --> OAuth Apps
# also need to pip install oauthenticator

from oauthenticator.github import LocalGitHubOAuthenticator
c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

# Set up config
c = get_config()
c.JupyterHub.log_level = 10
c.Spawner.cmd = '/opt/miniconda3/envs/jupyterhubenv/bin/jupyterhub-singleuser'

# Cookie Secret Files
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'
c.ConfigurableHTTPProxy.auth_token = '/srv/jupyterhub/proxy_auth_token'

# GitHub OAuth Login
c.LocalGitHubOAuthenticator.oauth_callback_url = 'https://mydomain.org/hub/oauth_callback'
c.LocalGitHubOAuthenticator.client_id = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
c.LocalGitHubOAuthenticator.client_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
c.LocalGitHubOAuthenticator.create_system_users = True
