import re
n = int(input())
listNum=[]
while n>0:
    s = input()
    num = re.findall(r'\d+', s)
    for i in num:
        newNum = int(i)
        listNum.append(newNum)
    n-=1
listNum.sort()
for i in listNum:
    print(i)
