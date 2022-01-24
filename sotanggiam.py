t = int(input())
def check_len(n):
    if len(n) < 3: return False
    return True
def check_suitable(x,pivot):
    for i in range(0, pivot):
        if int(x[i]) >= int(x[i+1]): return False
    for i in range(pivot, len(x)-1):
        if int(x[i]) <= int(x[i+1]): return False
    return True

while t>0:
    x = input()
    ok = False
    for i in range(0,len(x)):
        if check_len(x) == True and check_suitable(x,i):
            print("YES")
            ok = True
            break
    if ok == False: print("NO")
    t-=1
        

