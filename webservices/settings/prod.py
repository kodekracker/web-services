"""
Production-ready settings. All sensitive information is sources
from environment variables.
Checklist for production-ready settings:
https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
"""
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from .base import *

DEBUG = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Rest Framework
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
    )
