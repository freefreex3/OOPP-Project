word = input("Enter string here:")

if len(word) >= 5:
    if word[-3:]== "ing":
        word += "ly"
    else:
        word += "ing"
print(word)
