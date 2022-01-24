t = int(input())
list = []
while t>0:
    s = input()
    list.extend(s.split(' '))
    t-=1
dict = {}
for i in list:
    if len(i) == 0: continue
    if i.lower() not in dict:
        dict[i.lower()] = 1
    else: dict[i.lower()] +=1
res = sorted(dict.items(), key=lambda x: (-x[1],x[0]))
cnt = int(res[0][1])
# print(cnt)
tmp =0
for i in res:
    # print(int(i[1]))
    if int(i[1])<cnt:
        tmp = int(i[1])
        break
ans =[]
for i in reversed(res):
    if int(i[1])==tmp:
        ans.append(i[0])
ans.sort()
for i in ans:
    print(i,end=' ')
