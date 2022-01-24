t = int(input())

while t>0:
    n = int(input())
    a = [int(i) for i in input().split()]
    set1 = set(a)
    for i in set1:
        tmp = a.count(i)
        if tmp%2==1:
            print(i)
            break
    t-=1 