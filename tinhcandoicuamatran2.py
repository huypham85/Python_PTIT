import math

n = int(input())
a = [[float(i) for i in input().split()] for j in range(n)]
k = int(input())
lim = n-1
sumUp, sumDown = 0,0
for i in range(n-1):
    for j in range(lim):
        sumUp +=a[i][j]
    lim-=1
lim = n-1
for i in range(1,n):
    for j in range(lim,n):
        sumDown +=a[i][j]
    lim-=1
#print(sumUp,sumDown)
if abs(sumUp-sumDown) <= k:
    print("YES")
    print(int(abs(sumUp-sumDown)))
else:
    print("NO")
    print(int(abs(sumUp-sumDown)))