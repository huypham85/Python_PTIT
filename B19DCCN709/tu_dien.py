k = int (input())
sum1 = 0
tich = 1
if k > 10:
    print('INVALID INPUT')
else:
    for i in range(k):
        s = input().split()

        if s[1].isdigit():
            sum1 += int(s[1])

            tich *= int(s[1])

    print(sum1, tich)
