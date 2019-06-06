import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


try:
    from tidlundsved.secret import *
except ImportError as e:
    pass

PRODUCTION = False

if (PRODUCTION):
    try:
        from tidlundsved.settings_prod import *
    except ImportError as e:
        pass
else:
    try:
        from tidlundsved.settings_dev import *
    except ImportError as e:
        pass


WSGI_APPLICATION = 'tidlundsved.wsgi.application'
SECRET_KEY = KEY
ROOT_URLCONF = 'tidlundsved.urls'

INSTALLED_APPS = [
    'settings',
    'anymail',
    'ved',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ved.context_processors.offerings',
                'ved.context_processors.site_title',
                'settings.context_processors.get_settings',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SITE_TITLE = 'Tidlunds ved'

LANGUAGE_CODE = 'en'
LANGUAGES = [
  ('sv', _('Swedish')),
  ('en', _('English')),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = '/home/mjovanc/tv/venv/project_files/static/'
STATIC_URL = '/static/'

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@tidlundsved.se'

ANYMAIL = {
    'MAILGUN_API_KEY': ANYMAIL_KEY,
    'MAILGUN_SENDER_DOMAIN': 'mail.tidlundsved.se',
}
