# class Employee:
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age
#         pass

# employee1 =Employee("ekta",99)
# print(employee1.name)

# - Create a class called BankAccount with the following attributes: account number, account holder name, and account balance.
# - Create a constructor for the BankAccount class that initializes the account number, account holder name, and account balance.
# - Create methods to deposit and withdraw money from the account. The methods should update the account balance accordingly.
# - Create a method to display the account information, including the account number, account holder name, and account balance.
class BankAccount :
    def __init__ (self,account_number,account_holder_name, account_balance):
        self.account_number =account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance 

    def deposit_money(self,amount) :
        self.account_balance = amount+ self.account_balance
        return self.account_balance
    def withdraw_money(self,amount):
        self.account_balance = self.account_balance -amount
        return self.account_balance
    def account_details(self):
        print(f"account name: {self.account_holder_name}\n")
        print(f"account number:{self.account_number}\n")
        print(f"account balance:{self.account_balance}\n")

Account_holder1 = BankAccount(123,"ekta",100000000000000000) 
Account_holder1.deposit_money(200)
Account_holder1.account_details()
