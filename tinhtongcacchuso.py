t = int(input())

while t>0:
    s = input()
    list1 = list(s)
    list1.sort()
    res = 0
    for i in list1:
        if i.isdigit(): res += int(i)
        else: print(i,end='')
    print(res)
    t-=1