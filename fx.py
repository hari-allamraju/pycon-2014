import pnl
from celery import chain,group
import time
import redis

db = redis.Redis()

print db.lrange('JPY',-10,-1)

#independent tasks in parallel
for item in db.lrange('JPY',-10,-1):
    price = float(item)
    print price
    res=group(pnl.get_pnl.si('pos_%s'%(i,), price) for i in range(1,6))()
    print res.ready()
    print res.get(timeout=1)

#like a chain, but stil independent tasks
for item in db.lrange('JPY',-10,-1):
    price = float(item)
    res1=chain(pnl.get_pnl.si('pos_1', price),pnl.get_pnl.si('pos_2', price),pnl.get_pnl.si('pos_3', price))()
    print res1.get()
    print res1.parent.get()
    print res1.parent.parent.get()