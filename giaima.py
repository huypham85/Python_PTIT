def solve(s):
    res=""
    for i in range(len(s)):
        if(s[i].isdigit()):
            for j in range(0, int(s[i])):
                #print(s[i-1])
                res+=s[i-1]
    print(res)

t = int(input())
while(t>0):
    s = input()
    solve(s)
    t-=1
