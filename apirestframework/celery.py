import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apirestframework.settings')

app = Celery('apirestframework')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
