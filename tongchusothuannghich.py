t = int(input())

def Sum(x):
    sum=0
    for i in x:
        sum+=int(i)
    return sum

while t>0:
    s = input()
    dao = str(Sum(s))
    #print(dao)
    if len(dao)>1 and dao[::-1] == dao:
        print("YES")
    else: print("NO")
    t-=1

