n,k = map(int,input().split()) 
dict = {}
while n>0:
    list = input().split()
    dict[list[0]] = int(list[1])
    n-=1
if n>70 or k>5:
    print("INVALID INPUT")
else:
    ans = sorted(dict.items(),key=lambda x:(-x[1],x[0]))
    for i in range(k):
        print(ans[i][0],end=" ")
