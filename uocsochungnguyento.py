import math

t = int(input())

def check(k):
    if k<2: return False
    for i in range(2, int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

while t>0:
    a,b = map(int, input().split())
    k = math.gcd(a,b)
    k = str(k)
    res =0
    for i in k:
        res += int(i)
    if check(res): print("YES")
    else: print("NO")
    t-=1
