def check_rank(pts):
    if pts>=8.5: return ["A","Giỏi"]
    elif pts>=7.0: return ["B","Khá"]
    elif pts>=5.5: return ["C","Trung bình"]
    elif pts>=4.0: return ["D","Trung bình kém"]
    else : return ["F","Kém"]

ten = input()
cc = float(input())
kttx = float(input())
btl = float(input())
ck = float(input())
ans = check_rank(cc*0.1+ kttx*0.1 +btl*0.2+ck*0.6)
print(ten)
print(ans[0])
print(ans[1])