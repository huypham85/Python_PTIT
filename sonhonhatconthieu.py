t = int(input())
a = [int(i) for i in input().split()]
a.sort()
minn = a[0]
maxx = a[t-1] 
dd = 1
for i in range(1, maxx):
    if a.count(i) == 0:
        print(i)
        dd=0
        break
if dd == 1: print(maxx+1)

