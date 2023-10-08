# -*- coding:utf-8 -*-

import os
from datetime import timedelta

import django
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotsearchapi.settings.dev')
django.setup()

backend = 'redis://127.0.0.1:6379/2'
broker = 'redis://127.0.0.1:6379/1'
app = Celery(__name__, broker=broker, backend=backend, include=['celery_task.newhot_task', ])

app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False
app.conf.beat_schedule = {
    'add-task': {
        'task': 'celery_task.newhot_task.newhot_update',
        'schedule': timedelta(seconds=1),
        # 'args':(300,150),
    }
}
# celery worker -A celery_task -l info -P eventlet
# celery beat -A celery_task -l info
