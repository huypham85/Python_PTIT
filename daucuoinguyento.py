import math
t = int(input())


def check(k):
    if k<2: return False
    for i in range(2, int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

def Solve(x):
    s1 = int(x[:3].lstrip('0'))
    s2 = int(x[-3:].lstrip('0'))
    if check(s1) and check(s2): return True
    else: return False

while t>0:
    s = input()
    if Solve(s): print("YES")
    else: print("NO")
    t-=1

