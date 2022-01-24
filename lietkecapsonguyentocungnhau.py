import math
n = int(input())

list = [int(i) for i in input().split()]
ok = False
list = sorted(list)
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if math.gcd(list[j],list[i])==1 and list[j] != list[i]: 
            print(list[i],list[j])
            ok = True
if ok == False: print("-1")