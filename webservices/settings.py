# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'ajdo2vda-asd323i120sj130wu12-jws')

DEBUG = False

ALLOWED_HOSTS = ['.up.railway.app', '.akshayon.net']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_extensions',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webservices.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webservices.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Parse database configuration from $DATABASE_URL
if not os.environ.get('DATABASE_URL', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    # https://github.com/kennethreitz/dj-database-url
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL')
        )
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_ETAGS = True

DEFAULT_CHARSET = 'utf-8'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.IsAuthenticated',
    ),
    'EXCEPTION_HANDLER': 'app.utils.custom_exception_handler',
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'
}

# Email smtp settings
EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.mailgun.org'

EMAIL_HOST_USER = os.getenv('MAILGUN_SMTP_USER', None)

EMAIL_HOST_PASSWORD = os.getenv('MAILGUN_SMTP_PASSWORD', None)

EMAIL_PORT = 587

EMAIL_SUBJECT = '[akshayon.net] Contact Us - Message from {first_name} {last_name}'

EMAIL_TO = 'admin@akshayon.net'

APPEND_SLASH = True

# django-cors configuration
CORS_ORIGIN_ALLOW_ALL = True

# Twitter App settings
TWITTER_SCREEN_NAME = os.getenv('TWITTER_SCREEN_NAME', None)
TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY', None)
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET', None)
TWITTER_ACCESS_TOKEN_KEY = os.getenv('TWITTER_ACCESS_TOKEN_KEY', None)
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', None)

# RSS FEED URL
RSS_FEED_URL = "http://blog.akshayon.net/feeds/all.atom.xml"

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# import local settings, if any
try:
    from local_settings import *  # noqa: F401,F403
except ImportError as e:  # noqa: F841
    pass
