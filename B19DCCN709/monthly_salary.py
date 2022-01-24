
from tabnanny import check


def solve():
    m, n = map(float, input().split())
    if m < 1000 or n < 1000:
        print('INVALID INPUT')
        return
    tienbh = (8 + 1.5 + 1) * n / 100
    dp = 0.01 * n 
    ckt = 11000000
    TNCN = m + ckt + tienbh
    thue = TNCN
    if TNCN <= 5000000:
        thue *= 0.05
    elif TNCN <= 10000000:
        thue *= 0.1
        thue -= 250000
    elif TNCN <= 18000000:
        thue *= 0.15
        thue -= 750000
    elif TNCN <= 32000000:
        thue *= 0.2 
        thue -= 1650000
    elif TNCN <= 80000000:
        thue *= 0.3
        thue -=  5850000
    else:
        thue *= 0.35
        thue -= 9850000
    kq = tienbh + dp + thue 
    print(int(m - kq))

T = int (input())
check = True
if T > 10 or T < 0:
    print('INVALID INPUT')
    check = False
while T > 0:
    T -= 1
    if check:
        solve()
