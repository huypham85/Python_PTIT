import math


def tinh(l1, l2):
    tu = 0
    mau1 = 0
    mau2 = 0
    for i in range(len(l1)):
        tu += l1[i] * l2[i]
        mau1 += (l1[i] ** 2)
        mau2 += (l2[i] ** 2)
    mau = math.sqrt(mau1 * mau2)
    return '{:.4f}'.format(tu / mau)

n = int(input())
m = int(input())
if n > 1024 or n < 4:
    print('INVALID INPUT')
else: 
    tmp = [float(i) for i in input().split()]
    maxx = 0 
    ls = []
    resn = ''
    for i in range(n - 3):
        s = input().split()
        name = s[0]
        dd = []
        for j in range(1, len(s)):
            dd.append(float(s[j]))
        
        res = float(tinh(dd, tmp))
        if res > maxx:
            maxx = res
            resn = name 
        ls.append(res)
    print(resn, ls)
