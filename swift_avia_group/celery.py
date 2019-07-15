from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
#from LK.tasks import sum_list_numbers


# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swift_avia_group.settings")

app = Celery('proj')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


#from LK.tasks import *
from celery.schedules import crontab

app.conf.beat_schedule = {
    # 'add-every-minute-contrab': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': crontab(),
    #     'args': (16, 16),
    # },
    # 'add-every-5-seconds': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': 5.0,
    #     'args': (16, 16)
    # },
    # 'add-every-30-seconds': {
    #     'task': 'tasks.add',
    #     'schedule': 30.0,
    #     'args': (16, 16)
    # },

    # 'add-every-monday-morning': {
    #     'task': 'sum_list_numbers',
    #     'schedule': crontab(hour=16, minute=50),#crontab(hour=16, minute=10, day_of_week=1),
    #     'args': (),
    # },hour='16-17',

    # 'add-every-day-after-work': {
    #     'task': 'hello_world',
    #     'schedule': crontab(hour='12-13', minute='30-35', day_of_week='*'),  #crontab(),# # hour=15,  crontab(hour=16, minute=10, day_of_week=1),
    #     'args': (),
    # },
    # 'add-every-day-after-work-2': {
    #     'task': 'otchet_zavedeno',
    #     'schedule': crontab(hour=13, minute=30, day_of_week='*'),  #crontab(),# # hour=15,  crontab(hour=16, minute=10, day_of_week=1),
    #     'args': (),
    # },
    # 'email-to-client-every-days': {
    #     'task': 'sum_list_numbers',
    #     'schedule': crontab(hour=10, minute=30, day_of_week='*'),  #crontab(),# # hour=15,  crontab(hour=16, minute=10, day_of_week=1),
    #     'args': (),
    # },
}

app.conf.timezone = 'Europe/Kiev'