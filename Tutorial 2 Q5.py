class BankAccount:
    def _init_(self, account_number):
        self.__account_number = account_number
        self.__balance = 0.0

    def get_account_numbers(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount>0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.get_balance():
            print('You have insufficient funds')
        else:
            self.__balance -= amount

    def get_interest_rate(self):
        if self.__account_number.startswith('0'):
            return 0.005
        elif self.__account_number.startswith('1'):
            return 0.01
        else:
            print('You have an invalid account')
            return 0

    def get_interest(self):
        return self.__balance * self.get_interest_rate()

account = BankAccount('100000')
account.deposit(500)
print('You have ' , account.get_balance())
account.withdraw(100)
print('You have ' , account.get_balance())
