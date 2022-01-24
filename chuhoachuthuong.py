def cnt(s):
    cnt_upper = 0
    cnt_lower = 0
    for i in s:
        if i.isupper() : cnt_upper +=1
        if i.islower() : cnt_lower +=1
    if(cnt_lower >= cnt_upper):
        print(s.lower())
    else:
        print(s.upper())

s = input()
cnt(s)