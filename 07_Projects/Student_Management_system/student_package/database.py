import json
import os
from .student import Student

# Save file in the same folder as database.py
BASE_DIR = os.path.dirname(__file__)  
STUDENTS_FILE = os.path.join(BASE_DIR, "students.json")


def save_students(student):
    """Save a new student to JSON file"""
    students = []
    if os.path.exists(STUDENTS_FILE) and os.path.getsize(STUDENTS_FILE) > 0:
        with open(STUDENTS_FILE, "r") as f:
            students = json.load(f)

    students.append(student.to_dict())

    with open(STUDENTS_FILE, "w") as f:
        json.dump(students, f, indent=4)


def load_students():
    """Load all students from JSON file"""
    if not os.path.exists(STUDENTS_FILE) or os.path.getsize(STUDENTS_FILE) == 0:
        return []

    with open(STUDENTS_FILE, "r") as f:
        return json.load(f)
