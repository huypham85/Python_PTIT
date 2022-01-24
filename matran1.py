import math

n = int(input())
a = [[float(i) for i in input().split()] for j in range(n)]
k = int(input())
start = 1
sumUp, sumDown = 0,0
for i in range(0,n-1):
    for j in range(start,n):
        sumUp +=a[i][j]
    start+=1
end = 1
for i in range(1,n):
    for j in range(0,end):
        sumDown +=a[i][j]
    end+=1
#print(sumUp,sumDown)
if abs(sumUp-sumDown) <= k:
    print("YES")
    print(int(abs(sumUp-sumDown)))
else:
    print("NO")
    print(int(abs(sumUp-sumDown)))