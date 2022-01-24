from decimal import Decimal
import math
class Point:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def distance(self,point):
        return "{:.4f}".format(math.sqrt((self.start - point.start)**2 + (self.end - point.end)**2),4)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1