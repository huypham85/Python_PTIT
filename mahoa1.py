t = int(input())
while t > 0:
    t -= 1
    s = input()
    n = len(s)
    i = 0
    while True:
        dem = 1
        while i < n -1 and s[i] == s[i+1]:
            dem += 1
            i += 1
        print("{}{}".format(dem,s[i]),end="")
        i += 1
        if i == n:
            break 
    print('')