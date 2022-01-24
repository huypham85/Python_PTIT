while True:
    n = int(input())
    if n == 0: break
    a =[]
    for i in range(0,n):
        so = input().lstrip('0')
        a.append(so)
    a.sort(key = int)
    if a.count(a[0]) == len(a):
        print("BANG NHAU")
    else:
        print(a[0], a[len(a)-1])
    
