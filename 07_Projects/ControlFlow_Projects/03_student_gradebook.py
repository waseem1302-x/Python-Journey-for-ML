# Student Gradebook Project - Beginner Version
# Author: Waseem Mushtaq (waseem1302-x)
# Description: A basic Python program to input students' marks, assign grades, show stats, and save data to a file.
# Tools used: Lists, Loops, Functions, If-Else, File Handling

# -------------------------------
# Function to calculate grade
# -------------------------------

def get_student_data():

    name = input("Enter Student Name: ")
    marks = int(input(f"Enter marks for {name} (0 -100): "))
    
    return name, marks

def validate_marks(marks):
    
    return 0 <= marks <= 100


def calculate_grade(marks):

    """
    Determine grade based on marks.
    """
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 75:
        return "A-"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "B-"
    else:
        return "Fail"

def calculate_summary(marks_list):
    """
    Calculate average, highest, and lowest marks.
    Returns a tuple (avg, max, min).
    """
    average = sum(marks_list) / len(marks_list)
    return average, max(marks_list), min(marks_list)

def save_to_file(names, marks_list, grades, average, highest, lowest):
    """
    Save all student data and summary stats to a text file.
    """
    with open("student_grades.txt", "w") as file:
        file.write("Student Gradebook\n")
        file.write("=========================\n")
        for i in range(len(names)):
            file.write(f"{names[i]} - Marks: {marks_list[i]} - Grade: {grades[i]}\n")
        file.write("\nSummary:\n")
        file.write(f"Average Marks: {average:.2f}\n")
        file.write(f"Highest Marks: {highest}\n")
        file.write(f"Lowest Marks: {lowest}\n")
    print("ata saved to 'student_grades.txt'")


def main():
    """
    Main function to control program flow.
    """
    names = []
    marks_list = []
    grades = []

    num_students = int(input("How many students? "))

    for i in range(num_students):
        print(f"\nStudent {i+1}:")
        name, marks = get_student_data()

        if not validate_marks(marks):
            print("Invalid marks! Skipping...")
            continue

        grade = calculate_grade(marks)

        names.append(name)
        marks_list.append(marks)
        grades.append(grade)

        print(f"{name} → Marks: {marks}, Grade: {grade}")

    if marks_list:
        average, highest, lowest = calculate_summary(marks_list)

        print("\nSummary:")
        print(f"Average Marks: {average:.2f}")
        print(f"Highest Marks: {highest}")
        print(f"Lowest Marks: {lowest}")

        save_to_file(names, marks_list, grades, average, highest, lowest)
    else:
        print("No valid student data to process.")

main()
