from celery import Celery

celery = Celery('tut1',broker='redis://')

@celery.task
def add(a,b):
    print a+b

