from pathlib import Path
from .extra import *
import os
import logging
import sys

logger = logging.getLogger(__name__)

# ------------------------- PROJECT ROOT -----------------------------------
DJANGO_ROOT = Path(__file__).resolve(strict=True).parent.parent
PROJECT_ROOT = DJANGO_ROOT.parent

# ------------------------- SITE -------------------------------------------
SITE_NAME = DJANGO_ROOT.name

# ------------------------- STATIC FILES ------------------------------------
STATIC_ROOT = PROJECT_ROOT / 'staticfiles'
STATIC_URL = '/staticfiles/'
STATICFILES_DIRS = [
    PROJECT_ROOT / 'static',
]

# ------------------------- MEDIA FILES ------------------------------------
MEDIA_ROOT = PROJECT_ROOT / 'media'
MEDIA_URL = '/media/'

# ------------------------- TEMPLATES --------------------------------------
PROJECT_TEMPLATES = [
    PROJECT_ROOT / 'templates',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
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

# ------------------------- APPS PATH ---------------------------------------
sys.path.append(str(PROJECT_ROOT / 'apps'))

# ------------------------- TIMEZONE -----------------------------------------
TIME_ZONE = os.environ.get('TIMEZONE', 'Asia/Almaty')

# ------------------------- INSTALLED APPS ------------------------------------
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ------------------------- MIDDLEWARE ---------------------------------------
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

# ------------------------- ROOT URL ---------------------------------------
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)

# ------------------------- LOCALIZATION ------------------------------------
USE_I18N = False
from .i18n import *

# ------------------------- STUFF -------------------------------------------
ADMINS = (
    ('Rakhimbayev Ramazan', 'rakhimbayev.ramazan@gmail.com'),
)
MANAGERS = ADMINS

# ------------------------- SECURITY ----------------------------------------
SECRET_FILE = str(PROJECT_ROOT / 'config' / 'settings' / 'run' / 'SECRET.key')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECRET_KEY = os.environ.get('SECRET_KEY')
if SECRET_KEY is None:
    logger.debug('Could not find key in the environment!')

    logger.debug('Trying to read SECRET_KEY from SECRET_FILE...')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
        logger.info('Read SECRET_KEY from SECRET_FILE.')
    except IOError:
        logger.debug('Could not open SECRET_FILE ({})!'.format(SECRET_FILE))

        try:
            from django.utils.crypto import get_random_string

            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
            SECRET_KEY = get_random_string(50, chars)
            with open(SECRET_FILE, 'w') as f:
                f.write(SECRET_KEY)

            logger.info('Generated a new SECRET_KEY and stored it in SECRET_FILE ({})!'.format(SECRET_FILE))
        except IOError:
            logger.exception('Could not open SECRET_FILE ({}) for writing!'.format(SECRET_FILE))
            raise Exception('Could not open {} for writing!'.format(SECRET_FILE))
else:
    logger.info('Fetched SECRET_KEY from environment.')
