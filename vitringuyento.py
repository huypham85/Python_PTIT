import math
t = int(input())


def check(k):
    if k<2: return False
    for i in range(2, int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

def Solve(x):
    for i in range(0,len(x)):
        if (check(i)==True and check(int(x[i]))==False) or (check(i)==False and check(int(x[i]))==True): return False
        
    return True

while t>0:
    s = input()
    if Solve(s): print("YES")
    else: print("NO")
    t-=1

