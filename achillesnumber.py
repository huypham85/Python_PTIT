import math
def check_1(n):
    tmp = n
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            if tmp%(i*i)!=0: return False
            while n%i==0:
                n/=i
    if n>1:
        if tmp%(n*n)!=0: return False
    return True
def check_2(n):
    sum=1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            sum = sum + i + n/i
    if sum==n: return True
    else: return False
n = int(input())
if check_2(n)==False and check_1(n): print("1")
else: print("0")


