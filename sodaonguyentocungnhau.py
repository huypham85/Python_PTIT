import math
t = int(input())

while t>0:
    n = input()
    dao = n[::-1]
    if math.gcd(int(n), int(dao)) == 1: print("YES")
    else: print("NO")
    t-=1 