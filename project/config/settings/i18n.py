from django.utils.translation import ugettext_lazy as _

from .common import PROJECT_ROOT, MIDDLEWARE

# ------------------------- LOCALIZATION ------------------------------------
LANGUAGE_CODE = 'ru-RU'
USE_I18N = True
USE_L10N = True
LANGUAGES = (
    ('ru-RU', _('Russian')),
)
LOCALE_PATHS = (
    str(PROJECT_ROOT / 'locale'),
)
MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('django.middleware.locale.LocaleMiddleware', x) if MIDDLEWARE[i-1] == \
    'django.contrib.sessions.middleware.SessionMiddleware' else (x, ))]

# ------------------------- TIMEZONE ------------------------------------
USE_TZ = True
