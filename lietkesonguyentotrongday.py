import math
def check(k):
    if k<2: return False
    for i in range(2, int(math.sqrt(k))+1):
        if k%i==0: return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
set1 = sorted(set(a),key=a.index) # cho cac phan tu vao set va sort theo thu tu la index trong a
for i in set1:
    if check(i):
        print(i, a.count(i))