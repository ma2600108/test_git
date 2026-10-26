class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = []

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grades:", self. grade)

class UngraduateStudent(Student):
    def __init__(self, name, student_id, grade, major):
        super().__init__(name, student_id, grade)
        self.major=major
    
    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grades:", self.grade)
        print("Major:", self.major)

class GraduateStudent(Student):
    def __init__(self, name, student_id, grade, program_title):
        super().__init__(name, student_id, grade)
        self.program_title=program_title
        
    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grades:", self.grade)
        print("Program Title:", self.program_title)

a=UngraduateStudent("M","M",80,"M")
b=GraduateStudent("M","M",80,"M")

a.display_info()
b.display_info()

#testing to see if I am back!!!!!