
from oauthenticator.google import GoogleOAuthenticator
c.JupyterHub.authenticator_class = GoogleOAuthenticator

c.GoogleOAuthenticator.hosted_domain = 'mycollege.edu'
c.GoogleOAuthenticator.login_service = 'My College Name'

# fill out client secret and client id in ./env
#    $ source ./.env to get github environment variables
#    $ sudo full/path/to/jupyterhub
