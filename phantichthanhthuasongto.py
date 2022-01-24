import math

t = int(input())
while t>0:
    n = int(input())
    print("1", end=' ')
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            dem = 0
            while n%i==0:
                n/=i
                dem+=1
            print("{}{}{}{}".format("* ",i,"^",dem), end=' ')
    if n>1 :
        print("{}{}{}{}".format("* ",int(n),"^",1))
    if n == 1: print()
    t-=1
