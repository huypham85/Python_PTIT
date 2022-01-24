n, k = map(int, input().split())
dic = {}
for i in range(n):
    s = input().split()
    dic[s[0]] = float(s[1])

if k > n or n > 70 or k > 5:
    print('INVALID INPUT')
else:
    L = sorted(dic.items(), key= lambda x : (-x[1], x[0]))

    for i in range(k):
        print(L[i][0], end = ' ')
'''
10 3
Hung 6    
Long 7
Giang 8
Linh 5
Tuan 8
Hoa 9
Mai 5
Ngoc 4
Khanh 9
Ngan 10
'''