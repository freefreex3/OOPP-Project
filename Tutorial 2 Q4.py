class Holder:
    def __init__(self,name,address,phonenumber):
        self.__name = name
        self.__address = address
        self.__phonenumber = phonenumber

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phonenumber(self):
        return self.__phonenumber

    def set_name(self, name):
        self.__name = name

    def set_gender(self, address):
        self.__gender = address

    def set_phonenumber(self,phonenumber):
        self.__phonenumber = phonenumber

    def __str__(self):
        s ='Name : {}, address : {} and number : {}'.format(self.get_name(), self.get_address(), self.get_phonenumber())
        return s

s = Holder("Ms Khoo", 'NYP' ,"99wewqeqwe9")
print(s)
s = Holder("Mr LEE", 'NYP' ,"9eqweq99")
print(s)
s = Holder("Ms CHIT", 'NYP' ,"9grfege99")
print(s)

