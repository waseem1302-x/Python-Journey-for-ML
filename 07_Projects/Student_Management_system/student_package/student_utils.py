from .student import Student
from . import database

students = []

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    student_id = input("Enter Student ID: ")
    courses = input("Enter Student Courses (comma separated): ").split(",")
    gpa = float(input("Enter Student GPA: "))

    new_student = Student(name, age, student_id, [c.strip() for c in courses], gpa)
    database.save_students(new_student)
    print(f"Student '{name}' added successfully!")


def view_all_students():
    students = database.load_students()
    if not students:
        print("No student found\n")
        return
    
    print("\n=== All Students ===")
    for idx, student in enumerate(students, start=1):
        print(f"\nStudent {idx}")
        print(f"  Name     : {student.name}")
        print(f"  Age      : {student.age}")
        print(f"  ID       : {student.student_id}")
        print(f"  Courses  : {', '.join(student.courses)}")
        print(f"  GPA      : {student.gpa}")
    print()



def sort_students():

    students = database.load_students()
    if not students:
        print("No students found in the database.")
        return
    
    print("== Sort by ==")
    print("1: By Name (A-Z)")
    print("2: By ID (ascending)")
    print("3: By GPA (ascending)")
    choice = input("Enter Your Choice (1-3): ").strip()

    if choice == "1":
        sorted_list = sorted(students, key=lambda s: s.name.lower())
    elif choice == "2":
        sorted_list = sorted(students, key=lambda s: s.student_id)
    elif choice == "3":
        sorted_list = sorted(students, key=lambda s: s.gpa)
    else:
        print("Invalid choice.")
        return

    print("\n=== Sorted Students ===")
    for s in sorted_list:
        print(s)

def search_student():
    print("== Search By ==")
    print("1. Search by Name")
    print("2. Search by ID")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        name_query = input("Enter name to search: ").lower()
        results = [s for s in students if name_query in s.name.lower()]
        
        if results:
            print("\n=== Search Results ===")
            for s in results:
                print(s)
        else:
            print("No students found with that name.")

    elif choice == "2":
        id_query = input("Enter ID to search: ")
        results = [s for s in students if s.student_id == id_query]

        if results:
            print("\n=== Search Results ===")
            for s in results:
                print(s)
        else:
            print("No students found with that ID.")

    else:
        print("Invalid choice.")

def del_student():
    print("== Delete Student ==")
    print("1. By Name")
    print("2. By ID")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        del_std = input("Enter name to delete: ").lower()
        to_delete = [s for s in students if s.name.lower() == del_std]
        
        if to_delete:
            for s in to_delete:
                students.remove(s)
            print(f"{len(to_delete)} student(s) deleted successfully.")
        else:
            print("No student found with that name.")

    elif choice == "2":
        del_id = input("Enter ID to delete: ")
        to_delete = [s for s in students if s.student_id == del_id]
        
        if to_delete:
            for s in to_delete:
                students.remove(s)
            print(f"{len(to_delete)} student(s) deleted successfully.")
        else:
            print("No student found with that ID.")

    else:
        print("Invalid choice.")

    print("\n== Remaining Students ==")
    for s in students:
        print(s)
