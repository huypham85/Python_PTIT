import re
t,k = map(int,input().split())
list = []
while t>0:
    s = input()
    list.extend(re.findall("\w+",s))
    t-=1
dict ={}
for i in list:
    if i.lower() not in dict:
        dict[i.lower()] = 1
    else: dict[i.lower()] +=1
res = sorted(dict.items(), key=lambda x:(-x[1],x[0]))
# print(res)
for i in res:
    if i[1]>=k:
        print(i[0],i[1])

