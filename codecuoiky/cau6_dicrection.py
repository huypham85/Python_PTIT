k = int(input())
if k <=10:
    sum = 0
    mul = 1
    for i in range(k):
        key,val = input().split()
        if val.isdigit():
            sum += int(val)
            mul *= int(val)
    print(sum,mul)
else:
    print("INVALID INPUT")