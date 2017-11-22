import datetime
import os
from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =os.getenv("SECRET_KEY",None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.getenv("HOSTS",None)]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DBNAME",None),
        'USER': os.getenv("DBUSER",None),
        'PASSWORD': os.getenv("DBPASS",None),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(os.getcwd(),'static')