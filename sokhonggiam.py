t = int(input())

def check(s):
    for i in range(0,len(s)-1): #loop from 0 to len(s)-1
        if (s[i]>s[i+1]): return False
    return True

while (t>0) :
    s = input()
    if (check(s)) : print("YES")
    else : print("NO")
    t -=1


