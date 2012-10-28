# -*- coding:utf-8 -*-

import sys
import os
import warnings

from os.path import abspath, dirname, join

import dj_database_url

PROJECT_ROOT = dirname(abspath(__file__))
sys.path.insert(0, abspath(join(PROJECT_ROOT, '../apps')))

DEBUG = bool(int(os.environ.get('DJANGO_DEBUG', 1)))
TEMPLATE_DEBUG = DEBUG

DEFAULT_FROM_EMAIL = u'Pug-PE <organizacao@pug.pe>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

ADMINS = (
    ('Renato Oliveira', 'renato@labcodes.com.br'),
    ('Fernando Rocha', 'fernandogrd@gmail.com'),
    ('Gileno Alves', 'gascf.cin@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///{0}'.format(join(PROJECT_ROOT, 'pugpe.db')),
    )
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Recife'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

FACEBOOK_APP_ID = '220369961426964'
# TODO: ainda nao foi colocada no heroku
# FACEBOOK_APP_SECRET = os.environ.get('FACEBOOK_APP_SECRET')

MEDIA_ROOT = join(PROJECT_ROOT, 'media')
STATIC_ROOT = join(PROJECT_ROOT, 'static')

if not DEBUG and not AWS_ACCESS_KEY_ID:
    warnings.warn(
        'Atencao! S3 NAO esta em uso, adicione variaveis de ambiente '
        'referentes para habilitar',
    )

if AWS_ACCESS_KEY_ID:
    DEFAULT_FILE_STORAGE = 'pugpe.s3utils.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'pugpe.s3utils.StaticRootS3BotoStorage'
    THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

    MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
else:
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'

# Necessário para o uso de DatabaseStorage
DB_FILES = {
    'db_table': 'FILES',
    'fname_column':  'FILE_NAME',
    'blob_column': 'BLOB',
    'size_column': 'SIZE',
    'base_url': 'http://localhost/dbfiles/'
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# Additional locations of static files
STATICFILES_DIRS = (
    join(PROJECT_ROOT, 'static_files'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev_secret_key')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "pugpe.fbutils.app_id",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pugpe.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pugpe.wsgi.application'

TEMPLATE_DIRS = (
    join(PROJECT_ROOT, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'south',
    'easy_thumbnails',
    'storages',
    'bootstrapform',

    'geo',
    'emails',
    'submission',
    'cert',
    'events',
    'core',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
