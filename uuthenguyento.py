import math
t = int(input())


def check(k):
    if k<2: return False
    for i in range(2, int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

def Solve(x):
    if check(len(x)) == False: return False
    cnt_nt , cnt =0,0
    for i in range(0, len(x)):
        if check(int(x[i])): cnt_nt+=1
        else: cnt+=1
    if cnt >= cnt_nt: return False
    return True
    

while t>0:
    s = input()
    if Solve(s): print("YES")
    else: print("NO")
    t-=1

