from .base import *

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())

DEBUG = False
ALLOWED_HOSTS = [
    'amazonaws.com',
]
DATABASES = secrets['DATABASES']
WSGI_APPLICATION = 'config.wsgi.production.application'

# DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'
# STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'