from celery import Celery
# from celery.schedules import solar
from celery.schedules import crontab 

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ManNirmal.settings')

app = Celery('ManNirmal')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'SENDING BIRTHDAY EMAILS': {
        'task': 'onbase.tasks.send_birthday_emails',
        # 'schedule': 15,
        # 'schedule': solar('sunrise', 22.5726, 88.3639),
        'schedule': crontab(hour=7, minute=0, day_of_week='0-6'),
        
    }
}

app.conf.timezone = 'Asia/Kolkata'

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
