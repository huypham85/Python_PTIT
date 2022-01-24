class Person:
    def __init__(self,name,gender,dob):
        self.name = name
        self.gender = gender
        self.dob = dob
    def describe_person(self):
        print(self.name,self.gender,self.dob)

class Student(Person):
    def __init__(self,name,gender,dob,id,avgMark,email):
        super().__init__(name,gender,dob)
        self.id = id
        self.avgMark = avgMark
        self.email = email
    def describe_student(self):
        super().describe_person()
        print(self.id,self.avgMark,self.email)
    def check_scholarship(self):
        if self.avgMark >= 3.2:
            print(f"Sinh vien {self.name} co hoc bong")
        else:
            print(f"Sinh vien {self.name} ko co hoc bong")

# a = Student("A", "male","1/1/2001",123,3.4,"A@email.com")
# a.describe_student()
# a.check_scholarship()

class Rectangle():
    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong
    def tinhChuVi(self):
        return (self.dai+self.rong)*2
    def tinhDienTich(self):
        return self.dai*self.rong
        