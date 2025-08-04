# 🔁 02_ControlFlow – Conditional Logic and Functions in Python

This folder teaches you how to add logic, repetition, and reusability to your code. Control Flow is what makes your program dynamic and interactive.

---

## ✅ Topics Covered

### 1. Conditional Statements

- Use conditions to make decisions in your code.

```python
age = 20
if age >= 18:
    print("You are eligible to vote")
elif age >= 16:
    print("You can apply for a license")
else:
    print("You are too young")


Keywords: if, elif, else

2. Comparison and Logical Operators
==, !=, >, <, >=, <=

and, or, not

if age > 18 and has_id:
    print("Entry allowed")

3. Loops
➤ For Loop
Used to iterate over sequences like list, tuple, string, etc.
for i in range(5):
    print("Hello", i)


➤ While Loop
Runs while a condition is true.

x = 0
while x < 5:
    print(x)
    x += 1


4. Loop Control Statements
break – Exit the loop early

continue – Skip current iteration

pass – Do nothing (placeholder)


for i in range(10):
    if i == 5:
        break
    print(i)


5. Functions
Encapsulate code into reusable blocks.

def greet(name):
    return f"Hello, {name}"

message = greet("Waseem")
print(message)



Also covered:

Function arguments

Return values

Default parameters

Scope (global, local)

def, return

🧠 Why It Matters
Control flow is how your program decides what to do, when, and how often.
Functions make your code modular, reusable, and organized.

Without control flow, your code is just a list of instructions with no intelligence.

🎯 Learning Outcomes
By completing this section, you will be able to:

Write programs that make decisions

Use loops to handle repetitive tasks

Build and use your own functions

Manage complexity by organizing code into logical blocks

📌 This is the true start of "problem-solving" in Python — keep practicing patterns and challenges using what you’ve learned here!
