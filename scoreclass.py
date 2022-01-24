class ThiSinh:
    def __init__(self, ten, diem1,diem2,diem3):
        self.ten = ten
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
    def toString(self):
        print("%s %.1f"%(self.ten, 0.1*self.diem1+0.3*self.diem2+0.6*self.diem3))

if __name__ == "__main__":
    ten = input()
    diem1 = float(input())
    diem2 = float(input())
    diem3 = float(input())
    ts = ThiSinh(ten, diem1, diem2, diem3)
    ts.toString()
