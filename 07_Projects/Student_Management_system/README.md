# 🎓 Student Management System (CLI)

## 📖 About This Project

The **Student Management System (CLI)** is one of the core milestone projects in my Python learning journey.
It started as a simple practice exercise for basic Python concepts and evolved into a structured, modular, and scalable application following real-world software development practices.

This project is not just a one-time build — it’s designed as a **base project** that will grow alongside my Python skills. As I progress through different sections (OOP, File Handling, Databases, APIs, Machine Learning), I’ll integrate new features into it.

---

## 🚀 How It Started

* **Phase 1** → *Basic CLI prototype*

  * Implemented with simple variables, lists, and functions
  * Supported adding, viewing, and removing students
  * Code was in a **single file** (quick and messy)

* **Phase 2** → *Modular Python*

  * Refactored into **modules** and **packages**
  * Introduced `student_package` package with `Student` class and utilities containing `Helper Functions `
  * Cleaner imports, maintainable structure

---

## 🎯 Current Features (v2.0)

- Add a new student with **validated inputs** (Name, Age, Courses, GPA)
- View all students in a **tabular format**
- Sort students by **Name** or **ID**
- Search students by **Name** or **ID**
- Delete students with **confirmation**
- Export student data to **timestamped CSV**
- Automatic **unique student ID generation**
- **Persistent JSON database**
- Robust **input validation and error handling**

---

## 📂 Project Structure

```
SMS/
├── student_package/
│   ├── __init__.py
│   ├── student.py
│   ├── database.py
│   ├── student_utils.py
│   └── logger.py
|
├── logs/
│   └── sms.log
|
├── main.py
├── README.md
└── requirements.txt

```

---

## 🛠 Tech Stack

* **Python 3.x**
* **CLI-based Interface** (Text-based interaction)
* **Custom Modules & Packages**
* **OOP Principles**

---

## 🔮 Scaling Plan

This project will evolve as my Python journey continues:

1. **06\_FileHandling** → Save student data to text, CSV, and JSON files.
2. **Databases** → Integrate SQLite/MySQL for persistent storage.
3. **Error Handling** → More robust exception management.
4. **APIs** → Add API endpoints to access student data externally.
5. **GUI** → Transition from CLI to Tkinter or PyQt-based interface.
6. **Machine Learning** → Predictive features (e.g., GPA forecasting).
7. **Full Web App** → Convert into a Django/Flask-based web application.

---

## 💡 Learning Purpose

This project serves as:

* A **practice ground** for every Python concept I learn
* A **reference project** to revisit and improve as I grow
* A **portfolio piece** for GitHub and interviews

---

If you like this project or find it helpful, ⭐ **star it on GitHub** and follow my Python journey!
