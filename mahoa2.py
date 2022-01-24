P= "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    s = [str(i) for i in input().split()]
    k = int(s[0])
    if k == 0: break
    a = s[1]
    res =""
    for i in range(len(a)):
        index = P.find(a[i])
        res += P[(index+k)%28]
    list1 = list(res)
    list1.reverse()
    list1 = ''.join(list1)
    #res.reverse()
    print(list1)
