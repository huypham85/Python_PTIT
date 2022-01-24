t = int(input())
while t>0:
    n,x,m = map(float, input().split())
    cnt =0
    while n<m:
        cnt+=1
        n = n + n*(x/100.0)
    print(cnt)
    t-=1
