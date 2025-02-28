from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imageProject.settings')

app = Celery('imageProject')

# Load task modules from all registered Django app configs.
app.config_from_object(settings, namespace='CELERY')

# Auto-discover tasks in installed Django apps
app.autodiscover_tasks()
