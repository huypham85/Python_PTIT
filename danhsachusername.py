t = int(input())
list = []
while t>0:
    s = input().lower()
    list.append(s)
    t-=1
Set = set(list)
newList = []
for i in Set:
    newList.append(i)
newList.sort()
for i in newList:
    print(i)

