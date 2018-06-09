import environ
from django.core.wsgi import get_wsgi_application

env = environ.Env()
env.read_env('.env')

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
env("DJANGO_SETTINGS_MODULE", default="config.settings.production")

application = get_wsgi_application()
