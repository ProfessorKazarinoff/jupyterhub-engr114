
c = get_config()
c.JupyterHub.log_level = 10
c.Spawner.cmd = '/home/peter/anaconda3/bin/jupyterhub-singleuser'

c.Authenticator.whitelist = {'peter','other'}
c.Authenticator.admin_users = {'peter'}
