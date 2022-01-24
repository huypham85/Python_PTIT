import math

t = int(input())


def check(k):
    if k<2: return False
    for i in range(2,int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

while t>0:
    n = int(input())
    dem = 0
    for i in range(1,n):
        if math.gcd(i,n) ==1: dem += 1
    if check(dem):
        print("YES")
    else:
        print("NO")
    t-=1