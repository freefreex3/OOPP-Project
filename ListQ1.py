# num_1 = input("Please enter the first number:")
# num_2 = input("Please enter the second number:")
# num_3 = input("Please enter the third number:")
# num_4 = input("Please enter the fourth number:")
# num_5 = input("Please enter the fifth number:")
# num_6 = input("Please enter the sixth number:")
# num_7 = input("Please enter the senventh number:")
# num_8 = input("Please enter the eighth number:")
# num_9 = input("Please enter the ninth number:")
# num_10 = input("Please enter the tenth number:")
#
# if num_1.isdecimal() or num_2.isdecimal() or num_3.isdecimal() or num_4.isdecimal() or num_5.isdecimal() or num_6.isdecimal() or num_7.isdecimal() or num_8.isdecimal() or num_9.isdecimal() or num_10.isdecimal() :
#
#     series =[num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,num_10]
#
#
#     print("The maximum value is:",max(series))
#
#     print("The minumum value is:",min(series))
#
#     print("The total number of numbers in the list is:",len(series))
#
#     ave = sum(series)/len(series)
#
#     print("The average is",ave)
# else:
#     print("You have entered an invalid number")

numlist = []

for i in range(10):
    msg = "Enter number #" + str(i+1)
    num = int(input(msg))
    numlist.append(num)

print("The lowest number in the list:",min(numlist))
print("The highest number in the list:",max(numlist))
print("The total of the  numbers in the list:",sum(numlist))


print("The average of the number in the list:",sum(numlist)/len(numlist))
