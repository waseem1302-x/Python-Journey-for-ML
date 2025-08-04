
### 🧺 03_DataStructures – Lists, Tuples, Sets & Dictionaries in Python

This folder covers Python’s built-in data structures, which help you **store, organize, and access** your data effectively.

## ✅ Topics Covered

---

### 1. 📋 Lists – Ordered, Mutable Collections

Lists are used to store multiple items in a single variable.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
fruits.append("orange")
print(len(fruits))     # 4
````

#### 🔧 Common List Methods:

* `.append()`, `.insert()`, `.remove()`, `.pop()`
* `.sort()`, `.reverse()`, `.clear()`
* Slicing: `fruits[1:3]`
* Looping: `for item in fruits:`

#### ✅ Use when:

* You need ordered, changeable collections
* You need to add/remove frequently

---

### 2. 📦 Tuples – Ordered, Immutable Collections

Tuples are like lists, but you **cannot modify them**.

```python
dimensions = (1920, 1080)
print(dimensions[0])  # 1920
```

#### ✅ Use when:

* You need a fixed group of items
* For example: coordinates, RGB values, etc.

---

### 3. 🔁 Sets – Unordered, Unique Items

Sets automatically eliminate duplicates and support mathematical set operations.

```python
langs = {"Python", "Java", "C++", "Python"}
print(langs)  # {'Python', 'Java', 'C++'}
```

#### 🔧 Set Operations:

* `.add()`, `.remove()`
* `union()`, `intersection()`, `difference()`

```python
a = {"Python", "C++"}
b = {"Python", "Java"}

print(a | b)  # Union
print(a & b)  # Intersection
```

#### ✅ Use when:

* You need unique values
* You want fast membership checking

---

### 4. 🧠 Dictionaries – Key-Value Pairs

Dictionaries store data in `key: value` format.

```python
student = {
    "name": "Waseem",
    "age": 20,
    "course": "Python"
}
print(student["name"])
```

#### 🔧 Dictionary Methods:

* `.get()`, `.keys()`, `.values()`, `.items()`
* `.update()`, `.pop()`

#### 🔁 Looping through a dictionary:

```python
for key, value in student.items():
    print(key, ":", value)
```

#### ✅ Use when:

* You need to associate keys with values
* Great for configurations, JSON-like data

---

## 🧠 Why This Matters

Every problem you solve involves data. These structures help you:

* Organize data for fast access
* Eliminate duplication
* Create complex models (like storing users, scores, configs)

---

## 🎯 Learning Outcomes

By the end of this folder, you should be able to:

* Choose the right data structure for a problem
* Use all 4 types efficiently
* Solve problems using combinations (e.g., list of dicts)

📌 These structures are heavily used in **DSA**, **Web Dev**, **APIs**, and **Machine Learning**. Master them now for everything coming later.

```

