import math

listPrime = list()
def check(k):
    if k<2: return False
    for i in range(2, int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

def sieve():
    for i in range(2,10000):
        if check(i):
            listPrime.append(i)
        if len(listPrime) > 1001:
            return

n,x = map(int,input().split())
sieve()
print(x, end=' ')
tmp = x
for i in range(0,n):
    tmp += listPrime[i]
    print(tmp, end=' ')
