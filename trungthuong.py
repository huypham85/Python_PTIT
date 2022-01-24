t = int(input())
while t>0:
    n = int(input())
    list1 = []
    for i in range(0,n):
        tmp = int(input())
        list1.append(tmp)
    list1.sort()
    set1 = sorted(set(list1), key=list1.index)
    print(set1)
    res =0
    maxCount =0
    for i in set1:
        if list1.count(i)>maxCount :
            res = i
            maxCount = list1.count(i)
    print(res)
    t-=1

