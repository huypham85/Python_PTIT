
import math
def nhan(a,b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

def kc(a):
    res = 0
    for i in a:
        res += i**2
    return math.sqrt(res)

def solve(a,b):
    return nhan(a,b)/(kc(a) * kc(b))

if __name__ == "__main__":
    t = int(input())
    n = int(input())
    if t<4 or t>1024:
        print("INVALID INPUT")
    else:
        a = [float(x) for x in input().split()] 
        res = []
        name = ""
        max_similar = 0.0
        while t>3:
            t-=1
            nhap = input().split()
            b = [float(x) for x in nhap[1:]]
            x = round(solve(a,b),4)
            if max_similar <x:
                max_similar = x
                name = nhap[0]
            res.append(x)
        print(name,res)