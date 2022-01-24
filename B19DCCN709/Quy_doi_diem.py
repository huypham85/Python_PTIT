from decimal import ROUND_HALF_UP, Decimal

def printf(name, diemchu, xl):
    print(name)
    print(diemchu)
    print(xl)

name = input().strip().lower().split()

name = ' '.join(name).title()

diem = Decimal(input()) * Decimal('0.1')

diem += Decimal(input()) * Decimal('0.1')
diem += Decimal(input()) * Decimal('0.2')
diem += Decimal(input()) * Decimal('0.6')

diem = diem.quantize(Decimal('0.1'), ROUND_HALF_UP)

if diem >= 8.5:
    printf(name, 'A', 'Giỏi')
elif diem >= 7.0:
    printf(name, 'B', 'Khá')

elif diem >= 5.5:
    printf(name, 'C', 'Trung bình')
elif diem > 4.0:
    printf(name, 'D', 'Trung bình kém')
else:
    printf(name, 'F', 'Kém')

'''
Nguyen Van Hung
10
7
6.5
7
'''