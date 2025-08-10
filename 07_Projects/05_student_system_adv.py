class Student:
    def __init__(self, name, age, id, courses, gpa):
        self.name = name
        self.age = age
        self.id = id
        self.courses = courses
        self.gpa = gpa


    def __str__(self):
        return f"{self.id} - Name: {self.name}, Age: {self.age}, GPA: {self.gpa}, Courses: {" ".join(self.courses)}"

    
students = []

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    id = input("Enter Student ID: ")
    courses = input("Enter Student Courses: ")
    gpa = float(input("Enter Student GPA: "))

    new_student = Student(name,age,id,courses,gpa)
    students.append(new_student)
    print(f"Student '{name}' added successfully!")

def view_all_students():
    for s in students:
        print(s)


def sort_students():
    print("== Sort by ==")
    print("1: By Name (A-Z)")
    print("2: By ID (ascending)")
    print("3: By GPA (ascending)")
    choice = input("Enter Your Choice (1-3): ").strip()

    if choice == "1":
        sorted_list = sorted(students, key=lambda s: s.name.lower())
    elif choice == "2":
        sorted_list = sorted(students, key=lambda s: s.id)
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
        results = [s for s in students if s.id == id_query]

        if results:
            print("\n=== Search Results ===")
            for s in results:
                print(s)
        else:
            print("No students found with that ID.")

    else:
        print("Invalid choice.")



def main():
    while True:
        print("\n=== Student Management ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Sort Students")
        print("4. Search Student")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            sort_students()
        elif choice == "4":
            search_student()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()