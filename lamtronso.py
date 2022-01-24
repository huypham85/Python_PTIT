def lamtron(s):
    n = list(s)
    if len(n)==1: return n
    carry = 0
    for i in range(len(n)-1,-1,-1):
        if carry == 1: 
            n[i] = str(int(n[i])+carry)
            carry = 0
        if i == 0:
                # if int(n[i])+carry<=5:
                #     n[i] = str(int(n[i])+carry)
                if int(n[i])>5:
                    n[i] ='0'
                    n.insert(0,'1')
        else:
            if int(n[i])>=5:
                n[i]='0'
                carry = 1
            else:
                n[i] ='0'
        #print(i, n[i])
    return n


t = int(input())
while t>0:
    n = input()
    for i in lamtron(n):
        print(i,end='')
    print()
    t-=1
    