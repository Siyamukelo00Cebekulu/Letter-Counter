text = input("Enter a word:")
dict = {}
for x in text:
    count = text.count(x)
    dict[x] = count
print(dict)

