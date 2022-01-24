t = int(input())
while t>0 :
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    dd = 0
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            dd=1
            break
    if dd == 0: print("YES")
    t-=1