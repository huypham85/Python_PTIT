t = int(input())
import math
def check(s):
    if int(s)<2: return False
    for i in range(2, int(math.sqrt(int(s)))+1):
        if int(s)%i==0: return False
    return True
while t>0:
    s = input()
    if len(s)>=4: s = s[-4:]
    if check(s):print("YES")
    else: print("NO")
    t-=1