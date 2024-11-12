class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}."

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_all_students(self):
        return [student.name for student in self.students]

    def get_all_teachers(self):
        return [teacher.name for teacher in self.teachers]

ram = Student("Ram", 20, "S123")
sita = Teacher("Sita", 35, "Mathematics")
school = School("Indian Public School")
school.add_student(ram)
school.add_teacher(sita)

print(ram.greet())
print(sita.greet())
print(ram.study())
print(sita.teach())
print(school.get_all_students())
print(school.get_all_teachers())