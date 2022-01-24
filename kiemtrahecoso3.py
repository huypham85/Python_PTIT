t = int(input())
def check(s):
    Set = set(s)
    if len(Set)>3: return False
    for i in Set:
        if int(i)!=0 and int(i)!=1 and int(i)!=2: return False
    return True
while t>0:
    s = input()
    if check(s):print("YES")
    else: print("NO")
    t-=1