def solve():
    x = int(input())
    if x > 365:
        print('INVALID INPUT')
        return
    if x < 11:
        print(0)
        return
    tmp = x // 11
    kq = 2 ** tmp - 1
    print(kq)
T = int(input())

check = True
if T > 10 or T < 0:
    print('INVALID INPUT')
    check = False
while T > 0:
    T -= 1
    if check:
        solve()

'''
5
7
380
18
113
30
'''