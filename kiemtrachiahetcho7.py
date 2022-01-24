import math
t = int(input())
while t>0:
    a = int(input())
    res = a
    i=0
    while(i<=1000 and res %7!=0):
        i+=1
        res += int(str(res)[::-1])
        # print(res)
    if i>1000: res = -1
    print(res)
    t-=1