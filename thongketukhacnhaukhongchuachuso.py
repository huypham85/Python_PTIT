import re
t= int(input())
list = []
while t>0:
    s = input()
    list.extend(re.findall("[a-zA-Z]+",s))
    t-=1
dict ={}
for i in list:
    if i.lower() not in dict:
        dict[i.lower()] = 1
    else: dict[i.lower()] +=1
res = sorted(dict.items(), key=lambda x:(-x[1],x[0]))
# print(res)
for i in res:
    print(i[0],i[1])
