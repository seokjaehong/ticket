from .base import *

secrets = json.loads(open(SECRETS_LOCAL, 'rt').read())

DEBUG = True
ALLOWED_HOSTS = []
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = secrets['DATABASES']

WSGI_APPLICATION = 'config.wsgi.local.application'