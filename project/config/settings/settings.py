import os

from .common import *
from .extra import *

import environ

env = environ.Env()
environ.Env.read_env()

# ------------------------- HOSTS ------------------------------------
ALLOWED_HOSTS = ['*']

# ------------------------- INSTALLED APPS ------------------------------------
INSTALLED_APPS = DEFAULT_APPS
INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'drf_spectacular',

    # APPS
    'users',
    'utils',
    'provider_a',
    'provider_b',
    'airflow',
]

# ------------------------- MIDDLEWARE ------------------------------------
MIDDLEWARE = [
    *MIDDLEWARE,
]

# ------------------------- DATABASE ------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}
# ------------------------- DEBUG ------------------------------------
DEBUG = env.bool('DEBUG', False)
