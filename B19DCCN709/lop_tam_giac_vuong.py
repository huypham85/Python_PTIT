import math
from decimal import ROUND_HALF_UP, Decimal

class TamGiac():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def chuvi(self):
        return self.a + self.b + self.c
    def dientich(self):
        p = self.chuvi()
        dt = (p - 2 * self.a)*(p - 2* self.b) * (p - 2 * self.c) * p
        dt = dt / Decimal(16)

        return Decimal(math.sqrt(dt))
    def printf(self):
        tmp = max(self.a, self.b, self.c)
        s = self.a + self.b + self.c 
        if s - tmp <= tmp:
            print('INVALID')
        else: print(self.chuvi(), self.dientich().quantize(Decimal('1'), ROUND_HALF_UP))
    

a, b, c = map(Decimal, input().split())

TamGiac(a, b, c).printf()