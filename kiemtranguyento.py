import math

listPrime = list()
def check(k):
    if k<2: return False
    for i in range(2, int(math.sqrt(k))+1):
        if k%i==0: return False
    return True

row, col = map(int, input().split())
a = [[int(i) for i in input().split()] for j in range(row)]
for i in range(row):
    for j in range(col):
        if check(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0
for i in range(row):
    for j in range(col):
        print(a[i][j], end=' ')
    print()