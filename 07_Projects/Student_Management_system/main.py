from student_package import add_student, view_all_students, sort_students, search_student, del_student



def main():
    while True:
        print("\n=== Student Management ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Sort Students")
        print("4. Search Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            sort_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            del_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()