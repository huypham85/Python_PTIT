n = int(input())
a = [int(i) for i in input().split()]
res =0
for i in range(len(a)-1):
    if a[i] !=a[i+1]:
        res +=1
print(res)
