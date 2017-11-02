class Customer:
    def __init__(self,customerid,customername):
        self.__customerid = customerid
        self.__customername = customername


    def get_customerid(self):
        return self.__customerid

    def get_customername(self):
        return self.__customername;

    def set_customerid(self,customerid):
        if(len(customerid) == 6):
            if customerid[-1].isalpha():
                self.__customerid =  customerid

    def set_customername(self,customername):
        self__customername = customername

    def display_details(self):
        print("=============Customer Detail===============")
        print("Customer ID",self.__customerid)
        print("Self",self.__customername)

c1 = Customer("Lee Chit Boon","12345A")
c1.display_details()
