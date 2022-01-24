t = int(input())

def cmp(x):
    s = str(x)
    sum =0
    for i in s:
        sum+=int(i)
    return sum,x

while t>0:
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in sorted(a, key=cmp):
        print(i, end=' ')
    print()
    t-=1