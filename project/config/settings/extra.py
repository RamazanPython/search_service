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
        "dms_new": {
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
