# Exploring the 4 Pillars of OOP. 

# No:1 Abstraction (Hiding Unnecessary details)

class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.account_no = acc

    # debit method

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited")
        print(f"total balance = {self.get_balance()}")


    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited")
        print(f"total balance = {self.get_balance()}")


    def get_balance(self):
        return self.balance


acc1 = Account(2000, 5010600)
acc1.debit(1000)
acc1.credit(2000)
acc1.credit(40000)
acc1.debit(5000)   


# No:2 Encapsulation: Wrapping data (attributes) & code(methods) togather in single unit
# kind of secure box

# Private Attributes: Any attribute or method starting with double underscore __ is considered private.
# It means: “For internal use only” – don’t access directly from outside the class.

class Account:
    def __init__(self, balance):
        self.__balance = balance  # __balance: Private attribute
    
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
acc2 = Account(1000)
print(acc2.get_balance())