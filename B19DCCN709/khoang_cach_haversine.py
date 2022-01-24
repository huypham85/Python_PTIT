from decimal import Decimal
import math



long1, lat1 = map(Decimal, input().split())
long2, lat2 = map(Decimal, input().split())
R = 6371
dlat = lat2 - lat1
dlong = long2 - long1
a = math.sin(dlat / 2) ** 2 + math.cos(lat1)*math.cos(lat2)*(math.sin(dlong / 2) ** 2) 
c = 2 * math.asin(math.sqrt(a))
d = R * c

print('{:.2f}'.format(d))