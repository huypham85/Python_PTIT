from math import cos, sin, asin, sqrt

def haversine(lat1, long1, lat2, long2):
      R = 6371
      dLat = (lat2 - lat1)
      dLon = (long2 - long1)
      a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
      c = 2*asin(sqrt(a))
      return R * c

long1,lat1 = map(float,input().split())
long2,lat2 = map(float,input().split())

print("%.2f" %haversine(lat1, long1, lat2, long2))