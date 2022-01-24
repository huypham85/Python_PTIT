import re
xau1 = input().strip().lower()
xau2 = input().strip().lower()
if len(xau1) == 0 and len(xau2) == 0:
    print(1.00)
else:
    xau1 = set(re.findall("[\w+]", xau1))
    xau2 = set(re.findall("[\w+]", xau2))
    res = len(xau1&xau2) / len(xau1|xau2)
    print(f"{res:.2f}")