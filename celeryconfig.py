from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tut1.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
}
