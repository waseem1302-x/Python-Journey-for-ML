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




"""
INHERITANCE IN PYTHON

Inheritance allows one class (child) to inherit properties and behaviors (methods)
from another class (parent).

Purpose:
✅ Reuse existing code
✅ Avoid repetition (DRY – Don't Repeat Yourself)
✅ Build relationships like: is-a

Example:
If we have a 'Car' class,
we can create a 'Cars Brand (Toyotoa, Honda etc)' class that inherits from it,
so Student gets all of Person's features, and can have its own too.

Types:
- Single Inheritance
- Multiple Inheritance
"""
class Car:
    def __init__(self,name, brand, model):
        self.brand = brand
        self.model = model
        self.name = name

    def driver(self):
        print(f"The driver of this {self.brand} {self.model} is {self.name}.")
    
    def drive(self):
        print(f"{self.name} is driving {self.brand} {self.model}")

    def stop(self):
        print(f"{self.name} has stopped {self.brand} {self.model}.")


class Toyota(Car):
    def eco_mode(self):
        print(f"{self.name} put {self.brand} {self.model} is on eco_mode")

class Honda(Car):
    def music_system(self):
        print(f"{self.name} {self.brand} {self.model} has a premium music system.")


t1 = Toyota("Ali" , "Toyota", "Camry")
h1 = Honda("Waseem", "Honda", "Civic")

t1.driver()
t1.drive()
t1.stop()
t1.eco_mode()


print("---")

h1.driver()
h1.drive()
h1.music_system()
h1.stop()


"""
🎭 Polymorphism means 'many forms'.
In OOP, it allows different classes to have methods with the same name 
but with **different behaviors**.

✅ Purpose:
- To write cleaner, more flexible, and reusable code.
- It lets you call the same method on different objects and get different results.
"""


# 📦 Real-life example: We use + in all three but result is differnt for all.
print(2+3)
print("Waseem " + "Mushtaq")
print([1,2,3] + [4,5,6])

class Car:
    def drive(self):
        print("Car is driving...")

class Toyota(Car):
    def drive(self):
        print("Toyota is driving smoothly with eco mode...")

class Honda(Car):
    def drive(self):
        print("Honda is driving with sporty performance...")

# Polymorphism in action:
def test_drive(car):
    car.drive()  # Same method, different output depending on class

t1 = Toyota()
h1 = Honda()

# all test_drive on both
test_drive(t1)
test_drive(h1)  