import math
t = int(input())

def Sum(x):
    sum=0
    for i in x:
        sum+=int(i)
    return sum

def Check(x):
    if x<2: return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0: return False
    return True

while t>0:
    s = input()
    dao = Sum(s)
    #print(dao)
    if Check(dao):
        print("YES")
    else: print("NO")
    t-=1

