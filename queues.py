import simplejson as json
from celery import Celery
from celery.utils.log import get_task_logger
import redis

celery=Celery('positions',broker='redis://',backend='redis://')
logger = get_task_logger(__name__)

@celery.task(queue='priority_queue')
def get_initial_position_value(name):
    db=redis.Redis()
    pos=json.loads(db.get(name))
    return pos['size']*pos['price']
    

@celery.task(queue='priority_queue')
def get_value_at_close(name,close):
    db=redis.Redis()
    pos=json.loads(db.get(name))
    return pos['size']*close
    
@celery.task(queue='priority_queue')
def get_value_at_close_1(name,close):
    db=redis.Redis()
    pos=json.loads(db.get(name))
    logger.info('Calculating value with close price %s'%(close,))
    return pos['size']*close

