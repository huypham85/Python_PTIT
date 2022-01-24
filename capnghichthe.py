n = int(input())

list1 = [int(i) for i in input().split()]

res = 0
for i in range(n):
    for j in range(i+1,n):
        if(list1[i]>list1[j]): res+=1
print(res)
