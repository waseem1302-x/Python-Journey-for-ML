from .student import Student
from . import database
import datetime

students = []

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
    students = database.load_students()
    if not students:
        print("No student found\n")
        return
    
    print_students(students, "All Students")


# Sort Students
def sort_students():

    students = database.load_students()
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


# Search Students

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


def search_student():
    students = database.load_students()
    if not students:
        print("No students in database")
        return

    print("== Search Student ==")
    print("1. By Name")
    print("2. By ID")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ").lower()
        found = [s for s in students if s.name.lower() == name]
        if found:
            print_students(found, "Search Results")
        else:
            print("No student found with that name.")

    elif choice == "2":
        student_id = input("Enter ID: ")
        idx = binary_search_by_id(students, student_id)
        if idx != -1:
            print_students([students[idx]], "Search Result")
        else:
            print("No student found with that ID.")
    else:
        print("Invalid choice.")


# Delete Student
def del_student():
    students = database.load_students()
    if not students:
        print("No students in database")
        return

    print("== Delete Student ==")
    del_id = input("Enter ID to delete: ")
    idx = binary_search_by_id(students, del_id)

    if idx != -1:
        student_to_delete = students[idx]

        # Show student details before deletion
        print("\nStudent Found:")
        print(f"Name      : {student_to_delete.name}")
        print(f"Age       : {student_to_delete.age}")
        print(f"ID        : {student_to_delete.student_id}")
        print(f"Courses   : {', '.join(student_to_delete.courses)}")
        print(f"GPA       : {student_to_delete.gpa}")

        confirm = input(f"\nAre you sure you want to delete this student? (y/n): ").lower()
        if confirm == "y":
            students.pop(idx)
            database.save_students(students)
            print(f"\nStudent with ID {del_id} deleted successfully.")
            print_students(students, "Remaining Students")
        else:
            print("\nDeletion cancelled.")
    else:
        print("No student found with that ID.")


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

# Auto Student Id Generation
def generate_student_id():
    year = datetime.datetime.now().year
    yy = str(year)[-2:]

    students = database.load_students()  # load directly from JSON
    existing_ids = [s["student_id"] if isinstance(s, dict) else s.student_id for s in students]

    current_year_ids = [id for id in existing_ids if id.startswith(f"AIU{yy}")]

    if current_year_ids:
        max_serial = max(int(id[6:]) for id in current_year_ids)
        new_serial = max_serial + 1
    else:
        new_serial = 1

    return f"AIU{yy}{str(new_serial).zfill(4)}"


# Output
def print_students(students, title="Students"):
    if not students:
        print(f"\n== No {title} Found ==")
        return

    print(f"\n== {title} ==")
    for idx, student in enumerate(students, start=1):
        print(f"\nStudent {idx}")
        print(f"{'Name':<10}: {student.name}")
        print(f"{'Age':<10}: {student.age}")
        print(f"{'ID':<10}: {student.student_id}")
        print(f"{'Courses':<10}: {', '.join(student.courses) if student.courses else 'None'}")
        print(f"{'GPA':<10}: {student.gpa}")
        print("-" * 40)

