"""
Settings to be used in development.
"""
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from .base import *

DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
]

ALLOWED_HOSTS = [
    '*',
]
