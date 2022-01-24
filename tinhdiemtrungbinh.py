import math

n = int(input())
a = [float(i) for i in input().split()]
maxx = max(a)
minn = min(a)
b = [i for i in a if i!=maxx and i!=minn]
print("{:.2f}".format(sum(b)/len(b)))