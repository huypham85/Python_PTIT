s = input()

print(len(s))
print(s[-3:])
print(s[::-2])
print(s[:-2])
print(s[:5])


tmp = ''
for i in range(0, len(s), 2):
    tmp += s[i]

print(tmp)

tmp = ''
for i in range(1, len(s), 2):
    tmp += s[i]

print(tmp)
print(s[::-1])
print(s[-2])

