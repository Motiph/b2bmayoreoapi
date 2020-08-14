from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'b2bmayoreo',
        'USER': 'postgres',
        'PASSWORD': 'Solecismo1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
