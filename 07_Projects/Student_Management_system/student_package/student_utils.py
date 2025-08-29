from .student import Student
from . import database
import datetime
from tabulate import tabulate
import csv
from .logger import logger 

# -----------------------------
# Utility Functions for Student Management System
# -----------------------------

# -----------------------------
# Load Students
# -----------------------------
def get_students():
    """
    Safely load students from the database.
    Returns a list of Student objects.
    """
    return database.load_students() or []

# -----------------------------
# Add Student
# -----------------------------
def add_students():
    """
    Add a new student after validating all inputs.
    """
    name = get_valid_input("Enter Student Name: ", validate_name)
    age = get_valid_input("Enter Age (15–30): ", validate_age)
    student_id = generate_student_id()
    print(f"\nAssigned Student ID: {student_id}")
    courses = get_valid_input(
        "Enter Student Courses (comma separated): ",
        lambda x: validate_courses([c.strip() for c in x.split(",")])
    )
    gpa = get_valid_input("Enter GPA (0–4): ", validate_gpa)

    new_student = Student(name, age, student_id, courses, gpa)

    try:
        database.add_student(new_student)
        print(f"Student '{name}' (ID: {student_id}) added successfully!")

        # log success
        logger.info(f"Student Added | ID={student_id} | Name={name} | Age={age}")

    except Exception as e:
        print(f"Error adding student: {e}")
        logger.error(f"Failed to add student | ID={student_id} | Error={e}")

# -----------------------------
# View Students
# -----------------------------
def view_all_students():
    """
    Display all students in a tabular format.
    """
    students = get_students()
    if not students:
        print("No students found.\n")
        logger.warning("View All | No students found.")
        return
    print_students(students, "All Students")
    logger.info(f"Viewed all students | Count={len(students)}")


# -----------------------------
# Sort Students
# -----------------------------
def sort_students():
    """
    Sort students by Name or ID.
    """
    students = get_students()
    if not students:
        print("No students found in the database.")
        logger.warning("Sort | No students available.")
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
        logger.warning(f"Sort | Invalid key entered: {choice}")
        return

    print_students(sorted_list, "Sorted Students")
    logger.info(f"Students sorted by {choice } | Count={len(sorted_list)}")

# -----------------------------
# Search Students
# -----------------------------
def binary_search_by_id(students, target_id):
    """
    Perform binary search on students sorted by ID.
    Returns index if found, else -1.
    """
    students_sorted = sorted(students, key=lambda s: s.student_id)
    left, right = 0, len(students_sorted) - 1
    while left <= right:
        mid = (left + right) // 2
        if students_sorted[mid].student_id == target_id:
            return mid
        elif students_sorted[mid].student_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_student(students, by="id", value=""):
    """
    Find students by ID or Name.
    Returns a list of matching Student objects.
    """
    if by == "id":
        idx = binary_search_by_id(students, value)
        return [students[idx]] if idx != -1 else []
    elif by == "name":
        value_lower = value.lower()
        return [s for s in students if value_lower in s.name.lower()]
    return []

def search_student():
    """
    Interactive search for a student by Name or ID.
    """
    students = get_students()
    if not students:
        print("No students in database.")
        logger.warning("Search | No students available.")
        return

    print("== Search Student ==")
    print("1. By Name")
    print("2. By ID")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        found = find_student(students, by="name", value=name)
        if found:
            print_students(found, "Search Results")
            logger.info(
                f"Search success | Search by=name | value={name} | Matches={len(found)}"
            )
        else:
            print("No student found with that name.")
            logger.warning(f"Search failed | Search by=name | value={name}")

    elif choice == "2":
        student_id = input("Enter ID: ").strip()
        found = find_student(students, by="id", value=student_id)
        if found:
            print_student(found[0], "Search Result")
            logger.info(
                f"Search success | Search by=id | value={student_id} | Matches={len(found)}"
            )
        else:
            print("No student found with that ID.")
            logger.warning(f"Search failed | by=id | value={student_id}")

    else:
        print("Invalid choice.")
        logger.warning(f"Search | Invalid choice entered: {choice}")

# -----------------------------
# Delete Student
# -----------------------------
def del_student():
    """
    Delete a student by ID with confirmation.
    """
    students = get_students()
    if not students:
        print("No students to delete.")
        return

    student_id = input("Enter ID to delete: ").strip()
    found = find_student(students, by="id", value=student_id)

    if found:
        print_student(found[0], "Student Found")
        confirm = input("Delete this student? (y/n): ").strip().lower()
        if confirm == "y":
            students.remove(found[0])
            try:
                database.save_students(students)
                print("Student deleted successfully.")
                logger.info(f"Student Deleted | ID={found[0]['student_id']} | Name={found[0]['name']}")

            except Exception as e:
                print(f"Error saving changes: {e}")
        else:
            print("Deletion cancelled.")
    else:
        print("No student found with that ID.")

# -----------------------------
# Export Students to CSV
# -----------------------------
def export_students():
    """
    Export students to a timestamped CSV file.
    """
    students = get_students()
    if not students:
        print("No students to export.")
        logger.warning("Export | No students available.")
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"students_{timestamp}.csv"

    try:
        with open(filename, "w", newline="") as f:
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
        print(f"Students exported successfully to {filename}")
        logger.info(f"Export successful | File={filename} | Count={len(students)}")
    except Exception as e:
        print(f"Error exporting students: {e}")
        logger.error(f"Export failed | File={filename} | Error={e}")

# -----------------------------
# Generate Student ID
# -----------------------------
def generate_student_id():
    """
    Generate a unique student ID in the format AIUYYXXXX.
    """
    year = datetime.datetime.now().year
    yy = str(year)[-2:]

    students = get_students()
    existing_ids = [s.student_id for s in students]

    current_year_ids = [id for id in existing_ids if id.startswith(f"AIU{yy}")]
    if current_year_ids:
        max_serial = max(int(id[5:]) for id in current_year_ids)
        new_serial = max_serial + 1
    else:
        new_serial = 1

    return f"AIU{yy}{str(new_serial).zfill(4)}"

# -----------------------------
# Print Students
# -----------------------------
def print_students(students, title="Student List"):
    """
    Print multiple students in a table.
    """
    if not students:
        print("No students to display.")
        return

    print(f"\n== {title} ==")
    table = [[s.student_id, s.name, s.age, ", ".join(s.courses), s.gpa] for s in students]
    headers = ["ID", "Name", "Age", "Courses", "GPA"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def print_student(student, title=""):
    """
    Print a single student in a table.
    """
    print_students([student], title)

# -----------------------------
# Validators
# -----------------------------
def get_valid_input(prompt, validator):
    """
    Repeatedly prompt the user until validator returns a valid value.
    """
    while True:
        user_input = input(prompt)
        result = validator(user_input)
        if isinstance(result, str) and "Error" in result:
            print(result)
            continue
        return result

def validate_name(name):
    name = name.strip()
    if not name:
        return "Error: Name cannot be empty"
    if not all(char.isalpha() or char == " " for char in name):
        return "Error: Name can only contain letters and spaces"
    return name.title()

def validate_age(age_input):
    age_input = age_input.strip()
    if not age_input.isdigit():
        return "Error: Age must be a number"
    age = int(age_input)
    if age < 15 or age > 30:
        return "Error: Age must be between 15 and 30"
    return age

def validate_courses(courses_list):
    if not courses_list or all(not c.strip() for c in courses_list):
        return "Error: At least one valid course must be entered"
    normalized = [c.strip().upper() for c in courses_list if c.strip()]
    return normalized

def validate_gpa(gpa_input):
    gpa_input = gpa_input.strip()
    try:
        gpa = float(gpa_input)
    except ValueError:
        return "Error: GPA must be a number"
    if gpa < 0.0 or gpa > 4.0:
        return "Error: GPA must be between 0.0 and 4.0"
    return gpa
