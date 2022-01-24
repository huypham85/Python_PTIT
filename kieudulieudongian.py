import math
t = int(input())
res = 1
while t>0:
    sum = 0
    n = int(input())
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0 :
            while n%i==0 :
                n/=i
                sum+=i
    if n >1: sum+=n
    res*=sum
    t-=1
print(int(res))


