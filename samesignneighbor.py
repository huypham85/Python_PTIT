n = int(input())
list = [int(x) for x in input().split()]
cnt = 0
for i in range(len(list)-1):
    if (list[i] > 0 and list[i+1] > 0) or (list[i] < 0 and list[i+1] < 0):
        cnt+=1
print(cnt,end=" ")
for i in range(len(list)-1,0,-1):
    if (list[i] > 0 and list[i-1] > 0) or (list[i] < 0 and list[i+-1] < 0):
        print(list[i-1],list[i])
        break
