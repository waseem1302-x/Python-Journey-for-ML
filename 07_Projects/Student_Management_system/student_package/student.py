class Student:
    def __init__(self, name, age, student_id, courses, gpa):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses
        self.gpa = gpa


    def __str__(self):
        return f"{self.student_id} - Name: {self.name}, Age: {self.age}, GPA: {self.gpa}, Courses: {', '.join(self.courses)}"
