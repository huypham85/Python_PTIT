import json
dict_numbers ={"a":1,"b":7}
filename = "numbers.json"
with open(filename) as fn:
    # json.dump(dict_numbers, fn,indent=4) // ghi vao file json
    numbers = json.load(fn) #doc tu file json
print(numbers)