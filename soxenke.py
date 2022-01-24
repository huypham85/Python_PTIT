t = int(input())

def Check(x):
    if len(x)%2==0: 
        #print("here1")
        return False
    if x[0] == x[1]:
        #print("here2") 
        return False
    for i in range(2,len(x),2):
        if x[i] != x[0]:
            #print("here3")
            return False
    return True

while t>0:
    s = input()
    if Check(s): print("YES")
    else: print("NO")
    t-=1

