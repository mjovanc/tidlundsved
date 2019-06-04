DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tidlundsved_dev',
        'USER': 'mjovanc',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

EMAIL_SEND_TO = 'mjovanc@protonmail.com'
EMAIL_SEND_FROM = 'noreply@tidlundsved.se'
