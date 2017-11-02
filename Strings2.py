#sentence = input("Enter String:")
#sentence = sentence.replace(' ', '')
#print(sentence)

oldstr = input('Enter a string:')
newstr = ""
for c in oldstr:
    if c != " " :
        newstr += c
print(newstr)
