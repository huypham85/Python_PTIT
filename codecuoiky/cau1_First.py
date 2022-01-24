t = int(input())
while t>0:
    t -= 1
    s = input().lower()
    res = []
    for i in range(len(s)):
        if s[i] == 't':
            res.append(i)
    if len(res) == 0:
        print(-1)
    elif len(res) == 1:
        print(res[0])
    else:
        print(res[0],res[1],res[-1])