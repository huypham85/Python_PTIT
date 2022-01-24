import re
t = int(input())
while t>0:
    list = input().split(',')
    for i in list:
        if re.search("[a-z]",i)!=None and re.search("[0-9]",i)!=None and re.search("[A-Z]",i)!=None and re.search("[$#@]",i)!=None and len(i)>=6 and len(i)<=12:
            print(i)
    t-=1
