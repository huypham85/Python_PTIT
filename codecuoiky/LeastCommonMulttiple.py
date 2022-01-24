from math import gcd

t = int(input())
if t>10:
    print("INVALID INPUT")
else:     
    while t>0:
        t -= 1
        a,b = map(int, input().split())
        
