from decimal import Decimal
from math import sqrt

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self, p2):
        resx = abs(self.x - p2.x)
        resy = abs(self.y - p2.y)
        res = sqrt(resx**2 + resy**2)
        return res
    def Point(self,x,y):
        self.x = x
        self.y = y



t = int(input())
if t > 10:
    print("INVALID INPUT")
else:
    while t>0:
        arr = [int(i) for i in input().split()]
        p1 = Point(Decimal(arr[0]),Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]),Decimal(arr[3]))
        p3 = Point(Decimal(arr[4]),Decimal(arr[5]))
        a = p1.distance(p2)
        b = p1.distance(p3)
        c = p2.distance(p3)
        
        if (a+b)>c and (a+c)>b and (b+c)>a:
            cvi = a+b+c
            print('{:.3f}'.format(cvi))
        else:
            print("INVALID")
        t -= 1