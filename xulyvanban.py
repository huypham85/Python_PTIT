import re
text = ""
while True: 
    try: 
        str = input() 
        text += str + " "
    except EOFError: break
list = re.split("[.?!]",text.lower())
for i in list:
    x = " ".join(i.split()).strip().capitalize()
    print(x)
# for i in list:
#     print(i)