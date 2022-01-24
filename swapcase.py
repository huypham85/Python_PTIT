from re import L


s = input()
for i in s:
    if i.islower():
        print(i.upper(),end='')
    else: print(i.lower(),end='')