t = int(input())
while t > 0:
    n = int(input())
    if n % 2 == 0:
        sum = 0
        for i in range(2, n+1, 2):
            sum += float(1/i)
    else:
        sum = 0
        for i in range(1, n+1, 2):
            sum += float(1/i)
    print("{:.6f}".format(sum))
    t -= 1
