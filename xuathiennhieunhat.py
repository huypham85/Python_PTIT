t = int(input())
while t>0 :
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    res = 0
    index = 0
    for i in range(n):
        cnt =a.count(a[i])
        if cnt > res :
            res = cnt
            index = i
        if res > (n/2):
            break
    if res > n/2 :
        print(a[index])
    else : print("NO")
    t-=1