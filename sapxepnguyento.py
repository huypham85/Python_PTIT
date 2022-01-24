import math


def check(k):
    if k < 2:
        return False
    for i in range(2, int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
prime = []
for i in a:
    if check(i):
        prime.append(i)
prime.sort()
index = 0  # index of prime array
for i in range(n):
    if check(a[i]):
        print(prime[index], end=' ')
        index += 1
    else:
        print(a[i], end=' ')
