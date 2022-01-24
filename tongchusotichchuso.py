import math
t = int(input())


def Solve(x):
    sum=0
    mul=1
    dd=0
    for i in range(len(x)):
        if i%2==0:
            sum+=int(x[i])
        else:
            if x[i]!='0':
                dd=1
                mul*= int(x[i])
    if dd==0: mul=0
    print(sum, mul)   

while t>0:
    s = input()
    Solve(s)
    t-=1

