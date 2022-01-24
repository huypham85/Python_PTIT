#split a string into words
str = input()
listWord = list(str.split(' ')) #push every word into a list
#print(len(listWord))
for word in listWord:
    print(word)
