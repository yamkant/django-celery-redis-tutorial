
# reference: https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

app = Celery('config')

app.config_from_object(
    "django.conf:settings",
    namespace="CELERY",
)
app.autodiscover_tasks()


app.conf.timezone = 'Asia/Seoul'
app.conf.beat_schedule = {
    "test-periodic-job": {
        "task": "api.tasks.test_periodic_task",
        'schedule': crontab(),
        # "schedule": crontab(
        #     minute=0
        # )
    }
}
