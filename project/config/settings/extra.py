import os

# ------------------------- CORS ------------------------------------
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ['http://localhost', 'http://127.0.0.1']
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with'
]

# ------------------------- REST FRAMEWORK ------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'PAGE_SIZE': 30,
    'EXCEPTION_HANDLER': 'drf_handlers.formatter.errors_exception_handler'
}

# ----------------------------- CACHE ----------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', '6378')}/{os.getenv('REDIS_DB', '0')}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# ------------------------- AUTH ------------------------------------
AUTH_ALGORITHM = 'HS256'
AUTH_TOKEN_SECRET = 'secret'
AUTH_USER_MODEL = "users.User"

# ------------------------- SHELL ------------------------------------
SHELL_PLUS = "ipython"

# ------------------------- LOGGING ------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["console"]},
    "formatters": {
        "verbose": {
            "format": (
                "[%(asctime)s] %(levelname)s %(name)s %(message)s [PID:%(process)d:%(threadName)s]"
            )
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'WARNING',  # DEBUG will log all queries, so change it to WARNING.
            'propagate': False,  # Don't propagate to other handlers
        },
        "search_service": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True
        },
    },
}

# ------------------------- SWAGGER ------------------------------------
SPECTACULAR_SETTINGS = {
    'TITLE': 'search_service',
    'DESCRIPTION': 'Description of project',
    'VERSION': '1.0.0',
    'COMPONENT_SPLIT_REQUEST': True
}

# Celery
CELERY_BROKER_URL = f"redis://{os.environ.get('REDIS_HOST', 'localhost')}:{os.environ.get('REDIS_PORT', '6378')}/{os.environ.get('REDIS_DB', '0')}"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Almaty'
CELERY_RESULT_BACKEND = f"redis://{os.environ.get('REDIS_HOST', 'localhost')}:{os.environ.get('REDIS_PORT', '6378')}/{os.environ.get('REDIS_DB', '0')}"
CELERY_CACHE_BACKEND = 'django-cache'
CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# EXCHANGE RATE
EXCHANGE_RATE_URL = os.environ.get('EXCHANGE_RATE_URL', 'https://www.nationalbank.kz/rss/get_rates.cfm')

# PROVIDER URLS
PROVIDER_A_URL = os.environ.get('PROVIDER_A_URL', 'http://web:8000/api/v1/provider_a/search/')
PROVIDER_B_URL = os.environ.get('PROVIDER_B_URL', 'http://web:8000/api/v1/provider_b/search/')
