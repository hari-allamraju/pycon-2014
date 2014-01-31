from celery import Celery

celery = Celery('tut2',broker='redis://',backend='redis://')

@celery.task
def add(a,b):
    print a+b


@celery.task
def mult(a,b):
    return a*b 
