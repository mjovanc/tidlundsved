DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_SEND_TO = 'mjovanc@protonmail.com'
EMAIL_SEND_FROM = 'noreply@tidlundsved.se'
LIST_OF_EMAIL_RECIPIENTS = ['mjovanc@protonmail.com']
