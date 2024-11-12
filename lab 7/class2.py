class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def __del__(self):
        print(f"Deleting {self.name}")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        super().display()
        print(f"Roll No: {self.roll_no}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")

ram = Student("Ram", 20, 101)
ram.display()

sita = Teacher("Sita", 35, "Mathematics")
sita.display()

del ram
del sita