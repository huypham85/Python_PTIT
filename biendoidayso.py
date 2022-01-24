def check(lis1):
    n = len(lis1)
    for i in range(n-1):
        if lis1[i] != lis1[i+1]:
            return False
    return True

while True:
    a = [int(i) for i in input().split()] 
    if a == [0,0,0,0]:
        break
    dem = 0
    #print(a)
    while check(a) == False:
        dem +=1
        tmp = a[0]
        for i in range(0,3):
            a[i] = abs(a[i]-a[i+1])
        a[3] = abs(a[3]-tmp)
        #print(a)
    print(dem)