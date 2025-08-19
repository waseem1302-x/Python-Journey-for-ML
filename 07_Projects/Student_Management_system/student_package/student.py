class Student:
    def __init__(self, name, age, student_id, courses, gpa):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses
        self.gpa = gpa


    def __str__(self):
        return f"{self.student_id} - Name: {self.name}, Age: {self.age}, GPA: {self.gpa}, Courses: {', '.join(self.courses)}"

    def to_dict(self):
        """Convert Student object to dictionary for JSON storage"""
        return {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id,
            "courses": self.courses,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            age=data["age"],
            student_id=data["student_id"],
            courses=data["courses"],
            gpa=data["gpa"]
        )