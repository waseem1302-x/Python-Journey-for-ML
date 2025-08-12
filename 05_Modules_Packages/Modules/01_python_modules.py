"""
A module is just a Python file (.py) 
containing functions, variables, or classes that you can use in another file. 


"""

# Using Built-in Modules

import math

print(math.pi)
print(math.sqrt(4))

import random

print(random.randint(1,20))


# different ways to import modules

import math
print(math.sqrt(16))

from math import pi
print(pi)

import math as m
print(m.sqrt(25))


# We can also create customs modules & can import in main file

import custom_module

name = "Waseem"
a = 10
b = 2

print(custom_module.greet(name))
print(custom_module.add(a,b))
print(custom_module.subs(a,b))
print(custom_module.multiply(a,b))
print(custom_module.devide(a,b))