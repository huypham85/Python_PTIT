t = int(input())

def check_sum(s):
    sum = 0
    n = len(s)
    for i in range(n):
        sum += int(s[i])
    #print(sum)
    if sum % 10 == 0: return True
    else: return False

def check_relative(s):
    n = len(s)
    for i in range(0, n-1):
        if abs(int(s[i])-int(s[i+1])) != 2 : return False
    return True

while t>0 :
    s = input()
    if check_sum(s) and check_relative(s):
        print("YES")
    else: print("NO")
    t-=1