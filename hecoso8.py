import math
s = input()

def convert(x):
    ans  = 0
    x = x[::-1]
    for i in range(len(x)):
        if x[i]=='1':
            ans += int(math.pow(2,int(i)))
    return ans


while (len(s))%3!=0:
    s = "0"+s
n = len(s)
res=""
for i in range(n):
    if i>0 and (i+1)%3==0:
        a = s[i-2:i+1]
        res+=str((convert(a)))
#print(res)
print(res.lstrip('0'))