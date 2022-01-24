n = input()
while len(n)>1:
    k=len(n)
    s1= n[:k//2]
    s2 = n[k//2:]
    s3 = int(s1)+int(s2)
    print(s3)
    n= str(s3)