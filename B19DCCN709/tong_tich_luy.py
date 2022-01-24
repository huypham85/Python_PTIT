from decimal import Decimal


n = int (input())

A = [Decimal(i) for i in input().split()]

B = [0]

for i in A:
    B.append(B[-1] + i)
tong = 0
tich = 1
for i in range(1, len(B)):
    tong += B[i]
    tich *= B[i]

print(tong, tich)