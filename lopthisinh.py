class ThiSinh:
    def __init__(self, ten, dob, diem1,diem2,diem3):
        self.ten = ten
        self.dob = dob
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
    def toString(self):
        print(self.ten, self.dob,self.diem1+self.diem2+self.diem3)

if __name__ == "__main__":
    ten = input()
    dob = input()
    diem1 = float(input())
    diem2 = float(input())
    diem3 = float(input())
    ts = ThiSinh(ten, dob, diem1, diem2, diem3)
    ts.toString()
