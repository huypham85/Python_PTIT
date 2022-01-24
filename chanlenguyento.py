import math
t = int(input())

def Sum(x):
    sum=0
    for i in x:
        sum+=int(i)
    return sum

def check(k):
    if k<2: return False
    for i in range(2, int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

def Solve(x):
    if check(Sum(x)) == False: return False
    for i in range(0,len(x)):
        if (i%2==0 and int(x[i])%2==1) or (i%2==1 and int(x[i])%2==0): return False
        
    return True

while t>0:
    s = input()
    if Solve(s): print("YES")
    else: print("NO")
    t-=1

