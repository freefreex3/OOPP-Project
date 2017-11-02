# Author : Tey Tong Yuan Justin
# Admin No :172932F
creditcardno = input("Enter your credit card number:")

if len(creditcardno)!= 15 and len(creditcardno)!=16 :
    print("You have entered an invalid credit card number")
elif creditcardno[0] == "4" and len(creditcardno)==15:
    print("You have entered an invalid Amex card number")
elif (creditcardno[0:2] == "34" or creditcardno[0:2]=="37") and (len(creditcardno)== 15 or len(creditcardno)== 16):
    print("You have entered an invalid Visa card number")

else:
    if creditcardno[0:2] == "34" or creditcardno[0:2]== "37":
        print("You have a valid Amex card and the last 4 digits is",creditcardno[-4:])
    elif creditcardno[0] == "4":
        print("You have a valid Visa card and the last 4 digit is",creditcardno[-4:])


