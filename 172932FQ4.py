# Author : Tey Tong Yuan Justin
# Admin No :172932F
censoredword1 = input("Enter the word to be censored:")
censoredword2 = input("Enter the word to be censored:")
censoredword3 = input("Enter the word to be censored:")
i = 0
while i <3:
    sentence=input("Enter a string:")
    if censoredword1 or censoredword2 or censoredword3 in sentence:

            sentence = sentence.replace(censoredword1[1:],"*"*(len(censoredword1)-1))
            sentence = sentence.replace(censoredword2[1:],"*"* (len(censoredword2)-1))
            sentence = sentence.replace(censoredword3[1:],"*"*(len(censoredword3)-1))
            i += 1
            print("You have been censored",i,"times")
            print(sentence)
print("You have been banned")
