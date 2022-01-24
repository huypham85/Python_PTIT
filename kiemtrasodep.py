t = int(input())
def check(s):
    Set = set(s)
    # print(s)
    if len(Set) >2: return False
    for i in range(len(s)-2):
        if(s[i] != s[i+2]): return False
    return True
while t>0:
    s = input()
    if check(s): print("YES")
    else: print("NO")
    t-=1