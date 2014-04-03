import eurofx
import redis

db = redis.Redis()

print "getting historical fx data"
data = eurofx.get_historical_data()

for i,j,k in data:
    date_str = str(j)
    print "processing data for %s %s"%(i,date_str)
    db.lpush(i,k)
    
print db.llen('JPY')
print db.lindex('JPY',200)