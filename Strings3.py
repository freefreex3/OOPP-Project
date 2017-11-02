text = input("Enter a string:")
uppercount = 0

for char in text:
    if char.upper() == char and char != " ":
        uppercount += 1
if uppercount >= 2:
    print(text.upper())
else:
    print("The string contains less than 2 uppercase characters")

