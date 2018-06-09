# -*coding: utf-8 -*-
"""
Local settings

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
"""

import socket
import datetime
import os
from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='_w60i(j@wyo$f2fx79nrd@$a2g3+r=fk$ap-#@q=olq9&-d-1y')

# Mail settings
# ------------------------------------------------------------------------------


# CORS Configuration
CORS_ORIGIN_ALLOW_ALL = True

# django-debug-toolbar
# ------------------------------------------------------------------------------

# tricks to have debug toolbar when developing with docker

# TESTING
# ------------------------------------------------------------------------------

# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------