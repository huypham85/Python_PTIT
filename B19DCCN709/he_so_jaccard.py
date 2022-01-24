import re


def heSoJaccard(list1 , list2):
    s1 = set(list1)
    s2 = set(list2)
    
    return len(s1.intersection(s2))/len(s1.union(s2))

l1 = input().lower()
l2 = input().lower()
s1 = re.sub(r'[^\w]','',l1)
s2 = re.sub(r'[^\w]','',l2)


if len(s1) == 0 or len(s2) == 0 :
    print('1.00')
else : print("{:.2f}".format(heSoJaccard(s1,s2)))

'''
hom nay thi lap trinh python
Lap trinh Python.

Hom qua troi mua.
Hom qua mua, ngay mai co nang khong?
'''