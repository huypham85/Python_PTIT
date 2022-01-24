t = int(input())

def check(s):
    for i in s:
        if i!='4' and i!='7': return False
    return True

while t>0 :
    s = input()
    if check(s):
        print("YES")
    else: print("NO")
    t-=1