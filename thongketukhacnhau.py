import re
t = int(input())
list = []
while t>0:
    s = input()
    list.extend(re.findall("\w+",s))
    t-=1
dict = {}
for i in list:
    if len(i) == 0: continue
    if i.lower() not in dict:
        dict[i.lower()] = 1
    else: dict[i.lower()] +=1
res = sorted(dict.items(), key=lambda x: (-x[1],x[0])) #dict.items return a list of tuple,key=lambda x: (x[1],x[0]) means priority compare for value
for i in res:
    print(i[0]+" "+str(int(i[1])))

