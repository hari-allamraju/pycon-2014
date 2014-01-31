import pnl
from celery import chain,group
import time

#independent tasks in parallel
res=group(pnl.get_pnl.si('pos_%s'%(i,), 0.95) for i in range(1,6))()
print res.ready()
print res.get(timeout=1)

#like a chain, but stil independent tasks
res1=chain(pnl.get_pnl.si('pos_1', 0.95),pnl.get_pnl.si('pos_2', 0.95),pnl.get_pnl.si('pos_3', 0.95))()
print res1.get()
print res1.parent.get()
print res1.parent.parent.get()

#chain of sub tasks addig up the result
s1=pnl.get_pnl.delay('pos_1', 0.95)
s2=pnl.get_pnl.delay('pos_2', 0.95)
s3=pnl.get_pnl.delay('pos_3', 0.95)

#just wait a few secs
time.sleep(5)

print s1.result,s2.result,s3.result

res2=chain(pnl.add_pnl.s(0,s1.result),pnl.add_pnl.s(s2.result),pnl.add_pnl.s(s3.result))()
print res2.get()
print res2.parent.get()
print res2.parent.parent.get()

