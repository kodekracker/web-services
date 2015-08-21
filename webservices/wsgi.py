"""
WSGI config for webservices project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webservices.settings.prod")

application = Cling(get_wsgi_application())
# application = get_wsgi_application()
