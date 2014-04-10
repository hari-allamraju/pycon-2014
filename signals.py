from celery import Celery
from celery.signals import *

celery = Celery('tut2',broker='redis://',backend='redis://')

@celery.task
def add(a,b):
    print a+b


@celery.task
def mult(a,b):
    return a*b 


@after_task_publish.connect
def task_sent_handler(sender=None, body=None, **kwargs):
    print('after_task_publish for task id {body[id]}'.format(
        body=body,
    ))