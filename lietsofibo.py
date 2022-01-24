t = int(input())
f=[]
def fibo():
    f.append(0)
    f.append(1)
    for i in range(2,93):
        f.append(0)
        f[i] = f[i-1] + f[i-2]

while t>0:
    fibo()
    a,b = map(int, input().split())
    for i in range(a,b+1):
        print(f[i],end=" ")
    print()
    t-=1