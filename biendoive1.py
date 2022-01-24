while True:
    n = int(input())
    list1 = [n]
    if n == 0: break
    while(n!=1):
        if n%2==0:
            n/=2
            list1.append(n)
        else:
            n = n*3+1
            list1.append(n)
    print(len(list1))