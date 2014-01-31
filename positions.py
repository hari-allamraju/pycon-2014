import redis
import simplejson as json

#the database
db=redis.Redis()

#the positions
positions=[
{'name':'pos_1','size':100,'price':0.99},
{'name':'pos_2','size':100,'price':0.91},
{'name':'pos_3','size':100,'price':0.85},
{'name':'pos_4','size':100,'price':0.96},
{'name':'pos_5','size':100,'price':0.79}
]

def create_positions():
    for position in positions:
        db.set(position['name'],json.dumps(position))
        
if __name__=="__main__":
    create_positions()
    print json.loads(db.get('pos_1'))
