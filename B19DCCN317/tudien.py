t = int(input())
dict = {}
sum = 0
res = 1
if t>10: print("INVALID INPUT")
else:
    while t>0:
        a,b= input().split()
        if b.isdigit():
            sum += int(b)
            res *= int(b)
        t-=1
    print(sum,res)
