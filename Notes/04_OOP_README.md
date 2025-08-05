
### 🧱 04_OOP – Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a way of structuring code using **classes and objects**, focusing on **real-world modeling**, **modularity**, and **reusability**.

This folder covers the core concepts, structure, and four fundamental pillars of OOP.

# ✅ Topics Covered

### 1. 🔤 What is OOP?

OOP helps structure large programs by bundling **data (attributes)** and **behavior (methods)** together inside objects.

---

### 2. 🧩 Classes and Objects

- A **class** is a blueprint.
- An **object** is a specific instance built from that blueprint.

```python
class YouTuber:
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel

    def show_info(self):
        print(f"{self.name} runs the channel {self.channel}")

yt1 = YouTuber("Waseem", "StudyWithWaseem")
yt1.show_info()
````

---

### 3. 🧱 Instance Attributes vs Class Attributes

* **Instance Attribute**: Belongs to the object
* **Class Attribute**: Shared across all objects

```python
class Student:
    school = "AIU"  # Class Attribute

    def __init__(self, name):
        self.name = name  # Instance Attribute
```

---

### 4. ⚙️ Methods

* **Instance Methods**: Regular methods accessing/using object data
* **Static Methods**: Don’t use `self`, utility-like functions inside class

```python
class MathTool:
    @staticmethod
    def square(n):
        return n * n
```

---

## 🔐 The 4 Pillars of OOP

---

### 🧩 1. Abstraction – *Hiding unnecessary details*

Only expose what is needed to the user, and hide the inner complexity.

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Hidden (private)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

### 🛡️ 2. Encapsulation – *Wrapping data and code together*

Keep data safe and restrict direct access. Use getters/setters.

```python
class Person:
    def __init__(self, age):
        self.__age = age  # Encapsulated

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
```

---

### 🧬 3. Inheritance – *Reusing code between classes*

Child class inherits features from parent class.

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark!")

d = Dog()
d.speak()
```

---

### 🧠 4. Polymorphism – *Same method, different behavior*

Different classes can define the same method differently.

```python
class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

for animal in (Cat(), Cow()):
    print(animal.sound())
```

---

## 🧠 Why This Matters

OOP helps in:

* Modeling real-world entities
* Building **large-scale, maintainable applications**
* Organizing code cleanly using reusable components

OOP is used in:

* GUI apps, games, ML frameworks, web backends, and more.

---

## 🎯 Learning Outcomes

By the end of this section, you will:

* Understand how to define and use classes and objects
* Apply the 4 pillars in real-world code
* Build systems using OOP principles

---

📌 This knowledge is a **must-have for DSA, large Python projects, and ML development**.

```
