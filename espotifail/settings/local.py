from .base import *

SECRET_KEY = 'b*@za=3u3wog+jmw@ktq5exume5223lnqpq-lto5gdi#_m*pc$'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'espotifail',
        'USER': 'admin_espoti',
        'PASSWORD': 'espotifail2017',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}