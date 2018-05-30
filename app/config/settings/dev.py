from .base import *

secrets = json.loads(open(SECRETS_DEV, 'rt').read())

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '.ap-northeast-2.compute.amazonaws.com',
    '127.0.0.1'
]
DATABASES = secrets['DATABASES']