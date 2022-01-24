from cgi import print_form


t = int(input())
def base_4(num,base):
    res =""
    if len(num)%2==1:
        num = '0'+num
    i = len(num) -1
    print(num)
    while i>=1:
        num1 = num[i]
        num2 = num[i-1]
        print(num1)
        print(num2)
        
        tmp = num2 + num1
        if tmp == "00":
            res = "0" +res
        elif tmp == "01":
            res = "1" +res
        elif tmp == "10":
            res = "2" +res
        elif tmp == "11":
            res = "3" +res
        i-=2
    return res
   

while t>0:
    k = int(input())
    s = input()
    dec1 = int(s,2)
    res = 0
    if k == 2:
        print(s)
    elif k == 4:
        print(base_4(s,4))
    elif k == 8:
        print(str(oct(dec1))[2::])
    elif k == 16:
        print(str(hex(dec1))[2::])
    t-=1