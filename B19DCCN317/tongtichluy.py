n = int(input())
list = [int(x) for x in input().split()]
res = []
res.append(list[0])
for i in range(1,len(list)):
    tmp = 0
    for j in range(0,i+1):
        tmp+=list[j]
    res.append(tmp)
# print(res)
sum =0
mul =1
for i in res:
    sum += i
    mul *= i
print(sum,mul)