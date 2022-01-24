a = list()

while len(a)<10:
    b = [int(i) for i in input().split()]
    for i in b:
        a.append(i)
    #print(a, len(a))
    
for i in range(len(a)):
    a[i] = a[i]%42
myset = set(a)

print(len(myset))