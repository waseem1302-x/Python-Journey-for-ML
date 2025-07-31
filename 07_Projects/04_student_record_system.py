# Student Record System Project - Mid Level Project
# Author: Waseem Mushtaq (waseem1302-x)
# Description: A basic Python program to input students' marks, assign grades, show stats, and save data to a file.
# Tools used: Lists, Loops, Functions, If-Else, File Handling, Data Structures (lists,tuple,set and dictionaries)



def num_of_std():
    num = int(input("Enter Number of Students: "))
    return num


def add_std_data():
    name = input("Enter Student Name: ")
    student_id = int(input("Enter Student ID: "))

    marks = {
        "Math": int(input("Math Marks: ")),
        "Science": int(input("Science Marks: ")),
        "English": int(input("English Marks: "))
    }

    average = sum(marks.values()) / len(marks)

    if average >= 90:
        grade = 'A+'
    elif average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    else:
        grade = 'C'

    student = {
        "name": name,
        "id": student_id,
        "marks": marks,
        "average": average,
        "grade": grade
    }

    return student



def main():
    num = num_of_std()
    student_list = []

    for _ in range(num):
        student = add_std_data()  
        student_list.append(student)

    # Print student records
    for s in student_list:
        print("\n--- Student Report ---")
        print(f"Name: {s['name']}")
        print(f"ID: {s['id']}")
        print("Marks:")
        for subject, mark in s['marks'].items():
            print(f"  {subject}: {mark}")
        print(f"Average: {s['average']}")
        print(f"Grade: {s['grade']}")
main()

def find_topper(student_list):
    if not student_list:
        print("No students to evaluate.")
        return

    topper = student_list[0]

    for student in student_list[1:]:
        if student["average"] > topper["average"]:
            topper = student

    print("\n🏆 Topper Report 🏆")
    print(f"Name    : {topper['name']}")
    print(f"ID      : {topper['id']}")
    print(f"Average : {topper['average']}")
    print(f"Grade   : {topper['grade']}")

find_topper()

