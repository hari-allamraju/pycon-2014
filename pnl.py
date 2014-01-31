import simplejson as json
from celery import Celery
from celery.utils.log import get_task_logger
import redis

celery=Celery('positions',broker='redis://',backend='redis://')
logger = get_task_logger(__name__)

@celery.task
def get_pnl(name,close):
    if close is None or close<0:
        return None
    db=redis.Redis()
    pos_str=db.get(name)
    if pos_str is None:
        return None
    else:
        pos=json.loads(pos_str)
        current = pos['size']*close
        initial = pos['size']*pos['price']
        return current-initial    

@celery.task
def add_pnl(val1=0,val2=0):
    return val1+val2


@celery.task
def add_list(values):
    result=0
    for value in values:
        result+=value
    return result

