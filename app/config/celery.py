import os

from celery import Celery

# Django의 세팅 모듈을 Celery의 기본으로 사용하도록 등록합니다.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings',

)
app = Celery('config')

app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
