t = int(input())

def convert(num):
    if num>=0 and num<=9:
        return chr(num+ord('0'))
    else: #neu trong he 16
        # print(ord('A'))
        return chr( num- 10 + ord('A'))

while t>0:
    n,base = map(int,input().split()) 
    res=""
    while n>0:
        res += convert(n%base)
        n = int(n/base)
    res = res[::-1]
    print(res)
    t-=1
