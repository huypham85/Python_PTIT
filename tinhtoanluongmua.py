class TramDo:
    ID = 1
    
    def __init__(self,name,cu,moi):
        self.id = KhachHang.ID
        KhachHang.ID +=1
        self.name = name
        self.cu = cu
        self.moi = moi
    def tinhTien(self):
        self.tien = 0
        sdung = self.moi-self.cu
        if sdung <= 50:
            self.tien = sdung*100
            self.tien += self.tien*0.02
        elif sdung >50 and sdung <= 100:
            self.tien += (50*100)
            sdung -=50
            self.tien += (sdung*150)
            self.tien += self.tien*0.03

        elif sdung >100:
            self.tien += (50*100)
            self.tien += (50*150)
            sdung -=100
            self.tien += (sdung*200)
            self.tien += self.tien*0.05

        # print(self.tien)
        self.tien = round(self.tien)
    def toString(self):
        print ("KH%02d %s %d" % (self.id, self.name,self.tien))

if __name__ == "__main__":
    n = int(input())
    listKH = []
    while n > 0:
        name = input()
        cu = int(input())
        moi = int(input())
        kh = KhachHang(name,cu,moi)
        kh.tinhTien() 
        listKH.append(kh)
        n-=1 
    list =sorted(listKH,key=lambda x:(x.tien,x.id),reverse=True)
    # print(len(listKH))
    # print(list)
    for i in list:
        i.toString()


        

