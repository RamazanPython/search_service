import os
from django.conf import settings

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.settings')
celery_app = Celery('config', broker=settings.CELERY_BROKER_URL)
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(settings.INSTALLED_APPS)


celery_app.conf.beat_schedule = {
    'update-exchange-rate-every-day': {
        'task': 'airflow.tasks.exchange_rate.exchange_rate_task',
        'schedule': crontab(hour='12', minute='0')
    },
}
