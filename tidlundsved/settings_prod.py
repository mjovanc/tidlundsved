import os

ADMINS = [('Marcus Cvjeticanin', 'Marcus Cvjeticanin')]

DEBUG = False
ALLOWED_HOSTS = ['tidlundsved.se', 'www.tidlundsved.se', '35.195.44.203']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CONN_MAX_AGE = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tidlundsved_db',
        'USER': 'postgres',
        'PASSWORD': os.environ['DATABASE_KEY'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_SEND_TO = 'andtidlund@hotmail.com'
EMAIL_SEND_FROM = 'noreply@tidlundsved.se'
LIST_OF_EMAIL_RECIPIENTS = ['andtidlund@hotmail.com']