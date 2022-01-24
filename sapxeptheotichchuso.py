t = int(input())

def cmp(x):
    s = str(x)
    mul =1
    for i in s:
        mul*=int(i)
    return mul,x

while t>0:
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in sorted(a, key=cmp):
        print(i, end=' ')
    print()
    t-=1