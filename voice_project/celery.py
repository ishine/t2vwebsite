import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voice_project.settings')


app = Celery('voice')
app = Celery('voice')
app = Celery('voice')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
