import math
n, k = map(int, input().split())
minn = int(pow(10, k-1))
maxx = int(pow(10, k))
cnt =0
for i in range(minn, maxx):
    if math.gcd(n,i) == 1:
        cnt+=1
        if cnt == 10:
            print(i)
            cnt = 0
        else:
            print(i,end=' ')