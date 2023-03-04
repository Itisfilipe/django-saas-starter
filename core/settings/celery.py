from celery import Celery

from .django import env


celery_app = Celery("core")

celery_app.conf.update(
    result_backend=env.str("CELERY_RESULT_BACKEND"),
    cache_backend=env.str("CELERY_CACHE_BACKEND"),
    broker_url=env.str("CELERY_BROKER_URL"),
    task_serializer=env.str("CELERY_TASK_SERIALIZER"),
    beat_schedule={}
)

# Load task modules (tasks.py) from all registered Django apps.
celery_app.autodiscover_tasks()
