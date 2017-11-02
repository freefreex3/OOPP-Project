# Author : Tey Tong Yuan Justin
# Admin No :172932F
records =int(input("No of expense records you want to enter:"))
sum = 0
for n in range(1,records+1):
    expense = float(input("Please enter the expenses amount:"))
    sum=sum + expense
print("Total expenses you have entered is $ %.2f"%(sum) )
