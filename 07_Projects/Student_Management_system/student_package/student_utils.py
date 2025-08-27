from .student import Student
from . import database
import datetime
from tabulate import tabulate
import csv

students = []

# === Helper to Load Students ===
def get_students():
    """Load students from the database safely."""
    return database.load_students() or []


# Add Students
def add_students():
    name = input("Enter Student Name: ")
    age = get_valid_number("Enter Age (15–30): ", 17, 30, int)
    student_id = generate_student_id()
    print(f"\nAssigned Student ID: {student_id}")
    courses = input("Enter Student Courses (comma separated): ").split(",")
    gpa = get_valid_number("Enter GPA (0–4): ", 0, 4, float)

    new_student = Student(name, age, student_id, [c.strip() for c in courses], gpa)
    database.add_student(new_student)
    print(f"Student '{name}' added successfully!")


# View All Students
def view_all_students():
    students = get_students()
    if not students:
        print("No student found\n")
        return
    
    print_students(students, "All Students")


# Sort Students
def sort_students():
    students = get_students()
    if not students:
        print("No students found in the database.")
        return
    
    print("== Sort by ==")
    print("1: By Name (A-Z)")
    print("2: By ID (ascending)")
    choice = input("Enter Your Choice (1-2): ").strip()

    if choice == "1":
        sorted_list = sorted(students, key=lambda s: s.name.lower())
    elif choice == "2":
        sorted_list = sorted(students, key=lambda s: s.student_id)
    else:
        print("Invalid choice.")
        return

    print_students(sorted_list, "Sorted Students")


# === Search Students ===
def binary_search_by_id(students, target_id):
    left, right = 0, len(students) - 1
    while left <= right:
        mid = (left + right) // 2
        if students[mid].student_id == target_id:
            return mid
        elif students[mid].student_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # not found

def find_student(students, by="id", value=""):
    if by == "id":
        idx = binary_search_by_id(students, value)
        return [students[idx]] if idx != -1 else []
    elif by == "name":
        return [s for s in students if s.name.lower() == value.lower()]
    return []

def search_student():
    students = get_students()
    if not students:
        print("No students in database")
        return

    print("== Search Student ==")
    print("1. By Name")
    print("2. By ID")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        found = find_student(students, by="name", value=name)
        if found:
            print_students(found, "Search Results")
        else:
            print("No student found with that name.")

    elif choice == "2":
        student_id = input("Enter ID: ")
        found = find_student(students, by="id", value=student_id)
        if found:
            print_student(found[0], "Search Result")   # single
        else:
            print("No student found with that ID.")


# Delete Student
def del_student():
    students = get_students()
    if not students:
        print("No students to delete.")
        return

    student_id = input("Enter ID to delete: ").strip()
    found = find_student(students, by="id", value=student_id)

    if found:
        print_student(found[0], "Student Found")
        confirm = input("Delete this student? (y/n): ")
        if confirm.lower() == "y":
            students.remove(found[0])
            database.save_students(students)
            print("Student deleted successfully.")
    else:
        print("No student found with that ID.")


# Export Students to CSV 
def export_students():
    students = get_students()
    if not students:
        print("No students to export.")
        return

    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Age", "Courses", "GPA"])
        for s in students:
            writer.writerow([
                s.student_id,
                s.name,
                s.age,
                ", ".join(s.courses),
                s.gpa
            ])
    
    print("Students exported successfully to students.csv")


# Auto Student Id Generation
def generate_student_id():
    year = datetime.datetime.now().year
    yy = str(year)[-2:]

    students = get_students()
    existing_ids = [s["student_id"] if isinstance(s, dict) else s.student_id for s in students]

    current_year_ids = [id for id in existing_ids if id.startswith(f"AIU{yy}")]

    if current_year_ids:
        max_serial = max(int(id[6:]) for id in current_year_ids)
        new_serial = max_serial + 1
    else:
        new_serial = 1

    return f"AIU{yy}{str(new_serial).zfill(4)}"


# Inputs Validity
def get_valid_number(prompt, min_val, max_val, value_type=float):
    while True:
        try:
            value = value_type(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print(f"Please enter a valid {value_type.__name__}.")


# Output for Multiple students
def print_students(students, title="Student List"):
    if not students:
        print("No students to display.")
        return

    print(f"\n== {title} ==")
    table = []
    for s in students:
        table.append([
            s.student_id,
            s.name,
            s.age,
            ", ".join(s.courses),
            s.gpa
        ])

    headers = ["ID", "Name", "Age", "Courses", "GPA"]
    print(tabulate(table, headers=headers, tablefmt="grid"))


# Single student
def print_student(student, title = ""):
    print_students([student], title)