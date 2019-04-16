import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    from .secret import *
except ImportError as e:
    pass

PRODUCTION = False

if (PRODUCTION):
    try:
        from .settings_prod import *
    except ImportError as e:
        pass
else:
    try:
        from .settings_dev import *
    except ImportError as e:
        pass


WSGI_APPLICATION = 'tidlundsved.wsgi.application'
SECRET_KEY = KEY
ROOT_URLCONF = 'tidlundsved.urls'

INSTALLED_APPS = [
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
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ved.context_processors.offerings',
                'ved.context_processors.site_title',
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

LANGUAGE_CODE = 'sv-se'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = '/home/marcus/tv/tidlundsved/static/'
STATIC_URL = '/static/'

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@tidlundsved.se'

ANYMAIL = {
    'MAILGUN_API_KEY': ANYMAIL_KEY,
    'MAILGUN_SENDER_DOMAIN': 'mail.tidlundsved.se',
}