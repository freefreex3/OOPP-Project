string = "programming"

count=0

for ch in string:
    if count%2 == 0:
        print(ch.upper(),end ="")
    else:
        print(ch,end="")
    count += 1






