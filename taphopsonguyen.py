n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
setA = set(a)
setB = set(b)
#print(setA)
list1 = list(setA.intersection(setB))
list2 = list(setA.difference(setB))
list3 = list(setB.difference(setA))
for i in sorted(list1):
    print(i, end=' ')
print()
for i in sorted(list2):
    print(i, end=' ')
print()
for i in sorted(list3):
    print(i, end=' ')
print()