list1 = [int(i) for i in input().split()]
a = list1[0]
k = list1[1]
n = list1[2]
res = []
i=k
while i <= n:
    if i>a:
        res.append(i-a)
    i+=k
if len(res) == 0: print("-1")
else:
    for i in res:
        print(i, end=' ')
    