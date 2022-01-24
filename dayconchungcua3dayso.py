t = int(input())
while t>0:
    n,m,k = map(int, input().split())
    a = [int(i) for i in input().split()] 
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    i =0
    j=0
    h=0
    dd=0
    while i<n and j<m and h<k:
        if a[i]==b[j] and b[j] == c[h]:
            dd=1
            print(a[i],end=" ")
            i+=1
            j+=1
            h+=1
        elif a[i]<b[j]:
            i+=1
        elif b[j]<c[h]:
            j+=1
        else:
            h+=1
    if dd==0: 
        print("NO")
    else:    
        print()
    t-=1
