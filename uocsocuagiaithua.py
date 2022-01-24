t = int(input())

while t>0:
    n, p = map(int , input().split())
    res =0
    while n>0:
        n = n//p
        res +=n
    print(res)
    t-=1