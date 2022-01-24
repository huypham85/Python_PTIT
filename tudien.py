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
for i in dict:
    dict[i] = dict[i]/len(list)
res = sorted(dict.items(), key=lambda x: (-x[1],x[0]))
for i in res:
    print("%s %.2f"%(i[0],i[1]))
