import math
t = int(input())


def check(k):
    if k<2: return False
    for i in range(2, int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

def Solve(x):
    n = x[-4:]
    if check(int(n)): return True
    else: return False

while t>0:
    s = input()
    if Solve(s): print("YES")
    else: print("NO")
    t-=1

