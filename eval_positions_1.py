import simplejson as json
from celery import Celery
from celery.utils.log import get_task_logger
import redis

celery=Celery('positions',broker='redis://',backend='redis://')
logger = get_task_logger(__name__)

@celery.task
def get_initial_position_value(name):
    db=redis.Redis()
    pos=json.loads(db.get(name))
    if pos is None:
        return
    else:
        return pos['size']*pos['price']
    

@celery.task
def get_value_at_close(name,close):
    if close is None or close<0:
        return None
    db=redis.Redis()
    pos_str=db.get(name)
    if pos_str is None:
        return None
    else:
        pos=json.loads(pos_str)
        return pos['size']*close
    
@celery.task
def get_value_at_close_retry(name,close):
    if close is None or close<0:
        return None
    db=redis.Redis()
    pos_str=db.get(name)
    if pos_str is None:
        raise get_value_at_close_retry.retry()
    else:
        pos=json.loads(pos_str)
        return pos['size']*close

