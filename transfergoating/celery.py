import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transfergoating.settings')

app = Celery('transfergoating')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'transfer-goat': {
        'task': 'farm.tasks.transfer_goats',
        'schedule': crontab(hour=14),
    },
    'arrive-farmer-every-day': {
        'task': 'farm.tasks.farmer_arrive',
        'schedule': crontab(hour=15),
    },
}
