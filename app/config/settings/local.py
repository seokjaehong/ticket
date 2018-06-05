from .base import *

# secrets = json.loads(open(SECRETS_LOCAL, 'rt').read())
# secrets_base = json.loads(open(SECRETS_BASE,'rt').read())

DEBUG = True
ALLOWED_HOSTS = []
# DATABASES = secrets['DATABASES']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
WSGI_APPLICATION = 'config.wsgi.local.application'