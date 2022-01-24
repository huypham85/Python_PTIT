t = int(input())

def Mul(x):
    res=1
    for i in x:
        if i!='0':
            res*=int(i)
    return res

while t>0:
    s = input()
    print(Mul(s))
    t-=1

