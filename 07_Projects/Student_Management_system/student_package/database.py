import json
import os
from .student import Student

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
STUDENTS_FILE = os.path.join(DATA_DIR, "students.json")



def add_student(student):
    students = []
    if os.path.exists(STUDENTS_FILE) and os.path.getsize(STUDENTS_FILE) > 0:
        with open(STUDENTS_FILE, "r") as f:
            students = json.load(f)

    students.append(student.to_dict())

    with open(STUDENTS_FILE, "w") as f:
        json.dump(students, f, indent=4)


def save_students(students):
    with open(STUDENTS_FILE, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)


def load_students():
    if not os.path.exists(STUDENTS_FILE) or os.path.getsize(STUDENTS_FILE) == 0:
        return []

    with open(STUDENTS_FILE, "r") as f:
        data = json.load(f)
        return [Student.from_dict(s) for s in data]

