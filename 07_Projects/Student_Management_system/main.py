from student_package import student_utils as su
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("="*40)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Sort Students")
        print("4. Search Student")
        print("5. Delete Student")
        print("6. Export Students to CSV")
        print("7. Import Students from CSV & JSON")
        print("8. Exit")
        print("="*40)

        try:
            choice = input("Enter your choice (1-8): ").strip()
            if choice == "1":
                su.add_students()
            elif choice == "2":
                su.view_all_students()
            elif choice == "3":
                su.sort_students()
            elif choice == "4":
                su.search_student()
            elif choice == "5":
                su.del_student()
            elif choice == "6":
                su.export_students()
            elif choice == "7":
                su.import_students()
            elif choice == "8":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except KeyboardInterrupt:
            print("\nExiting program. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

        input("\nPress Enter to return to the main menu...")

            

if __name__ == "__main__":
    main_menu()