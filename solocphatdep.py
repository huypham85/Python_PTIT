def Sum(s):
    sum=0
    for i in s:
        sum += int(i)
    return sum

def check(s):
    if s[0] !='6':
        print("NO")
        return
    for i in range(1,len(s)-1):
        if s[i] == '8':
            if Sum(s[i-1:i+2])>=24:
                print("NO")
                return
        if s[i] !='6' and s[i] != '8':
            print("NO")
            return
    print("YES")

s = input()
check(s)