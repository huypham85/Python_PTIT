s = input()
sum = 0
for i in s:
    if (i!='+' and i!=' ' and i!='='):
        sum += int(i)
sum -= int(s[8])
if sum == int(s[8]): print("YES")
else: print("NO")