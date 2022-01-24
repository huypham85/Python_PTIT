filename = "guest.txt"


while(True):
    name = input("Nhap ten nguoi dung ")
    if name == "quit" : break
    print("Hello", name)
    with open(filename, 'a+') as fn:
        fn.write(name+ '\n')
    
