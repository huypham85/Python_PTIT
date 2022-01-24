def check(s):
    n = len(s)
    s1 = s[::-1]
    if s!=s1: return False
    for i in range(0, n):
        if int(s[i])%2==1: return False
    # if n%2==1: return False
    return True

t = int(input())
while t>0:
    n = int(input())
    for i in range(22,n):
        if(i%2==0 and len(str(i))%2==0 and check(str(i))):
            print(i, end=' ')
    print()
    t-=1
    