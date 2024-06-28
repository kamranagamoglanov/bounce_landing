import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bounce_landing.settings')

app = Celery('bounce_landing')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'expiration-date': {
    'task': 'skin_care.tasks.deactivate_product',
    'schedule': 15
    },
}
app.conf.timezone = 'Asia/Baku'