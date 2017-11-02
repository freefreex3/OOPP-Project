# Author : Tey Tong Yuan Justin
# Admin No :172932F
print("Welcome to ABC Department Store")
print("--Self Checkout Kiosk--")
listprice = float(input("Enter List Price $"))

if listprice <30 :
    discountedprice=listprice/2
    print("Discounted price $%.2f @50 percent" %discountedprice)
elif listprice <=100 :
    discountedprice=listprice*(.7)
    print("Discounted price $%.2f @30 percent" %discountedprice)
else :
    discountedprice=listprice*(0.85)
    print("Discounted price $%.2f @15 percent" %discountedprice)
