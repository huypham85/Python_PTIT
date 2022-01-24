t = int(input())

def solve(a,b,test):
    if len(b)!=len(a):
        print("{}{}{}".format("Test ", test,": NO"))
        return
    for i in range(len(b)):
        if b[i] != a[i]:
            print("{}{}{}".format("Test ", test,": NO"))
            return
    print("{}{}{}".format("Test ", test,": YES"))

for test in range(1,t+1):
    s1 = input()
    s2 = input()
    list1 = sorted(list(s1))
    list2 = sorted(list(s2))
    # print(list1)
    # print(list2)
    solve(list1,list2,test)