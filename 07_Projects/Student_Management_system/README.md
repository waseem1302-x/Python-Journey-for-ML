# 🎓 Student Management System (SMS)

A **Python-based Student Management System (SMS)** built step by step during my learning journey.
This project started as a simple single-file script and gradually evolved into a **modular, professional-grade package** with logging, validation, and tabular data presentation.

---

## 📖 Project Evolution Timeline

### **Step 1: The Beginning**

* Started with **one file (`main.py`)**.
* Contained only **`add_student()`** function.
* Stored student info in a list of dictionaries.
* Minimal validation (manual age, GPA inputs).
* Output was printed directly to console in raw format.

```python
students = []

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    student_id = len(students) + 1
    courses = input("Enter Courses (comma separated): ").split(",")
    gpa = float(input("Enter GPA: "))
    
    student = {
        "name": name,
        "age": age,
        "id": student_id,
        "courses": courses,
        "gpa": gpa
    }
    students.append(student)
    print("Student added successfully!")
```

✅ **Basic functionality working.**
❌ **Problems**: No modularity, no error handling, no structure, everything was in one place.

---

### **Step 2: Object-Oriented Design**

* Introduced a **`Student` class** with attributes (`name`, `age`, `id`, `courses`, `gpa`).
* Moved from dicts → **objects** for better encapsulation.
* Added **methods** for displaying student info.

```python
class Student:
    def __init__(self, name, age, student_id, courses, gpa):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses
        self.gpa = gpa
```

---

### **Step 3: Modularization**

* Split code into multiple files inside a **package `student_package/`**:

  * `student.py` → `Student` class.
  * `database.py` → file handling (save/load JSON).
  * `student_utils.py` → helper functions (add, delete, search, sort).
  * `__init__.py` → clean imports.
* Main file (`main.py`) became a **menu-driven system**.

---

### **Step 4: Validation & Error Handling**

* Introduced **input validators**:

  * Name: must be alphabetic.
  * Age: restricted to **15–30**.
  * GPA: must be **0–4**.
  * Courses: comma-separated values, cleaned.
* Added **`get_valid_input()`** wrapper to reduce repetitive code.
* User input became **safe and controlled**.

---

### **Step 5: Tabular Display**

* Added **`tabulate`** library to print students in neat tables.
* Implemented `print_students()` for multi-student display and `print_student()` for single view.

Example Output:

```
=== All Students ===
+------+--------+-----+----------------------+-----+
| ID   | Name   | Age | Courses              | GPA |
+------+--------+-----+----------------------+-----+
| S001 | Alice  | 20  | Math, Physics        | 3.5 |
| S002 | Bob    | 19  | Chemistry, English   | 3.9 |
+------+--------+-----+----------------------+-----+
```

---

### **Step 6: Logging System**

* Created a **`logs/`** folder.
* Added `logger.py` with:

  * File handler (`logs/sms.log`).
  * Console handler.
  * Levels: INFO, WARNING, ERROR.
* Logged all critical operations:

  * Student added.
  * Student deleted.
  * Searches.
  * Export operations.

Example log:

```
2025-08-29 11:45:12 | INFO | Student Added | ID=S003 | Name=Charlie
2025-08-29 11:47:01 | INFO | Student Deleted | ID=S002 | Name=Bob
2025-08-29 11:49:15 | WARNING | Search | No students available
```

---

## 📂 Project Structure (Final)

```
SMS/
│── main.py                # Menu-driven main file
│── requirements.txt        # Dependencies
│── logs/                   # All logs stored here
│   └── sms.log
|
│── student_package/        # Package
│   │── __init__.py
│   │── student.py          # Student class
│   │── database.py         # Save/load students (JSON)
│   │── student_utils.py    # Operations (add, delete, search, sort, export)
│   │── logger.py           # Central logging setup
|        
```

---

## ⚙️ Features (Final State)

* ✅ Add, view, sort, delete, search, and export students.
* ✅ Input validation (name, age, GPA, courses).
* ✅ Student IDs generated automatically.
* ✅ Save/load from JSON database.
* ✅ Tabular display using `tabulate`.
* ✅ Logging with file.
* ✅ Modular, package-based design.

---

## 🚀 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/waseem1302-x/Python-Journey-for-ML.git
   cd SMS
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the system:

   ```bash
   python main.py
   ```

---

## 📦 Requirements

* Python ≥ 3.8
* Tabulate ≥ 0.9.0

```txt
tabulate>=0.9.0
```

---

## 📝 Example Usage

```
===== Student Management System =====
1. Add Student
2. View All Students
3. Sort Students
4. Search Student
5. Delete Student
6. Export Students
7. Exit
```

---

## 🔮 Future Improvements

* Add GUI (Tkinter/PyQt).
* Import from CSV/Excel.
* GPA calculator integration.
* Student performance analytics.

---

## 🧑‍💻 Learning Outcome

Through this project, I learned:

* Python fundamentals → OOP → modular programming.
* File handling (JSON database).
* Package structuring & `__init__.py`.
* Logging best practices.
* Error handling & input validation.
* Using external libraries (`tabulate`).

This **Student Management System** represents my **Python learning journey** — from absolute basics to building a **clean, scalable, real-world project**. 🚀

---

If you like this project or find it helpful, ⭐ star it on GitHub and follow my Python journey!