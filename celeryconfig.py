import os
import sys

sys.path.insert(0, os.getcwd())

CELERY_BACKEND = 'redis'
BROKER_URL = 'redis://localhost:6379'
CELERY_DISABLE_RATE_LIMITS = True
CELERY_ENABLE_UTC = True
CELERYD_CONCURRENCY = 10
