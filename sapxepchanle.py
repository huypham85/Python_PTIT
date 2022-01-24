n = int(input())
listTmp = []
cnt = 0
while cnt < n:
    arr = [int(x) for x in input().split()]
    listTmp.extend(arr)
    cnt += len(arr)
list = []
list.extend(listTmp)
le = []
chan = []
for i in listTmp:
    if i % 2 == 0:
        chan.append(i)
    else: le.append(i)
chan.sort()
le.sort(reverse=True)
i ,j= 0,0
for x in listTmp:
    if x % 2 == 0: 
        print(chan[i], end=' ')
        i+=1
    else: 
        print(le[j], end=' ')
        j+=1