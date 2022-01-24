n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
set1 = set(a) 
set2 = set(b) 
dd=0
for i in set1:
    if b.count(i)==0: dd=1
if len(set1) == len(set2) and dd == 0:
    print("YES")
else:
    print("NO")